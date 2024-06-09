import tkinter as tk
from tkinter import filedialog, Text
import whisper

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

def transcribe_audio():
    file_path = entry.get()
    if file_path:
        try:
            model = whisper.load_model("small")
            result = model.transcribe(file_path, verbose=True, fp16=False, language="ja")
            transcription = result['text']
            
            if not transcription:
                raise ValueError("Transcription is empty.")
            
            # 文ごとに分割して改行
            sentences = transcription.split('。')
            sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
            
            output_text.delete(1.0, tk.END)
            for sentence in sentences:
                output_text.insert(tk.END, sentence + '。\n\n')
        except Exception as e:
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, "失敗しました\n")


app = tk.Tk()
app.title("Audio Transcription App")

frame = tk.Frame(app, padx=10, pady=10)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Select Audio File:")
label.pack(pady=5)

entry = tk.Entry(frame, width=50)
entry.pack(pady=5)

upload_btn = tk.Button(frame, text="Upload", command=upload_file)
upload_btn.pack(pady=5)

transcribe_btn = tk.Button(frame, text="Transcribe", command=transcribe_audio)
transcribe_btn.pack(pady=20)

output_text = Text(frame, height=20, width=80)
output_text.pack(pady=5)

app.mainloop()
