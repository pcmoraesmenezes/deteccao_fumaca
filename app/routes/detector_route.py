from fastapi import APIRouter, File, UploadFile, HTTPException, Header, Depends
from fastapi.responses import Response
from app.services.detector_de_fumaca import DetectorDeFumaca

router = APIRouter()
detector_service = DetectorDeFumaca()

API_KEY = "SOU_UM_GRAU_E_MEIO!"
async def verify_api_key(x_api_key: str = Header(...)):

    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Chave API inválida. Acesso negado.")
        
@router.post("/api/detector_de_fumaca", dependencies=[Depends(verify_api_key)])
async def detector_de_fumaca(file: UploadFile = File(...)):

    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(
            status_code=400,
            detail="Formato de imagem não suportado. Utilize JPEG ou PNG."
        )
    
    try:
        contents = await file.read()
        annotated_image_bytes = detector_service.detect_smoke(contents)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return Response(content=annotated_image_bytes, media_type="image/jpeg")
