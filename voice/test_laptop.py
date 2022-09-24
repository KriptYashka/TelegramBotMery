from vosk import Model, KaldiRecognizer
import soundfile as sf  # pip install pysoundfile
import sys
import json
import os
import time
import wave
import telebot
import uuid
import ffmpy


class VoiceRecognize:
    def __init__(self):
        model = Model(r"./voice/vosk-model-small-ru-0.22")
        self.hz = 48000
        self.rec = KaldiRecognizer(model, self.hz)

    def __convert_to_wave(self, bot: telebot.TeleBot, message: telebot.types.Message):
        filename = str(uuid.uuid4())
        file_name_full = "./voice/" + filename + ".ogg"
        file_name_full_converted = "./voice/" + filename + "_conv.wav"
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(file_name_full, 'wb') as new_file:
            new_file.write(downloaded_file)

        ff = ffmpy.FFmpeg(
            executable='./voice/ffmpeg/bin/ffmpeg.exe',
            inputs = {file_name_full: None},
            outputs = {file_name_full_converted: None}
        )
        print(ff.cmd)
        ff.run()

        # data, samplerate = sf.read(file_name_full)
        # sf.write('new_file.wav', data, samplerate)
        return file_name_full_converted

    def recognize(self, bot: telebot.TeleBot, message: telebot.types.Message):
        file_name_full_converted = self.__convert_to_wave(bot, message)
        wf = wave.open(file_name_full_converted, "rb")

        result = ''
        last_n = False

        while True:
            data = wf.readframes(self.hz)
            if len(data) == 0:
                break

            if self.rec.AcceptWaveform(data):
                res = json.loads(self.rec.Result())

                if res['text'] != '':
                    result += f" {res['text']}"
                    last_n = False
                elif not last_n:
                    result += '\n'
                    last_n = True

        res = json.loads(self.rec.FinalResult())
        result += f" {res['text']}"

        print(result)


def main():
    vr = VoiceRecognize()


if __name__ == '__main__':
    main()