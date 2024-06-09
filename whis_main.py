import whisper

model = whisper.load_model("small")  # モデル指定
result = model.transcribe("あいさつ.mp3", verbose=True, fp16=False, language="ja")  # ファイル指定
transcription = result['text']

# 文ごとに分割する
sentences = transcription.split('。')  # 日本語の句点「。」で分割
sentences = [sentence.strip() for sentence in sentences if sentence.strip()]  # 空文を削除し、トリム

# 改行してテキストファイルに書き込む
with open('transcription.txt', 'w', encoding='UTF-8') as f:
    for sentence in sentences:
        f.write(sentence + '。\n')  # 各文の後に句点「。」を付けて改行

print("Transcription has been written to transcription.txt")
