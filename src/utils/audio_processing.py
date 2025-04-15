from pydub import AudioSegment
import os

def load_audio(file_path: str) -> AudioSegment:
    """Load an audio file and return it as an AudioSegment."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    audio = AudioSegment.from_file(file_path)
    return audio

def convert_audio_format(audio: AudioSegment, target_format: str) -> AudioSegment:
    """Convert the audio to the specified format."""
    if target_format not in ['wav', 'mp3', 'flac']:
        raise ValueError("Unsupported target format. Choose from 'wav', 'mp3', or 'flac'.")
    
    # Export the audio to the desired format
    temp_file = f"temp_audio.{target_format}"
    audio.export(temp_file, format=target_format)
    
    # Load the converted audio
    converted_audio = AudioSegment.from_file(temp_file)
    
    # Clean up the temporary file
    os.remove(temp_file)
    
    return converted_audio

def convert_to_wav(file_path: str) -> str:
    """Convert an audio file to WAV format and return the new file path."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    audio = AudioSegment.from_file(file_path)
    wav_path = os.path.splitext(file_path)[0] + ".wav"
    audio.export(wav_path, format="wav")
    return wav_path

def preprocess_audio(audio: AudioSegment) -> AudioSegment:
    """Preprocess the audio for transcription or diarization."""
    # Example preprocessing: normalize audio
    normalized_audio = audio.normalize()
    return normalized_audio