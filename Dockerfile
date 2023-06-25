FROM python:3.9

#
WORKDIR /code
WORKDIR /handled_files

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
pip install -qq https://github.com/pyannote/pyannote-audio/archive/refs/heads/develop.zip


#
ENV WHISPER_TOKEN=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
ENV HUGGINGFACE_TOKEN=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

#
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
