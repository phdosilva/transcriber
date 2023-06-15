import openai
import os

def get_transcription():
    return openai.Audio.transcribe(
            api_key= os.environ.get("WHISPER_TOKEN"),
            model="whisper-1",
            file=media_file,
            response_format="srt"
        )

