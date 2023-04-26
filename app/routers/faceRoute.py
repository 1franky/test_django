from fastapi import APIRouter
from fastapi import File, UploadFile
from fastapi import HTTPException

import app.controllers.face.faceValidator as validador
import app.models.faceModels as faceModels
# from app.routers.contexPath import context
from app.utils import utils
from datetime import datetime

context = ""
router = APIRouter(
    prefix=f"{context}/face",
    tags=["Face Recognitions"]
)



# @router.post("/recognition/base64", response_model=faceModels.faceResponse)
# def compara_rostro_base64(item: faceModels.comparaRostroBase):
#     """
#     Servicio para comparar foto de 2 rostros desde imagenes base 64
#     """
#     return validador.comparaFromBase64(utils.from_base64_to_numpy(item.foto1), utils.from_base64_to_numpy(item.foto2))


# @router.post("/recognition", response_model=faceModels.faceResponse)
# def compara_rostro(
#     foto1: UploadFile = File(...),
#     foto2: UploadFile = File(...)
# ):
#     """
#     Servicio para comparar foto de 2 rostros desde imagenes
#     """

#     return validador.comparaFromBase64(utils.from_file_to_numpy(foto1.file.read()), utils.from_file_to_numpy(foto2.file.read()))



# @router.post("/findRostroBase64", response_model=faceModels.findFaceResponse)
# def find_rostro_base64(item: faceModels.selfie):
#     """
#     Servicio para validar el rostro de en una imagen base 64
#     """
#     return validador.validaRostro(utils.read_image_from_base64(item.selfie))


# @router.post("/findRostro", response_model=faceModels.findFaceResponse)
# def find_rostro(
#     foto: UploadFile = File(...)
# ):
#     """
#     Servicio para validar el rostro de en una imagen
#     """

#     return validador.validaRostro1(utils.from_file_to_numpy(foto.file.read()))


@router.post("/getFaces", response_model=faceModels.numpyFaces)
async def get_faces_numpy(
        ine: UploadFile = File(...)
):
    """
    Servicio para obtener un arreglo de numpy con caras de la ine
    """
    print(f"{datetime.now()} \t {ine.filename}")
    try:
        img = utils.from_file_to_numpy(ine.file.read())
    except Exception as e:
        print(f"Error al leer imagen {e}")
        raise HTTPException(status_code=500, detail="Erro al leer imagen")

    return validador.getNumpy(img)



@router.post("/getFaces2", response_model=faceModels.numpyFaces)
async def get_faces_numpy2(
        ine: UploadFile = File(...)
):
    """
    Servicio para obtener un arreglo de numpy con caras de la ine usando P. concurrente
    """
    print(f"{datetime.now()} \t {ine.filename}")
    try:
        img = utils.from_file_to_numpy(ine.file.read())
    except Exception as e:
        print(f"Error al leer imagen {e}")
        raise HTTPException(status_code=500, detail="Erro al leer imagen")

    return validador.getNumpy2(img)



# @router.post("/comparaNumpy", response_model=faceModels.faceResponse )
# async def compara_with_numpy(
#         id: str,
#         selfie: UploadFile = File(...)
# ):
#     """
#     Servicio para ir a redis y comparar vs una selfie
#     """
#     return validador.validaRedis(id, utils.from_file_to_numpy(selfie.file.read()))