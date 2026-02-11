import gradio as gr
import os
from model.tts_engine import generate_audio


with open("assets/style.css") as f:
    css = f.read()

with gr.Blocks(css=css, theme=gr.themes.Soft()) as demo:
    gr.HTML("""
        <div class="top-header">
        <h1>🎤 Qwen3-TTS</h1>
        <p>🔊 High-Quality Text-to-Speech with Voice Cloning</p>
        <div class="tab-title">🧬 Voice Clone</div>
    </div>
    """)


    with gr.Tabs():
        with gr.Tab("Voice Clone"):
            with gr.Row():
                with gr.Column(scale=1):
                    ref_audio = gr.Audio(
                        label="Reference Audio",
                        type="filepath",
                        interactive=True,
                        show_label=True
                    )

                    ref_text = gr.Textbox(label="Reference Text", lines=3)
                    target_text = gr.Textbox(label="Target Text", lines=5)

                    language = gr.Dropdown(
                        ["Auto", "English", "Hindi"],
                        value="Auto",
                        label="Language"
                    )

                    size = gr.Slider(0.5, 2.0, value=1.0, label="Size")
                    chunk_size = gr.Slider(50, 500, value=70, label="Chunk Size")
                    chunk_gap = gr.Slider(0, 1.0, value=0.3, label="Chunk Gap (s)")
                    seed = gr.Number(value=-1, label="Seed (-1 Auto)")
                    tone = gr.Dropdown(
                        ["Default", "Calm", "Storytelling", "Aggressive Motivation","Friendly",
                         "Professional", "Emotional",],
                        value="Default",
                        label="Emotion Tone"
                    )


                    generate_btn = gr.Button("Clone & Generate")

                with gr.Column(scale=1):
                    out_audio = gr.Audio(label="Generated Audio")
                    status = gr.Textbox(label="Status", lines=3)

            generate_btn.click(
                fn=generate_audio,
                inputs=[ref_audio, ref_text, target_text, language, size, chunk_size, chunk_gap, seed, tone],
                outputs=[out_audio, status]
            )

demo.launch(share=True)

