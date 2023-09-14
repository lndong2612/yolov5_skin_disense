import random
import cv2
import numpy as np
from PIL import ImageDraw, Image
import json
number_of_colors = 5

def check_color(eng_name):
    menu_color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
    with open('skin_disense.json', 'r',encoding='utf-8') as outfile:
        json_object = json.load(outfile)
        for info in json_object['english_name']:
            try:
                ID = info[eng_name][0]['ID']
            except Exception:
                pass
    return menu_color[ID]

# # color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
# #              for i in range(number_of_colors)]
# # input_image = './test/images/skin_disense/langben.jpg'
# # image = cv2.imread(input_image)
# # cv2_im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)# Convert the image to RGB (OpenCV uses BGR)
# # pil_im = Image.fromarray(cv2_im_rgb)# Transform the cv2 image to PIL    
# # draw = ImageDraw.Draw(pil_im)
# # shape = [(3, 8), (370, 35)]      
# # draw.rectangle(shape, fill = color[0])
# # img = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)# Get back the image to OpenCV

eng_name = 'Ringworm'
# label = ''
color = check_color(eng_name)
print(color)

