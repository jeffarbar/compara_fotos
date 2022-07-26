import io

from fastapi import FastAPI, File
from starlette.responses import StreamingResponse

import comparacao

app = FastAPI()


@app.post('/compara')
async def compara(foto_1: bytes = File(...),
                  foto_2: bytes = File(...)) -> str:

    img_1 = io.BytesIO(foto_1)
    img_1.seek(0)

    img_2 = io.BytesIO(foto_2)
    img_2.seek(0)

    result = comparacao.compare(img_1, img_2)

    if result:
        return {"result": "Deu match"}
    else:
        return {"result": "Não deu match"}
