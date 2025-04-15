# Project Title: Audio Transcription and Diarization Service

## Overview
This project is a FastAPI application that allows users to upload audio files for transcription and speaker diarization. The application utilizes the Whisper model for transcription and includes functionality to identify and separate different speakers in the audio.

## Project Structure
```
project
├── main.py                     # Entry point of the FastAPI application
├── src
│   ├── services
│   │   ├── diarization.py      # Functions for speaker diarization
│   │   └── transcription.py     # Functions for audio transcription using Whisper
│   └── utils
│       └── audio_processing.py  # Utility functions for audio processing
├── static                      # Directory for storing uploaded audio files
├── requirements.txt            # List of project dependencies
└── README.md                   # Documentation for the project
```

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd project
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Start the FastAPI application:
   ```
   uvicorn main:app --reload
   ```

2. Open your web browser and navigate to `http://127.0.0.1:8000/` to access the upload form.

3. Upload an audio file (supported formats: audio/*) and submit the form.

4. The application will process the audio file and return the transcription and diarization results.

## Dependencies
The project requires the following Python packages:
- FastAPI
- Whisper
- Additional libraries for audio processing and diarization (to be specified in `requirements.txt`)

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.