from roboflow import Roboflow
from ultralytics import YOLO

rf = Roboflow(api_key="n6mEsjSQxh51ABYyaE6P")
project = rf.workspace("graduation-project-9vf0s").project("currency-detection-6rhgh")
dataset = project.version(1).download("yolov8")