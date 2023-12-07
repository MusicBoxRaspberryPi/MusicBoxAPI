from fastapi import APIRouter, status
from starlette.responses import JSONResponse

system_router = APIRouter()


@system_router.get("/", include_in_schema=False)
async def root() -> dict[str, str]:
    return {"message": "MusicBox API"}


@system_router.get("/health", include_in_schema=False)
async def health() -> JSONResponse:
    data = {"music-box-api": status.HTTP_200_OK}
    return JSONResponse(data, status_code=status.HTTP_200_OK)
