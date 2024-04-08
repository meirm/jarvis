from transformers import VitsModel, AutoTokenizer
import torch
import simpleaudio as sa
import numpy as np

class TextToSpeechPlayer:
    def __init__(self, model_name="facebook/mms-tts-eng", sample_rate=16000):
        self.model = VitsModel.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.sample_rate = sample_rate

    def text_to_speech(self, text):
        inputs = self.tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            output = self.model(**inputs).waveform
        return output

    def play_audio(self, waveform):
        audio_np = waveform.numpy()
        audio_np *= 32767 / np.max(np.abs(audio_np))
        audio_np = audio_np.astype(np.int16)
        self.play_obj = sa.play_buffer(audio_np, num_channels=1, bytes_per_sample=2, sample_rate=self.sample_rate)
        

    def setProperty(self,property, value):
        pass
    
    def say(self, text):
        waveform = self.text_to_speech(text)
        self.play_audio(waveform)

    def stop(self):
        self.play_obj.stop()

    def runAndWait(self):
        self.play_obj.wait_done()
# Example usage
if __name__ == "__main__":
    tts_player = TextToSpeechPlayer()
    tts_player.say("some example text in the English language")
