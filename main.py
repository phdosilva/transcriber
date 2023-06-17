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

interview: Interview = Interview()


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """User access to interface"""
    return templates.TemplateResponse("upload_file.html", {"request": request})


@app.post("/upload")
async def upload_media_file(file: UploadFile = File(...)):
    """Upload the interview file to start"""
    try:
        async with aiofiles.open(f"./handled_files/{file.filename}", "wb") as f:
            while chunk := await file.read(CHUNK_SIZE):
                await f.write(chunk)
    except Exception as error:
        return {"message": "There was an error uploading the file",
                "error": {"type": type(error).__name__, "args": error.args}}
    finally:
        file.file.close()

    # Needs no signalise to conductor that the upload has been succeeded
    return {"message": f"Successfully uploaded {file.filename}", "file": {"name": file.filename, "size": file.size}}


@app.get("/health")
async def get_service_health():
    """Return service health"""
    return {"OK"}
