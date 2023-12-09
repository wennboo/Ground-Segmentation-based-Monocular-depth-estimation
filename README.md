### Ground Segmentation based Monocular depth estimation 基于图像地面分割处理的单目深度估计
The python code is provided for ground-segmentation based monocular depth estimation.
``src`` file is the python source file.

#### Condensed Abstract

A monocular depth estimation method based on image ground segmentation is proposed to address the issues of inaccurate object edge positioning and limited long-range plane depth capability in monocular depth estimation tasks. Firstly, an improved SE DenseNet depth model is proposed to achieve monocular depth estimation. The model adopts an encoder-decoder structure, and the encoder adopts a DenseNet network. The attention network SENet is embedded in the encoder, which adaptively learns the contribution of each channel to depth information to assign weights to the channels. Then, the encoder extracts features layer by layer to regress the depth image. Jumping connections are added between the decoder and encoder to alleviate network degradation and effectively improve object edge positioning problems. Secondly, a ground segmentation algorithm based on SAM is proposed, which uses prompts to quickly segment the ground information. Finally, the fusion of depth images and ground segmentation images achieved monocular depth estimation.

---

#### Installation
Prerequisites
- python3
- pytorch
- ipykernel
- pillow
- numpy
- torchvision
---

#### Dataset

The information about the NYUv2 dataset could be seen in the following link:
https://github.com/ankurhanda/nyuv2-meta-data

---

#### Usage

You can train the model through the following file:
```py
SE-DenseNet/PyTorch/train.py
```
You can test the segmentation module through the following file:
```py
segment-anything/test.py
```

#### simulation

![p](pic/simulation.png)

