from fastapi import APIRouter, status
from fastapi_restful.cbv import cbv
from starlette.responses import JSONResponse

system_router = APIRouter()


@cbv(system_router)
class SystemRouter:
    @system_router.get("/", include_in_schema=False)
    async def root(self) -> dict[str, str]:
        return {"message": "MusicBox API"}

    @system_router.get("/health", include_in_schema=False)
    async def health(self) -> JSONResponse:
        data = {"music-box-api": status.HTTP_200_OK}
        return JSONResponse(data, status_code=status.HTTP_200_OK)
