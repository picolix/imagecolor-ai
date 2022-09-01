#PicoLix Design
import cv2
import tensorflow as tf
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('image_path', nargs='+', help='path to image file list')
args = parser.parse_args()
image_path = args.image_path

loaded = tf.saved_model.load(export_dir='./')
print(list(loaded.signatures.keys()))

infer = loaded.signatures["serving_default"]
print(infer.structured_outputs)

imgbytes = list()
for path in image_path:
        img = cv2.imread(path)
        rst,bts = cv2.imencode('.png', img)
        imgbytes.append(bts.tobytes())

out = infer(key=tf.constant('uniq_dummy_id_123'), image_bytes=tf.constant(imgbytes))
print(out)

scores = out["scores"]
labels = out["labels"]

num = scores.numpy().shape[0]
for j in range(num):
        top = np.argsort(-scores.numpy()[j])
        print(image_path[j])
        for i in range(3):
                print('%d: %-7.6f : %s' % (i + 1,scores.numpy()[j][top[i]], labels.numpy()[j][top[i]].decode('utf-8')))
