import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

idx = '000013'
wkdir = '/home/hyao/Documents/pseudo_lidar'



plt.figure(figsize=(10,10))

image2_file_path = '{}/KITTI/object/testing/image_2/{}.png'.format(wkdir, idx)
image2 = cv2.imread(image2_file_path)
plt.subplot(3,1,1)
plt.imshow(image2)

image3_file_path = '{}/KITTI/object/testing/image_3/{}.png'.format(wkdir, idx)
image3 = cv2.imread(image3_file_path)
plt.subplot(3,1,2)
plt.imshow(image3)

disparity_file_path = '{}/KITTI/object/testing/predict_disparity/{}.npy'.format(wkdir, idx)
disparity = np.load(disparity_file_path)
plt.subplot(3,1,3)
plt.imshow(disparity)
plt.show()

pc_file_path = '{}/KITTI/object/testing/pseudo-lidar_velodyne/{}.bin'.format(wkdir, idx)
script_path = './SAIC/pyutility/show_utility.py'
os.system('python {} --pc={}'.format(script_path, pc_file_path))

pc_file_path = '{}/KITTI/object/testing/velodyne/{}.bin'.format(wkdir, idx)
os.system('python {} --pc={}'.format(script_path, pc_file_path))





disparity_file_path = '{}/KITTI/object/training/predict_disparity/{}.npy'.format(wkdir, idx)
disparity = np.load(disparity_file_path)
plt.subplot(3,1,1)
plt.imshow(disparity)
plt.title('predict')
disparity_file_path = '{}/KITTI/object/training/disparity/{}.npy'.format(wkdir, idx)
disparity = np.load(disparity_file_path)
plt.subplot(3,1,3)
plt.imshow(disparity)
plt.title('gt predict')
plt.title('gt')
plt.show()


script_path = './SAIC/pyutility/show_utility.py'
pc_file_path = '{}/KITTI/object/training/velodyne/{}.bin'.format(wkdir, idx)
os.system('python {} --pc={}'.format(script_path, pc_file_path))
pc_file_path = '{}/KITTI/object/training/pseudo-lidar_velodyne/{}.bin'.format(wkdir, idx)
os.system('python {} --pc={}'.format(script_path, pc_file_path))

