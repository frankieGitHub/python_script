import tensorflow as tf
import numpy as np

import label_image
import os,shutil

data_dir = "/home/coolpad/AI/face_dataset/auto_classify/temp"
output_dir = "/home/coolpad/AI/face_dataset/auto_classify/to"

for mm1, mm2 ,files  in os.walk(data_dir):
    for images in files:
        images_path = data_dir + "/" + images
        print(images_path)
        res = label_image.hello(images_path)
        print (str(res))
        if(res == 0):
            dest = output_dir + "/" + "black"
            print("000000")
        elif(res == 1):
            dest = output_dir + "/" + "white"
            print("111111")
        elif(res == 2):
            dest = output_dir + "/" + "yellow"
            print("22222")
        shutil.move(images_path, dest)
