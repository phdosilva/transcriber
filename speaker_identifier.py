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
        self.file_uploaded = None
        self.file_size = None
        self.pipeline: Callable = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1",
                                                           use_auth_token=os.environ.get("HUGGINGFACE_TOKEN"))
        self.state: State = State.FREE

    def start_diarization(self):
        self.state = State.RUNNING_FILE
        DEMO_FILE = {"uri": "blabal", "audio": "audio.wav"}
        diarization = self.pipeline(DEMO_FILE)

        with open("diarization.txt", "w") as text_file:
            text_file.write(str(diarization))

    def get_state(self):
        return self.state

    def set_free(self):
        self.state = State.FREE

    def set_uploading_file(self):
        self.state = State.UPLOADING_FILE

    def set_running_file(self):
        self.state = State.RUNNING_FILE

    def set_finished(self):
        self.state = State.FINISHED
        
    def save_file(self, num: int):
        self.file_size: int = num
        self.file_uploaded: int = 0
        
