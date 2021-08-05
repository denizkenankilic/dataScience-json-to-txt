import os
import json
from skimage import io

def read_json(json_path,json_file):
    with open(os.path.join(json_path,json_file)) as f:
        data = json.load(f)
    f.close()
    return data


json_folder_path = 'Data/json_labels/AOI_34'
image_path = 'Data/images/AOI_34'
txt_folder_path = 'Data/txt_labels/AOI_34'
image_type = 'bmp'

if not os.path.exists(txt_folder_path):
    os.makedirs(txt_folder_path)

image_list = os.listdir(image_path)
json_list = os.listdir(json_folder_path)
f = None
for json_file in json_list:
    if ((os.path.isdir(os.path.join(json_folder_path, json_file)))):
        continue
    if (f != None):
        f.close()

    file_name,file_extension = os.path.splitext(json_file)
    f = open(txt_folder_path + '/' + file_name + '.txt', 'a')
    im = io.imread(os.path.join(image_path, file_name+'.' + image_type))
    im_width = im.shape[1]
    im_height = im.shape[0]

    json_data = read_json(json_folder_path,json_file)
    gt_samples = json_data['samples']
    for sample in gt_samples:
        class_num = sample["class"]
        width = float(sample['width'])
        height = float(sample['height'])
        x_center = (float(sample['x']) + width/2)/im_width
        y_center = (float(sample['y']) + height/2)/im_height
        f.write(str(class_num)+' '+str(x_center) + ' ' + str(y_center) + ' ' + str(width/im_width) + ' ' + str(height/im_height) +'\n')
