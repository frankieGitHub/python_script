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
    data_dir = '../face_lib_%s' % str(i)
    #print book
    
    with open(book, 'r') as b:
        lines = b.readlines()
        for line in lines:
            #print line
            if(line == '\n'):
                continue
            l = json.loads(line)
            str_uid_pid = l['uid_pid']
            #print("we want to download %s" % str_uid_pid)

            find_file = 0
            for mm1, mm2 ,files  in os.walk(data_dir):
                for file in files:
                    #print('find file %s' % file)
                    if(file == str_uid_pid):
                        #print('%s has found' % file)
                        find_file = 1
                        break;
                if(find_file == 1):
                    break;
            if(find_file == 1):
                continue
            else:
                print('%s has not found.downloading.....' % str_uid_pid)

            #continue

            s1 = str_uid_pid.split('_')
            uid = s1[0]
            temp = s1[1]
            s2 = temp.split('.')
            pid = s2[0]
            url = id2code.generateUrl(pid)

            if(url == 'abcdefg'):
                continue
            save_2_local_file = './face_lib_%s/%s' % (str(i), str_uid_pid)
            urllib.urlretrieve(url, save_2_local_file)
            print('%s download OK' % str_uid_pid)



'''
            img = cv2.imread(save_2_local_file, cv2.IMREAD_COLOR)
            for i in range(len(l['resp'])):
                face_point1_x = int(l['resp'][i]['position']['center']['x'] - \
                        100)
                        #(l['resp'][i]['position']['width'])/2)
                face_point1_y = int(l['resp'][i]['position']['center']['y'] - \
                              100)
                              #(l['resp'][i]['position']['height'])/2)

                face_point2_x = int(l['resp'][i]['position']['center']['x'] + \
                        100)
                        #(l['resp'][i]['position']['width'])/2)
                face_point2_y = int(l['resp'][i]['position']['center']['y'] + \
                            100)
                              #(l['resp'][i]['position']['height'])/2)
               
                print str(face_point1_x)
                print str(face_point1_y)
                print str(face_point2_x)
                print str(face_point2_y)

                #crop = img[face_point1_x:face_point2_x, face_point1_y:face_point2_y]
   
                #crop = cv2.resize(crop, (224, 224), interpolation=cv2.INTER_CUBIC )
                cv2.imshow('Video', img)
                #cv2.imwrite(output_str_image , crop)

                #print l['resp'][i]['attribute']['gender']['value']
            
            #gender = l['resp']
            #print len(gender)
            
            #gender = l['resp']['attribute']['gender']['value']
            #print gender
            

            #cv2.imshow('Video', img)
            cv2.waitKey(0)
'''
'''
#d = json.load(open(book, 'r'))
#print d, type(d)

fopen=open(book,'r')

lines=fopen.readlines()
for line in lines:
    if(line == '\n'):
        continue
    l = json.loads(line)
    print l['uid_pid']
    str_uid_pid = l['uid_pid']
    s1 = str_uid_pid.split('_')
    uid = s1[0]
    temp = s1[1]
    print(uid)
    s2 = temp.split('.')
    pid = s2[0]
    print(pid)
    url = id2code.generateUrl(pid)
    print(url)

    if(url == 'abcdefg'):
        continue

    urllib.urlretrieve(url, './face_lib_1/%s' % str_uid_pid)
    print('%s download OK' % str_uid_pid)
    
    #cmd='wget %s -O ./face_lib_1/%s' % (url, str_uid_pid)
    #res = subprocess.call(cmd,shell=True)
    #print res

    

#with open(book, 'r') as b:
#    book_list = b.read().splitlines()
#    print book_list
    #j = json.dumps(book_list)
    #l = json.loads(j)
    #print l['uid_pid']

#d = json.load(open(book, 'r'))
#print d, type(d)

#data = dict(book_list)
#print type(data)
#print data
#
#j = json.dump(data)
#print type(j)
#print j
#
'''
