#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 17:01:13 2022

@author: data
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt
#%%

img = cv2.imread('downloads/stars-s-b.jpeg')
#%%
print(np.max(img[:,:,0]))
print(np.min(img[:,:,0]))
print(np.max(img[:,:,1]))
print(np.min(img[:,:,1]))
print(np.max(img[:,:,2]))
print(np.min(img[:,:,2]))

#%% Dimmer
b_1 = 0
g_1 = 0
r_1 = 0

b_2 = 178
g_2 = 178
r_2 = 178

b = ((255 - b_1)/255) * ((b_2 - b_1)/(255 - b_1))
g = ((255 - g_1)/255) * ((g_2 - g_1)/(255 - g_1))
r = ((255 - r_1)/255) * ((r_2 - r_1)/(255 - r_1))

img[:,:,0] = img[:,:,0] * b + b_1
img[:,:,1] = img[:,:,1] * g + g_1
img[:,:,2] = img[:,:,2] * r + r_1
cv2.imwrite('downloads/stars-s-b-temp.jpeg', img)

#%% Inverse
img = 255 - img
cv2.imwrite('downloads/stars-s-w-temp.jpeg', img)

#%%


#%%
from PIL import Image


img = Image.open('downloads/after copy.jpg')
#%%

box = (80, 0, 6144, 4096)
img = img.crop(box)
img.save('downloads/after.jpg')

