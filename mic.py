import speech_recognition as sr
import os
import openai
import time

r = sr.Recognizer()
m = sr.Microphone(device_index=1) #device_index=1
print(sr.Microphone.list_microphone_names())
def storeinwav():
    text = ""
    with m as source:
        r.adjust_for_ambient_noise(source, duration=2)
        os.system(f"say 'Bark Bark'") 
        os.system(f"echo 'Bark  Bark'")
        time.sleep(0.1)
        audio = r.listen(source)
        os.system(f"echo 'Understood'")
        os.system(f"say 'Understood'") 
        with open("microphone-results.wav", "wb") as f:
            f.write(audio.get_wav_data())
        

def wavtotext():
    openai.api_key = "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"
    audio_file= open("microphone-results.wav", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript["text"]

while 1 == 1:
    storeinwav()
    text = wavtotext()
    print(text)
    os.system(f"echo '{text} Bark  Bark'")
    os.system(f"say '{text} Bark Bark'") 
