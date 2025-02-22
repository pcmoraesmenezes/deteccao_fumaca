from app.external.carregamento_modelo import carregar_modelo
from app.utils.processador_de_imagem import process_image
import numpy as np
import cv2

class DetectorDeFumaca:
    def __init__(self):
        self.model = carregar_modelo()

    def detect_smoke(self, file_bytes: bytes) -> bytes:

        pil_image = process_image(file_bytes)
        image_cv = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
        results = self.model(image_cv)
        annotated_image = results[0].plot()
        ret, buffer = cv2.imencode('.jpg', annotated_image)
        if not ret:
            raise ValueError("Erro ao codificar a imagem")
        return buffer.tobytes()
