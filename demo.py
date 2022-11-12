import os
import cv2
import numpy as np
root_path="./images"
out_path="./result"
A1 = np.array([255,255,255])
D1=np.array([250,250,250])
B1=np.array([0,0,0])
C1=np.array([100,100,100])
add_num=np.array([50,50,50]).astype(np.uint8)
black=np.array([0,0,0]).astype(np.uint8)
# sub_num=np.array([50,50,50]).astype(np.uint8)
# print(add_num)
for i in os.listdir(root_path):
    filename=os.path.join(root_path,i)
    img=cv2.imread(filename)
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            # if (img[x,y,:]<=A1-add_num).all() and (img[x,y,:]>B1).all():
            if (img[x,y,:]>B1).all() and (img[x,y,:]<D1).all():
                # print(img[x][y])
                # img[x][y]+=add_num
                # print(img[x][y])
                img[x][y]=black
                # img[x][y]=(img[x][y]*0.3).astype(np.uint8)
                # print(img[x][y])
                # print(img[x][y])
    tmp_img = np.where(img > 255, 255, img)
    out_img = np.where(tmp_img < 0, 0, tmp_img)
    # cv2.imshow("img",out_img)
    # cv2.waitKey(0)
    cv2.imwrite(os.path.join(out_path,i),out_img)