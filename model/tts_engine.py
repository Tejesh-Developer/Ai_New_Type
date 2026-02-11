import torch
from TTS.api import TTS
import tempfile
import random
from pydub import AudioSegment
import os

from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

# ===============================
# LOAD MODEL (ONCE)
# ===============================
tts_model = TTS(
    "tts_models/multilingual/multi-dataset/your_tts",
    gpu=torch.cuda.is_available()
)

# ===============================
# UTILS
# ===============================
def split_text(text, chunk_size):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def apply_speed(text, size, seed):
    random.seed(seed if seed != -1 else None)
    words = text.split()
    new_words = []

    for w in words:
        new_words.append(w)
        if size < 1:
            new_words.append("...")   # slow effect
        elif size > 1 and random.random() < 0.2:
            continue                 # fast effect

    return " ".join(new_words)

# ===============================
# MAIN FUNCTION
# ===============================
def generate_audio(
    ref_audio,
    ref_text,
    target_text,
    language,
    size,
    chunk_size,
    chunk_gap,
    seed,
    tone
):
    # Mandatory checks
    if ref_audio is None:
        return None, "❌ Reference audio required"

    if target_text.strip() == "":
        return None, "❌ Target text required"

    lang = language.lower()
    seed = int(seed)
    
    # ===============================
    # EMOTION TONE ADJUSTMENTS
    # ===============================
    if tone == "Calm":
         size = 0.85
         chunk_gap += 0.3

    elif tone == "Storytelling":
        size = 0.95
        chunk_gap += 0.2
        target_text = target_text.replace(".", "... ")

    elif tone == "Aggressive Motivation":
        size = 1.25
        chunk_gap = max(0, chunk_gap - 0.2)
        target_text = target_text.upper()
        
    elif tone == "Friendly":
        size = 1.05
        chunk_gap += 0.1
        target_text = target_text + " 😊"

    elif tone == "Professional":
        size = 1.0
        chunk_gap = 0.2

    elif tone == "Emotional":
        size = 0.9
        chunk_gap += 0.4
        target_text = target_text.replace(".", "... ")
        
    elif tone == "Default":
        pass  # 👈 Important


    chunks = split_text(target_text, int(chunk_size))
    final_audio = AudioSegment.silent(duration=0)

    try:
        for idx, chunk in enumerate(chunks):

            # Speed + seed effect
            processed_text = apply_speed(
                chunk,
                size,
                seed + idx if seed != -1 else -1
            )

            # ===============================
            # LANGUAGE HANDLING (FINAL)
            # ===============================
            if lang in ["english", "auto"]:
                final_text = processed_text

            elif lang == "hindi":
                # Hindi (Devanagari) → phonetic English
                final_text = transliterate(
                    processed_text,
                    sanscript.DEVANAGARI,
                    sanscript.ITRANS
                )

            else:
                return None, "❌ Unsupported language"

            # Temp output per chunk
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as fp:
                out_path = fp.name

            # Always use English engine (stable)
            tts_model.tts_to_file(
                text=final_text,
                file_path=out_path,
                speaker_wav=ref_audio,
                language="en"
            )

            audio = AudioSegment.from_wav(out_path)
            final_audio += audio

            # Chunk gap
            if idx < len(chunks) - 1:
                final_audio += AudioSegment.silent(
                    duration=int(chunk_gap * 1000)
                )

            os.remove(out_path)

        # Export final audio
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as final_fp:
            final_path = final_fp.name
            final_audio.export(final_path, format="wav")

        return final_path, "✅ English + Hindi generated successfully"

    except Exception as e:
        return None, f"❌ Error: {str(e)}"
