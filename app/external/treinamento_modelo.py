"""
    Esse script é responsável pelo treinamento do modelo de classificador de fumaça ou incêndio.

    Observação:
    -   O treinamento foi feito utilizando o google colab devido a necessidade de uma GPU para treinamento.
    -   O modelo treinado foi salvo no google drive.

    Para acessar o colab com o treinamento do modelo, acesse o link: https://colab.research.google.com/drive/11wyOBE2OPTQOy-YViluhjtV-rNaXFUTG?usp=sharing
"""


from ultralytics import YOLO

save_path = "/content/drive/MyDrive/case/model"


model = YOLO("yolov8n.pt")  
model.train(
    data="data.yaml",  
    epochs=10,
    imgsz=640,
    project=save_path,  
    name="yolo_fire_smoke"  )

print(f"✅ Modelo salvo em: {save_path}/yolo_fire_smoke/weights/best.pt")
