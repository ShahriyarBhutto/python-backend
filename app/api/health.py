from fastapi import APIRouter


router = APIRouter()


@router.get("/health")
async def health_route():
    return {"status":"OK"}
