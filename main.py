from fastapi import FastAPI, Request, UploadFile, BackgroundTasks
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from speaker_identifier import Interview

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

interview = Interview()


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """User access to interface"""
    return templates.TemplateResponse("upload_file.html", {"request": request})


@app.post("/uploadfile/")
async def upload_media_file(file: UploadFile, background: BackgroundTasks):
    background.add_task(interview.start_diarization)
    try:
        contents = file.file.read()
        with open(f"handled_files/audio.wav", "wb") as f:
            f.write(contents)
    except Exception as error:
        return {"message": "There was an error uploading the file", "error": {"type": type(error).__name__, "args": error.args}}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}


@app.get("/health")
async def get_service_health():
    """Return service health"""
    return {"OK"}


@app.get("/diarization")
async def get_actual_diarization():
    """Get the result from last audio speaker-diarization"""
    try:
        file = open("handled_files/diarization.txt", "r")
        content = file.read()
        file.close()
        return {"diarization": content}
    except:
        return {"There is no audio diarization file"}
