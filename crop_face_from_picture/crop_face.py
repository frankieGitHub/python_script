#import tensorflow as tf
#import numpy as np
import json
import id2code
import subprocess
import urllib
import cv2
import os

#book = '/home/coolpad/AI/face_dataset/get_photo_from_internet/my_txt_2_jason/face_lib_1.txt'

for i in range(1,21):
    #print i
    book = '../face_lib_%s.txt' % str(i)
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
            print("we want to crop %s" % str_uid_pid)

            find_file = 0
            for mm1, mm2 ,files  in os.walk(data_dir):
                for file in files:
                    if(file == str_uid_pid):
                        print('find file %s, cropping....' % file)
                        local_file = data_dir + '/' + str_uid_pid
                        img = cv2.imread(local_file, cv2.IMREAD_COLOR)
                        print('image x is:%d' % img.shape[1])
                        print('image y is:%d' % img.shape[0])

                        scal_x = float(img.shape[1]/100.0)
                        scal_y = float(img.shape[0]/100.0)

                        print('scale x is:%f' % scal_x)
                        print('scale y is:%f' % scal_y)

                        for i in range(len(l['resp'])):
                            center_x = l['resp'][i]['position']['center']['x']
                            center_y = l['resp'][i]['position']['center']['y']
                            half_width = float((l['resp'][i]['position']['width'])/2)
                            half_high = float((l['resp'][i]['position']['height'])/2)

                            face_point1_x = int((center_x - half_width)*scal_x)
                            face_point1_y = int((center_y - half_high)*scal_y)

                            face_point2_x = int((center_x + half_width)*scal_x)
                            face_point2_y = int((center_y + half_high)*scal_y)

                            print str(face_point1_x)
                            print str(face_point1_y)
                            print str(face_point2_x)
                            print str(face_point2_y)

                            crop = img[face_point1_y:face_point2_y, face_point1_x:face_point2_x]
   
                            crop = cv2.resize(crop, (224, 224), interpolation=cv2.INTER_CUBIC )
                            cv2.imshow('Video', crop)
                            #cv2.imwrite(output_str_image , crop)
                            cv2.waitKey(0)

                       #print('%s has found' % file)
                        find_file = 1
                if(find_file == 1):
                    break;
            if(find_file == 1):
                print('pic found and deal done')
            else:
                print('%s has not found.' % str_uid_pid)

        
