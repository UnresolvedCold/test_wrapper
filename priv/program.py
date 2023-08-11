from pypmml import Model
import pandas as pd
import random
import json
import downloader
import os
from dotenv import load_dotenv

model = None

def init(model_name, model_version):
  print("init invoked")
  global model
  load_dotenv()
  model_name = model_name.decode('utf8')
  model_version = model_version.decode('utf8')
  minio_url = os.environ.get("MINIO_URL")
  print("minio_url: " + minio_url)
  print("model_name: " + model_name)
  model_url = minio_url +"?modelName="+ model_name + "&modelVersion=" + model_version
  idc_file = downloader.download_file(model_url)
  model = Model.fromFile(idc_file)
  downloader.delete_file(idc_file)
  return model != None

def get_required_features():
  global model
  return model.inputNames

def evaluate(features):
  global model
  deserialized_features = json.loads(features)
  return model.predict(deserialized_features)['predicted_y']

# init("storable_to_pps_queue_model", "1.0.0")
# print(get_required_features())