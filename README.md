# tfcolor2

You can get the top 3 image colors of the image.  
Inference in python,tensorflow using image color trained model saved_model.pb.  
A saved_model.pb is GCP Auto ML Edge mode, export container TensorFlow saved model file. 

## Usage
python tfcolor2.py imagefile1 [imagefile2 ...]

## Installation  
python3,TensorFlow2  

pip3 install numpy  
pip3 install opencv-python  
pip3 install tensorflow  
pip3 install argparse  

## Include packages
saved_model.pb   : Image Color Learned Model (TensorFlow Saved Model)   
blue-doragon.png : sample image 1  
red-doragon.png  : sample image 2  
<kbd>![br-2](https://user-images.githubusercontent.com/7918390/188066217-4ef18d84-fc94-4c46-b815-b4eec7c9088c.png)</kbd>  

## Execution example
c:\apps\ai>**python tfcolor2.py blue-doragon.png red-doragon.png**  
<kbd><pre>{'labels': <tf.Tensor 'Tile:0' shape=(None, 14) dtype=string>, 
'scores': <tf.Tensor 'scores:0' shape=(None, 14) dtype=float32>, 
'key': <tf.Tensor 'Identity:0' shape=(None,) dtype=string>} 
{'labels': <tf.Tensor: shape=(2, 14), dtype=string, numpy= 
array([[b'orange', b'yellow', b'purplish_red', b'green', b'gray', 
b'yellow_green', b'purple', b'pink', b'red', b'black', b'white', 
b'blue_green', b'blue', b'brown'], 
[b'orange', b'yellow', b'purplish_red', b'green', b'gray', 
b'yellow_green', b'purple', b'pink', b'red', b'black', b'white', 
b'blue_green', b'blue', b'brown']], dtype=object)>, 
'scores': <tf.Tensor: shape=(2, 14), dtype=float32, numpy= 
array([[0.05143434, 0.0465448 , 0.3964859 , 0.0465448 , 0.05680693,  
0.04539329, 0.07087733, 0.05016822, 0.04893166, 0.05823032, 
0.04003182, 0.5781289 , 0.7745404 , 0.2492084 ], 
[0.03903484, 0.04772406, 0.67595094, 0.0924189 , 0.04539329, 
0.05968711, 0.39022017, 0.10650936, 0.07087733, 0.05405774,
0.04539329, 0.08602025, 0.230078 , 0.60351413]], dtype=float32)>, 
'key': <tf.Tensor: shape=(), dtype=string, numpy=b'uniq_dummy_id_123'>} 
</pre></kbd>  

Top 3 image color result.  
**blue-doragon.png**  
1: 0.774540 : blue  
2: 0.578129 : blue_green  
3: 0.396486 : purplish_red  

**red-doragon.png**  
1: 0.675951 : purplish_red  
2: 0.603514 : brown  
3: 0.390220 : purple  

## Author  
PicoLix Design / Naeba [Twitter nae2sho](https://twitter.com/nae2sho)















