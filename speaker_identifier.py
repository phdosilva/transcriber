from pyannote.audio import Pipeline
from typing import Callable
import os

class Interview:
    def __init__(self):
        self.pipeline: Callable = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1",
                                                           use_auth_token=os.environ.get("HUGGINGFACE_TOKEN"))

    def diarization(self, filename) -> None:
        try:
            DEMO_FILE = {"uri": "blabal", "audio": f"./handled_files/{filename}"}
            diarization = self.pipeline(DEMO_FILE)

            with open(f"./handled_files/diarization.txt", "wb") as text_file:
                text_file.write(diarization)
        except Exception as error:
            raise Exception("There is an error with diarization", error.args)

        
