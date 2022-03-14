import requests
import json
import numpy as np
import cv2
import tensorflow as tf
import time

image = cv2.imread("dvd.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = cv2.resize(image, (224,224))
image = np.expand_dims(image, axis=0)
# to set the batch size


url = "https://resnetapps.herokuapp.com/v1/models/resnet50:predict"
# url = "http://localhost:8501/v1/models/resnet50:predict"
# url = "http://localhost:8501/v1/models/vgg16:predict"

data = json.dumps({
	"signature_name":"serving_default",
	"instances":image.tolist()
	})

headers = {"content-type":"application/json"}

while True:
	start_time = time.time()
	response = requests.post(url, data=data, headers=headers)
	print(response)
	prediction = json.loads(response.text)["predictions"]
	# print(prediction)
	result = tf.keras.applications.imagenet_utils.decode_predictions(np.array(prediction))
	print(result)
	print("Time Taken: ",time.time()-start_time)

"""
2022-03-14 19:29:54.506593: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory; LD_LIBRARY_PATH: /home/vinay/miniconda3/envs/tf2/lib/python3.7/site-packages/cv2/../../lib64:
2022-03-14 19:29:54.506629: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
^[[A[[('n02979186', 'cassette_player', 0.707468629), ('n03424325', 'gasmask', 0.106079057), ('n02988304', 'CD_player', 0.0875394791), ('n04392985', 'tape_player', 0.0850655735), ('n04265275', 'space_heater', 0.00455882633)]]
Time Taken:  0.40688347816467285
"""