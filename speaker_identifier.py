from pyannote.audio import Pipeline
from typing import Callable
import os

class Diarization:
    def __init__(self):
        print("Initializing pipeline")
        self.pipeline: Callable = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1",
                                                           use_auth_token=os.environ.get("HUGGINGFACE_TOKEN"))

    async def start(self, filename) -> None:
        print(f"Starting diarization at {filename}")
        try:
            DEMO_FILE = {"uri": "blabal", "audio": f"./handled_files/{filename}"}
            diarization = self.pipeline(DEMO_FILE)

            with open(f"./handled_files/diarization.txt", "wb") as text_file:
                text_file.write(diarization)
            print("Success with diarization")
        except Exception as error:
            print("Something went wrong")
            raise Exception("There is an error with diarization", error.args)
        finally:
            print("Diarization ended")