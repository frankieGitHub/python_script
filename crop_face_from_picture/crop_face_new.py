# -*- coding: UTF8 -*-
#import tensorflow as tf
#import numpy as np
import json
#import id2code
import subprocess
import urllib
import cv2
import os

#book = '/home/coolpad/AI/face_dataset/get_photo_from_internet/my_txt_2_jason/face_lib_1.txt'

def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
#    fsize = fsize/float(1024*1024)
#    return round(fsize,2)
    return fsize

def crop_and_save(race, gender, age, smile):
    older_str = ''
    smile_str = ''

    print('race is: %s' % race)
    print('gender is: %s' % gender)
    print('age is: %s' % str(age))
    print('smile is: %s' % str(smile))

    if(age > 53):
        older_str = 'old'
    elif(age <= 53 and age > 15):
        older_str = 'yong'
    else:
        older_str = 'child'
    if(smile < 3):
        smile_str = 'nothappy'
    elif(smile >= 3 and smile <20):
        smile_str = 'notsmile'
    else:
        smile_str = 'smile'
    folder_str = '%s_%s_%s_%s' % (race, gender, older_str, smile_str)
    print('getttttttttt: %s' % folder_str)

    return folder_str

output_str_image = './output'
for i in range(1,3):
    #print i
    book = './face_lib_%s.txt' % str(i)
    data_dir = './face_lib_%s' % str(i)
    #print book
    
    with open(book, 'r') as b:
        lines = b.readlines()
        for line in lines:
            #print line
            if(line == '\n'):
                continue
            l = json.loads(line)
            str_uid_pid = l['uid_pid']
            temp_s1 = str_uid_pid.split('.')
            uid_pid = temp_s1[0]

            print("we want to crop %s" % str_uid_pid)

            find_file = 0
            for mm1, mm2 ,files  in os.walk(data_dir):
                for file in files:
                    if(file == str_uid_pid):
                        print('find file %s, cropping....' % file)
                        local_file = data_dir + '/' + str_uid_pid
                        size = get_FileSize(local_file.encode("utf-8"))
                        if(size < 200):
                            break;
                        img = cv2.imread(local_file, cv2.IMREAD_COLOR)
                        #print('image x is:%d' % img.shape[1])
                        #print('image y is:%d' % img.shape[0])

                        scal_x = float(img.shape[1]/100.0)
                        scal_y = float(img.shape[0]/100.0)

                        #print('scale x is:%f' % scal_x)
                        #print('scale y is:%f' % scal_y)

                        for i in range(len(l['resp'])):
                            center_x = l['resp'][i]['position']['center']['x']
                            center_y = l['resp'][i]['position']['center']['y']
                            half_width = float((l['resp'][i]['position']['width'])/2)
                            half_high = float((l['resp'][i]['position']['height'])/2)

                            face_point1_x = int((center_x - half_width)*scal_x)
                            face_point1_y = int((center_y - half_high)*scal_y)

                            face_point2_x = int((center_x + half_width)*scal_x)
                            face_point2_y = int((center_y + half_high)*scal_y)

#                            print str(face_point1_x)
#                            print str(face_point1_y)
#                            print str(face_point2_x)
#                            print str(face_point2_y)

                            if(face_point2_y - face_point1_y < 100):
                                print('the face image is too small, ignore')
                                continue
                            crop = img[face_point1_y:face_point2_y, face_point1_x:face_point2_x]
  
                            #for mobilenet image input is 224*224
                            crop = cv2.resize(crop, (224, 224), interpolation=cv2.INTER_CUBIC )
                            cv2.imshow('Video', crop)


                            race = l['resp'][i]['attribute']['race']['value']
                            age = l['resp'][i]['attribute']['age']['value']
                            gender = l['resp'][i]['attribute']['gender']['value']
                            smile = l['resp'][i]['attribute']['smiling']['value'] 

                            folder_str = crop_and_save(race, gender, age, smile)
                            new_path = output_str_image + '/' + folder_str
                            #print(os.path.exists(new_path))
                            if(os.path.exists(new_path) == False):
                                os.mkdir(new_path)
                           
                            new_file_name = output_str_image + '/' + folder_str + '/' + uid_pid + '_' + str(i) + '.jpg' 
                            print('we are going to write %s' % new_file_name) 
                            cv2.imwrite(new_file_name, crop)

                            #cv2.imwrite(output_str_image + '/' + str_uid_pid , crop)
                            cv2.waitKey(0)

                       #print('%s has found' % file)
                        find_file = 1
                if(find_file == 1):
                    break;
            if(find_file == 1):
                print('pic found and deal done')
            else:
                print('%s has not found.' % str_uid_pid)

        
