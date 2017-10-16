import cv2
from PIL import Image
import numpy as np

height = 288
width = 512
batch_size = 32
initial_learning_rate = 1e-4
theta_mul = 1000
regu_mul = 10000
training_iter = 100000
step_size = 30000
train_data_size = 4000
test_data_size = 600
crop_rate = 0.8
batch_size = 20
before_ch = 7
after_ch = 7
tot_ch = before_ch + after_ch + 1
test_batches = 10
random_crop_rate = 0.9
disp_freq = 50
test_freq = 500
save_freq = 1000

def cvt_img2train(img, crop_rate = 1):
    img = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY))
    if (crop_rate != 1):
        h = int(height / crop_rate)
        dh = int((h - height) / 2)
        w = int(width / crop_rate)
        dw = int((w - width) / 2)

        img = img.resize((w, h), Image.BILINEAR)
        img = img.crop((dw, dh, dw + width, dh + height))
    else:
        img = img.resize((width, height), Image.BILINEAR)
    img = np.array(img)
    img = img * (1. / 255) - 0.5
    img = img.reshape((1, height, width, 1))
    return img
