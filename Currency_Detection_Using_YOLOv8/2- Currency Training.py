from ultralytics import YOLO

model = YOLO('yolov8n.yaml')
model.train(data='C:/Users/maham/Desktop/GraduationProject/Currency-Detection-1/data.yaml', epochs=25)
model.val()