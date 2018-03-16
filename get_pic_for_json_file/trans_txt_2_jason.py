#import tensorflow as tf
#import numpy as np
import json
import id2code
import subprocess
import urllib

book = '/home/coolpad/AI/face_dataset/get_photo_from_internet/my_txt_2_jason/face_lib_1.txt'

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
print("hee")
