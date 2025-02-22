from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import Response
from app.services.detector_de_fumaca import DetectorDeFumaca

router = APIRouter()
detector_service = DetectorDeFumaca()

@router.post("/api/detector_de_fumaca")
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
