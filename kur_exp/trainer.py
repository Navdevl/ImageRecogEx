#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import numpy as np
from scipy.ndimage import imread

cats = {'apple':0, 'orange':1}
data = {'images':[], 'labels':[]}
for i in range(1,10):
    apple = imread('resized/apple{0}.jpg'.format(i), flatten=True)
    orange = imread('resized/orange{0}.jpg'.format(i), flatten=True)
    data['images'].append(apple)
    data['labels'].append([cats['apple']])

    data['images'].append(orange)
    data['labels'].append([cats['orange']])

data['images'] = np.array(data['images']).reshape(18,1,-1)
print data['images'].shape
data['labels'] = np.array(data['labels']) #.reshape(-1,1,1,1)
print data['labels'].shape
#print data['labels']
with open('data.pkl', 'w') as file:
    pickle.dump(data, file, protocol=2)

with open('evaluate.pkl', 'w') as file:
    pickle.dump(data, file, protocol=2)
