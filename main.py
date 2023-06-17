from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import aiofiles

app = FastAPI()

CHUNK_SIZE = 1024

@app.get("/")
async def root():
    """Will be used to show a User Interface"""
    return {"message": "Go to /docs to test the API"}

@app.post("/upload")
async def upload_media_file(file: UploadFile = File(...)):
    """Upload the interview file to start"""
    try:
        with open(f"./handled_files/{file.filename}", "wb") as f:
            content: bytes = file.read()
            f.write(content)
        print("File has been downloaded!")
    except Exception as error:
        return {"message": "There was an error uploading the file",
                "error": {"type": type(error).__name__, "args": error.args}}
    finally:
        file.file.close()

    print("Responding the request")
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
