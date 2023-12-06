import matplotlib.image as mpimg#读取图片
import matplotlib.pyplot as plt #显示图片
from PIL import Image
import os
import string
 
# path = "E:\\LT0514\\data\\"         #最后要加双斜杠，不然会报错
# filelist=os.listdir(path)
 
# for file in filelist:
#     whole_path = os.path.join(path, file)
#     img = Image.open(whole_path)  # 打开图片img = Image.open(dir)#打开图片
#     img = img.convert("RGB") # 将一个4通道转化为rgb三通道
#     save_path =  'E:\\LT0514\\data1\\' 
#     #img.save(save_path + img1)
#     img.save(save_path + file)

image = Image.open('./examples/1_image.png')
print(image.size)
img = image.convert("RGB")
print(img.size)

plt.title('Read Image by Matplotlib')
plt.axis('off')# 不显示坐标轴
plt.imshow(image)
plt.show()


