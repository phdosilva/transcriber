from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from speaker_identifier import Diarization


app = FastAPI()
diarization = Diarization()


@app.get("/")
async def root():
    """Will be used to show a User Interface"""
    return {"message": "Go to /docs to test the API"}

@app.post("/upload")
async def upload_media_file(background: BackgroundTasks, file: UploadFile = File(...)):
    """Upload the interview file to start"""
    try:
        with open(f"./handled_files/{file.filename}", "wb") as f:
            content: bytes = await file.read()
            f.write(content)
        background.add_task(diarization.start, file.filename)
        print("File has been downloaded!")
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
