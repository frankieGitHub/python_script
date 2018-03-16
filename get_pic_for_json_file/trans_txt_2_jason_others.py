#import tensorflow as tf
#import numpy as np
import json
import id2code
import subprocess
import urllib
import cv2

#book = '/home/coolpad/AI/face_dataset/get_photo_from_internet/my_txt_2_jason/face_lib_1.txt'

for i in range(2,21):
    print i
    book = './face_lib_%s.txt' % str(i)
    print book
    
    with open(book, 'r') as b:
        lines = b.readlines()
        for line in lines:
            #print line
            if(line == '\n'):
                continue
            l = json.loads(line)
            str_uid_pid = l['uid_pid']
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


            for i in range(len(l['resp'])):
                print l['resp'][i]['attribute']['gender']['value']
            #img = cv2.imread(save_2_local_file, cv2.IMREAD_COLOR)
            
            #gender = l['resp']
            #print len(gender)
            
            #gender = l['resp']['attribute']['gender']['value']
            #print gender
            

            #cv2.imshow('Video', img)
            cv2.waitKey(0)

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
