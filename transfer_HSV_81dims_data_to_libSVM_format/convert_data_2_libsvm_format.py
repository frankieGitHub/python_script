#import numpy as np
import math

data_file = './attribute.txt'
output_file = './libsvm_data.txt'

f_output = open(output_file, 'wr')


with open(data_file, 'r') as b:
    lines = b.readlines()
    index = 1
    for line in lines:
        array = line.split('\t')
    
        sum_line = 0.0
        for i in range(0, 81):
            sum_line += float(array[i])
    
        mean = sum_line/81

        sum2 = 0.0
        for i in range(0, 81):
            sum2 += ((float(array[i]) - mean)*(float(array[i]) - mean))

        std = math.sqrt(sum2/81)

        new_line = ''
        if(index <= 5105):
            new_line = '0 1:%s' % str((float(array[0])-mean)/std)
        else:
            new_line = '1 1:%s' % (array[0])
        
        for j in range(1,81):
            new_line = new_line + ' ' + str(j+1) + ':' + ((str((float(array[j])-mean)/std)))

        print new_line
        f_output.writelines(new_line)
        f_output.writelines('\n')

        index += 1
f_output.close()
        
