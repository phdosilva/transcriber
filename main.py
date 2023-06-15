from fastapi import FastAPI, Request, UploadFile, File, BackgroundTasks
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from speaker_identifier import Interview

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

interview = Interview()

# def save_file(file: UploadFile):
#     with open(f"handled_files/audio.wav", "wb") as temp_file:
#         content = file.read()
#         temp_file.write(content)
#     return speaker_identifier.start_diarization()


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """User access to interface"""
    return templates.TemplateResponse("upload_file.html", {"request": request})


@app.post("/uploadfile/", response_model=dict[str, str])
async def upload_media_file(file: UploadFile, background: BackgroundTasks):
    background.add_task(interview.start_diarization)
    try:
        contents = file.file.read()
        with open(f"handled_files/audio.wav", 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}


@app.get("/health", response_model=str)
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
