from segment_anything import build_sam, SamPredictor
import numpy as np
import cv2
image = cv2.imread('./notebooks/images/dog.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
predictor = SamPredictor(build_sam(checkpoint="./sam_vit_b_01ec64.pth"))
predictor.set_image(image)
input_point = np.array([[800, 534]])
input_label = np.array([1])

masks, _, _ = predictor.predict(    point_coords=input_point,
    point_labels=input_label,
    multimask_output=True,)
print('Done')

