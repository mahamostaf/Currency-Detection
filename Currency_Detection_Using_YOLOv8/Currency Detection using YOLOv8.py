from ultralytics import YOLO

text = ""
model = YOLO("best.pt")
results = model('https://i.etsystatic.com/20961880/r/il/4b6efe/3870219052/il_fullxfull.3870219052_azd0.jpg')
print(results)
print(results.boxes.cls)
for label in results.boxes.cls:
    print(label)
    if model.names[int(label)] == 1:
        text = text + model.names[int(label)] + " pound, "
    else:
        text = text + model.names[int(label)] + " pounds, "
print(text)