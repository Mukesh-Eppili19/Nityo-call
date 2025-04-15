from fastapi import FastAPI, File, UploadFile , Request
import shutil
from pathlib import Path
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.services.transcription import transcribe_audio
from src.services.diarization import diarize_audio
from src.services.sentiment_analysis import analyze_sentiment
from src.utils.audio_processing import convert_to_wav


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Define the static folder path
STATIC_FOLDER = Path("static")
#STATIC_FOLDER.mkdir(exist_ok=True)

templates = Jinja2Templates(directory="templates")

@app.post("/upload-audio/")
async def upload_audio(request: Request,file: UploadFile = File(...)):
    file_path = STATIC_FOLDER / file.filename
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Perform diarization and transcription
    try:
        wav_path = convert_to_wav(file_path)
        print(f"Converted {file_path} to {wav_path}")
        diarization_result = diarize_audio(wav_path)
        print("Diarization completed")
        print(f"Diarization result: {diarization_result}")
        transcription_result = transcribe_audio(wav_path)
        print("Transcription completed")
        print(f"Transcription result: {transcription_result}")
        sentiment , sentence_scores = analyze_sentiment(transcription_result)
        print("Sentiment analysis completed")
        print(f"Sentiment result: {sentiment}")
        print(f"Sentence scores: {sentence_scores}")
        
        return templates.TemplateResponse("pages/dashboard.html", {
            "request": request,
            # "filename": file.filename,
            "diarization": diarization_result,
            "transcription": transcription_result,
            "sentiment": sentiment,
            "sentence_scores": sentence_scores,

        })
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("pages/dashboard.html", {"request": request})


@app.get("/", response_class=HTMLResponse)
async def main():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Upload Audio</title>
    </head>
    <body>
        <h1>Upload an Audio File</h1>
        <form action="/upload-audio/" method="post" enctype="multipart/form-data">
            <input type="file" name="file" accept="audio/*" required>
            <button type="submit">Upload</button>
        </form>
    </body>
    </html>
    """
    return html_content