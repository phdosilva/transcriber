import openai
import os

with open("audio.mp3", "rb") as media_file:
    transcript = openai.Audio.transcribe(
        api_key= os.environ.get("WHISPER_TOKEN"),
        model="whisper-1",
        file=media_file,
        response_format="srt"
    )

    print(transcript)

    with open("transcription.txt", "w") as transcription_file:
        transcription_file.write(str(transcript))
