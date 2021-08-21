from fastapi import APIRouter, File, UploadFile
from starlette.requests import Request
from typing import Dict
import uuid

from core.facialExpression import FacialExpression

router = APIRouter()

@router.post("/gateway")
async def post_gatewat(
    request: Request,
    file: UploadFile = File(...),
) -> Dict:
    # Generación del fichero temporal
    fileName = "/tmp/{key}.{format}".format(
        key = str(uuid.uuid4()),
        format = file.content_type.replace(
            "image/", ""
        )
    )
    with open(fileName, mode = "wb") as fileOut:
        fileOut.write(file.file.read())
    file.file.close()

    facialExpression: FacialExpression = request.app.state.FE
    return facialExpression.compute(fileName)