from pyannote.audio import Pipeline
import os

pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1",
                                    use_auth_token=os.environ.get("HUGGINGFACE_TOKEN"))


class Enterview:

    def __init__(self):
        # self.file
        # self.transcription
        # self.diarization

        pass

