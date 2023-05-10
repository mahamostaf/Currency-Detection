from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials


key = "078e943cda2145bf9866e5fe8668faa6"
endpoint = "https://other-apis.cognitiveservices.azure.com/"
text = ""
computerVision = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))
image = "https://people.com/thmb/KHj3b47xBQiKkCGaIZNG57cBtSs=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc():focal(314x329:316x331)/william-catherine-wales-092722-2-b8bcb651e77840e88142d1c4679ecff7.jpg"
response = computerVision.analyze_image(image, visual_features=['Faces','color'])
print(response)

for face in response.faces:
    print(face)




