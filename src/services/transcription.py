from fastapi import UploadFile
import whisper
import os
import shutil

def transcribe_audio(file: UploadFile):
    # Load the Whisper model
    model = whisper.load_model("base")  # You can choose a different model size if needed

    # Save the uploaded file temporarily
    """temp_file_path = f"temp_{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)"""

    # Transcribe the audio file
    result = model.transcribe(file)

    # Clean up the temporary file
    #os.remove(temp_file_path)

    return result['text']