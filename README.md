# AI Text-to-Speech System with Emotion Control

An AI-powered Text-to-Speech application that converts text into natural-sounding speech with dynamic emotion simulation.  
The system supports multilingual speech generation and allows users to control tone, speed, pauses, and speech flow through an interactive interface.

---

## 🚀 Features

- 🔊 **Text-to-Speech Generation**
  - Convert text into speech in real-time.

- 🌍 **Multilingual Support**
  - Supports English and Hindi speech generation.

- 🎭 **Emotion Tone Simulation**
  - Default
  - Calm
  - Storytelling
  - Aggressive Motivation
  - Friendly
  - Professional
  - Excited
  - Emotional
  - News Anchor

- 🎚 **Speech Customization Controls**
  - Speed Control
  - Chunk Size Control
  - Pause / Gap Control
  - Seed-based variation

- 🎨 **Interactive UI**
  - Built using Gradio for real-time interaction.

- 🎧 **Audio Processing**
  - Dynamic speech speed adjustment
  - Pause insertion
  - Chunk-based audio synthesis

---

## 🏗 System Architecture
User Input
↓
Emotion Modulation Layer
↓
Text Chunking Algorithm
↓
Text-to-Speech Engine (gTTS)
↓
Audio Processing (pydub)
↓
Speed Adjustment & Pause Control
↓
Final Audio Output


---

## 🛠 Technologies Used

- **Python**
- **Gradio** – Interactive UI framework
- **gTTS (Google Text-to-Speech)** – Speech synthesis engine
- **pydub** – Audio manipulation
- **FFmpeg** – Audio processing support

---

## 📦 Installation

Clone the repository:

git clone https://github.com/yourusername/ai-text-to-speech-system.git
cd ai-text-to-speech-system

pip install -r requirements.txt

sudo apt install ffmpeg

python app.py

http://127.0.0.1:7860


🎛 Usage

Enter the text you want to convert to speech.

Select the language (English / Hindi).

Choose the emotion tone.

Adjust speed, chunk size, and pause settings.

Click Generate Audio.

Listen to the generated speech.


📊 Project Highlights

Emotion-aware speech synthesis simulation

Modular backend architecture

Real-time audio processing

Customizable speech generation pipeline


👨‍💻 Author

Developed as an AI/ML project demonstrating speech synthesis, emotion modulation, and real-time audio processing using Python.
