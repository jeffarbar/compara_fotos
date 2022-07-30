import io

from fastapi import FastAPI, File
from fastapi.middleware.cors import CORSMiddleware
from response import Response
import comparacao
import salva_imagem as si 


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/compara')
async def compara(foto_1: bytes = File(...),
                  foto_2: bytes = File(...)) -> str:

    try:
        img_1 = io.BytesIO(foto_1)
        img_1.seek(0)

        img_2 = io.BytesIO(foto_2)
        img_2.seek(0)

        result = comparacao.compare(img_1, img_2)

        diretorio_uuid = si.salva(img_1, img_2, result)

        if result:
            res = Response(0, "Deu Match",diretorio_uuid)
        else:
            res = Response(0, "Não Deu Match", diretorio_uuid)

        return res

    except Exception as ex:
        return Response(1, ex)



@app.post('/avaliacao')
async def avaliacao(uuid: str,
                  avaliacao: bool ) -> str:

    si.salva_avaliacao(uuid,avaliacao)

    return "OK"