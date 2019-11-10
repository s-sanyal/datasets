import os
import cv2
import skimage
import matplotlib.pyplot as plt

DIR = './class_train'
NEW_DIR = './class_noisy/'
try:
    if not os.path.exists(NEW_DIR):
        os.makedirs(NEW_DIR)
except OSError:
    print("Error Creating Directory " + NEW_DIR)

print('Starting to add Noise .... ')
for img in os.listdir(DIR):
    img_path = os.path.join(DIR, img)
    img_name, idx, img_type = img.split('.')
    raw_img = cv2.imread(img_path)
    noisy = skimage.util.random_noise(raw_img, mode="s&p")
    noisy_image = skimage.util.random_noise(noisy, mode="gaussian")
    cv2.imwrite(os.path.join(NEW_DIR, img_name+'.'+idx+'.'+img_type), 255.0*noisy_image)
print('Done !!!')