#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from keras.applications import ResNet50
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
import tensorflow as tf
from PIL import Image
import numpy as np
import io
from timeit import default_timer as timer

route_path_general = Blueprint("route_path_general", __name__)

@route_path_general.route('/imagenation', methods=['POST'])
def predict():
	data = []
	if request.method == "POST":
		if request.files.get("image"):
			image = request.files["image"].read()
			image = Image.open(io.BytesIO(image))
			image = prepare_image(image, target=(224, 224))
			with graph.as_default():
				preds = model.predict(image)
				results = imagenet_utils.decode_predictions(preds)
				
			for (imagenetID, label, prob) in results[0]:
				r = {"label": label, "probability": float(prob)}
				data.append(r)
	print("Predictions:")
	print(data)
	return response_with(resp.SUCCESS_200, value=data)   

@route_path_general.route('/hello', methods=['GET'])
def test_api():
	return response_with(resp.SUCCESS_200, value={'data': 'oi'})   

def load_model():
	global model
	model = ResNet50(weights="imagenet")
	global graph 
	graph = tf.get_default_graph()

def prepare_image(image, target):
	if image.mode != "RGB":
		image = image.convert("RGB")

	image = image.resize(target)
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)
	image = imagenet_utils.preprocess_input(image)

	return image
