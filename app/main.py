from fastapi import FastAPI
from app.routes.detector_route import router as detector_router
import uvicorn


app = FastAPI(title="Detector de Fumaça API", version="1.0")

app.include_router(detector_router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=4000, reload=True)
