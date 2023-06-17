from fastapi import FastAPI, Request, UploadFile, BackgroundTasks, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import aiofiles

from speaker_identifier import Interview

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

CHUNK_SIZE = 1024

conductor: Interview = Interview()


@app.get("/")
async def root():
    """Will be used to show a User Interface"""
    return {}

@app.post("/upload")
async def upload_media_file(file: UploadFile = File(...)):
    """Upload the interview file to start"""
    try:
        async with aiofiles.open(f"./handled_files/{file.filename}", "wb") as f:
            while chunk := await file.read(CHUNK_SIZE):
                await f.write(chunk)

            await conductor.diarization(file.filename)
    except Exception as error:
        return {"message": "There was an error uploading the file",
                "error": {"type": type(error).__name__, "args": error.args}}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}", "file": {"name": file.filename, "size": f"{file.size} bytes"}}

@app.get("/diarization")
def get_diarization():
    """Access Diarization File"""
    try:
        with open("./handled_files/diarization.txt", "rb") as file:
            content: bytes = file.read()
            return {"diarization": str(content)}
    except Exception as error:
        return {"message": "There was an erros with getting diartization.txt file",
                "error": {"type": type(error).__name__, "args": error.args}}
