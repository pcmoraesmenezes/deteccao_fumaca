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
