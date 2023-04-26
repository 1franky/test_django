from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from app.routers import faceRoute #, voz, twilioRoute, contexPath

app = FastAPI(title="Test FACE ID" )

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(faceRoute.router)
# app.include_router(twilioRoute.router)
#app.include_router(voz.router)


@app.get("/", tags=["Home"])
def read_root():
    return {
        "Hola": " ® :) "
    }


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Test FACE ID",
        version="1.0.1",
        description="<h2>Servicios de reconocimiento facial y otros generales.</h2>",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://metafinanciera.com.mx/wp-content/uploads/2021/03/logo-meta-color.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi