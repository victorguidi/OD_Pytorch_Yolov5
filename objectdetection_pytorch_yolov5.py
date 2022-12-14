# -*- coding: utf-8 -*-
"""ObjectDetection_pytorch_Yolov5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kj5NSOQbrV_CxdncmSId5GtWgZMcrJjB
"""

!pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu

!git clone https://github.com/ultralytics/yolov5
!cd yolov5 && pip3 install -r requirements.txt

import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Images
img = 'https://reviewed-com-res.cloudinary.com/image/fetch/s--NfTzdRCA--/b_white,c_limit,cs_srgb,f_auto,fl_progressive.strip_profile,g_center,q_auto,w_1200/https://reviewed-production.s3.amazonaws.com/1531323557000/P1012724.jpg'  # or file, Path, PIL, OpenCV, numpy, list
# Inference
results = model(img)
# Results
results.pandas()  # or .show(), .save(), .crop(), .pandas(), etc.

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
plt.imshow(np.squeeze(results.render()))
plt.show()

#Training a model for identify a fire extinguisher

!cd yolov5/ && python train.py --img 320 --batch 16 --epochs 5 --data dataset.yaml --weights yolov5s.pt

model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp4/weights/best.pt', force_reload=True)

results = model('https://reviewed-com-res.cloudinary.com/image/fetch/s--NfTzdRCA--/b_white,c_limit,cs_srgb,f_auto,fl_progressive.strip_profile,g_center,q_auto,w_1200/https://reviewed-production.s3.amazonaws.com/1531323557000/P1012724.jpg')
results.print()



