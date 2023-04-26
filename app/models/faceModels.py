from pydantic import BaseModel
from fastapi import File, UploadFile

class comparaRostroBase(BaseModel):
    foto1: str
    foto2: str


class selfie(BaseModel):
    selfie:  str


class faceResponse(BaseModel):
    r : bool
    message : str
    time: str

class findFaceResponse(BaseModel):
    r : bool
    message : str
    numRostros : int 
    time : str

class numpyFaces(BaseModel):
    numRostros: int
    arrays: list
    time: str

class comparaNumpy(BaseModel):
    id: str
    selfie: UploadFile = File(...)