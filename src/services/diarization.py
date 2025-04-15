

from typing import List, Tuple
import numpy as np
import librosa
import torch
from pyAudioAnalysis import audioSegmentation as aS
from src.utils.audio_processing import convert_to_wav
from pyannote.audio import Pipeline




def diarize_audio(audio_path: str) -> List[str]:
    
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization")
    diarization = pipeline(audio_path)
    
    speaker_labels = []
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        speaker_labels.append(f"{turn.start:.1f}-{turn.end:.1f}: {speaker}")
    
    return speaker_labels
def load_audio_file(file_path: str):
    audio, sr = librosa.load(file_path, sr=None)
    return audio, sr

def save_diarization_results(results: List[str], output_path: str):
    with open(output_path, 'w') as f:
        for speaker in results:
            f.write(f"{speaker}\n")