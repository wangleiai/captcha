import os
from PIL import Image
import numpy as np

def get_data(file_path):
    dirs = os.listdir(file_path)
    image_path = []
    image_label = []
    # print(dirs)
    for d in dirs:
        s = d.split('.')

        label = s[0]
        path = os.path.join(file_path, d)
        # print(label)
        # print(path)
        # break
        image_label.append(label)
        image_path.append(path)
    return image_path, image_label

def getImage(img_path):
    return np.array(Image.open(img_path, mode='r'))

def resizeAndSave(image_pathes, image_labels, save_path):
    for i in range(len(image_labels)):
        img = Image.open(image_paths[i])
        img = img.resize((170, 80), Image.ANTIALIAS)
        sp = save_path+'/'+str(label[i])+'.jpg'
        img.save(sp, quality = 95)

if __name__ == '__main__':
    train_file_path = 'D:\BaiduYunDownload\jwxt_captcha_data/train'
    train_image_path, train_image_label = get_data(train_file_path)
    print(train_image_label)
    
    train_save_path = 'D:\BaiduYunDownload\jwxt_captcha_data\ntrain'
    resizeAndSave(train_image_path, train_image_label, train_save_path)

    test_file_path = 'D:\BaiduYunDownload\jwxt_captcha_data/test'
    test_image_path, test_image_label = get_data(test_file_path)
    print(test_image_label)
    
    test_save_path = 'D:\BaiduYunDownload\jwxt_captcha_data\ntest'
    resizeAndSave(test_image_path, test_image_label, test_save_path)

    # get_bs_data(image_path, image_label)
    # for i,j in get_bs_data(image_path, image_label):
    #     print(i)
    #     print(j)