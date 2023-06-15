from pyannote.audio import Pipeline
from typing import Callable
import os


class Interview:

    def __init__(self):
        self.pipeline: Callable = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1",
                                                            use_auth_token=os.environ.get("HUGGINGFACE_TOKEN"))

    def start_diarization(self):
        DEMO_FILE = {"uri": "blabal", "audio": "audio.wav"}
        diarization = self.pipeline(DEMO_FILE)

        with open("diarization.txt", "w") as text_file:
            text_file.write(str(diarization))
