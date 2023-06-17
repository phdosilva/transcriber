from pyannote.audio import Pipeline
from typing import Callable
import os
from enum import Enum


class State(Enum):
    FREE = 0
    UPLOADING_FILE = 1
    RUNNING_FILE = 2
    FINISHED = 3


class Interview:
    def __init__(self):
        self.filename: str
        self.pipeline: Callable = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1",
                                                           use_auth_token=os.environ.get("HUGGINGFACE_TOKEN"))

    def diarization(self):
        filename = self.filename
        DEMO_FILE = {"uri": "blabal", "audio": f"/handled_files/{filename}"}
        diarization = self.pipeline(DEMO_FILE)

        with open(f"./handled_files/{filename}-diarization.txt", "w") as text_file:
            text_file.write(str(diarization))


        
