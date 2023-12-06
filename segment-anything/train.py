import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import cv2
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor
 
matplotlib.use('TkAgg')
 
def show_anns(anns):
    if len(anns) == 0:
        return
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
    ax = plt.gca()
    ax.set_autoscale_on(False)
    polygons = []
    color = []
    for ann in sorted_anns:
        m = ann['segmentation']
        img = np.ones((m.shape[0], m.shape[1], 3))
        color_mask = np.random.random((1, 3)).tolist()[0]
        for i in range(3):
            img[:,:,i] = color_mask[i]
        ax.imshow(np.dstack((img, m*0.35)))
 
sys.path.append("..")
 
 
sam_checkpoint = "sam_vit_b_01ec64.pth"
model_type = "vit_b"
 
device = "cuda"#如果想用cpu,改成cpu即可
 
sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device=device)
 
image = cv2.imread('notebooks/images/dog.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# plt.figure(figsize=(20,20))
# plt.imshow(image)
# plt.axis('off')
# plt.show()
 
 
mask_generator = SamAutomaticMaskGenerator(sam)
 
masks = mask_generator.generate(image)
print(len(masks))
plt.figure(figsize=(20,20))
plt.imshow(image)
show_anns(masks)
plt.axis('off')
plt.show()
# import torch # 如果pytorch安装成功即可导入
# print(torch.cuda.is_available()) # 查看CUDA是否可用
# print(torch.cuda.device_count()) # 查看可用的CUDA数量
# print(torch.version.cuda) # 查看CUDA的版本号