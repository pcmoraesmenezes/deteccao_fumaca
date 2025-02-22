from ultralytics import YOLO
from app.settings.gerenciador_caminho import GerenciadorCaminho

def carregar_modelo() -> YOLO:
    caminho_modelo = GerenciadorCaminho.MODEL_PATH
    return YOLO(caminho_modelo)