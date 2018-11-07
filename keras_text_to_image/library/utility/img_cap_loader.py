import os
import numpy as np
from keras.preprocessing.image import img_to_array, load_img


def load_normalized_img_and_its_text(img_dir_path, txt_dir_path, img_width, img_height):
    wrong_name = dict()
    images = dict()
    texts = dict()
    count = 0
    for f in os.listdir(txt_dir_path):
        count= count+1
        filepath = os.path.join(txt_dir_path, f)
        if os.path.isfile(filepath) and f.endswith('.txt'):
            name = f.replace('.txt', '')
            print(name)
            try:
                texts[name] = open(filepath, 'rt').read()   #.decode('iso-8859-1').encode('utf-8')
                wrong_name[name] = False
            except:
                wrong_name[name] = True
    print(count)
    for f in os.listdir(img_dir_path):
        filepath = os.path.join(img_dir_path, f)
        if os.path.isfile(filepath) and f.endswith('.jpg'):
            name = f.replace('.jpg', '')
            if wrong_name[name]:
                continue
            images[name] = filepath

    result = []
    count = 0
    for name, img_path in images.items():
        if name in texts:
            if name == "magikarp":
                continue
            if wrong_name[name]:
                continue
            if (count == 7000):
                break

            text = texts[name]
            image = img_to_array(load_img(img_path, target_size=(img_width, img_height)))
            image = (image.astype(np.float32) / 255) * 2 - 1
            result.append([image, text])
            count = count+1

    print(len(result))

    return np.array(result)