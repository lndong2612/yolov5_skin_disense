import cv2

im_path = './data/images/skin_disense/haclao.jpg'
# # doc = {'xmax': 338, 'xmin': 181, 'ymax': 425, 'ymin': 258}

im = cv2.imread(im_path)
# start_point = (338, 425)
# end_point = (181, 258)
# # Blue color in BGR
# color = (255, 0, 0)
# # Line thickness of 2 px
# thickness = 2
# image = cv2.rectangle(im, start_point, end_point, color, thickness)
# cv2.imshow('im', image)
# cv2.waitKey(0)

classified = [{'xmin': 27, 'ymin': 300, 'xmax': 178, 'ymax': 430, 'score': '0.35', 'label': 'Zona'}, 
            {'xmin': 29, 'ymin': 301, 'xmax': 174, 'ymax': 432, 'score': '0.54', 'label': 'Ringworm'}, 
            {'xmin': 181, 'ymin': 258, 'xmax': 338, 'ymax': 425, 'score': '0.88', 'label': 'Ringworm'}]
fontScale = 0.5
image_h, image_w, _ = im.shape
bbox_thick = int(0.6 * (image_h + image_w) / 600)
bbox_color = (0, 255, 0)
thickness = 2

for info in classified:
    print(info)
    xmin = info['xmin']
    ymin = info['ymin']
    xmax = info['xmax']
    ymax = info['ymax']
    c1, c2 = (xmin, ymin), (xmax, ymax)
    score = float(info['score'])
    if score < 0.5:
        pass
    else:
        bbox_mess = '%s - %s' % (info['label'], info['score'])
        t_size = cv2.getTextSize(bbox_mess, 0, fontScale, thickness=bbox_thick // 2)[0]
        c3 = (c1[0] + t_size[0], c1[1] - t_size[1] - 7)      
        cv2.rectangle(im, c1, c2, bbox_color, thickness)
        cv2.rectangle(im, c1, c3, bbox_color, -1) #filled
        cv2.putText(im, bbox_mess, (c1[0] + 1, c1[1] - 3), cv2.FONT_HERSHEY_SIMPLEX,
                fontScale, (0, 0, 0), bbox_thick // 2, lineType=cv2.LINE_AA)    
cv2.imshow('im', im)
cv2.waitKey(0)