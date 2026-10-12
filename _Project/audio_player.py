import pyaudio
import wave
from pydub import AudioSegment
import numpy

SUPORTED_FORMATS = ["wav", "mp3"]
VOLUME_SCALE = 100

class TrakPlayer:
    def __init__(self, trak_path, volume):
        self.TRAK_PATH = trak_path
        self.TRAK_DATA = []
        self.VOLUME = volume
        self.PLAY = True
        self.IS_TRAK_LOADED = False
        self.CHANNELS = 0
        self.RATE = 0
        self.WIDTH = 0

    def load_trak(self):
        self.correct_trak_path_format()
        trak_data = wave.open(self.transform_trak_format(), "rb")

        self.CHANNELS = trak_data.getnchannels()
        self.RATE = trak_data.getframerate()
        self.WIDTH = trak_data.getsampwidth()

        self.TRAK_DATA = []
        data = trak_data.readframes(1024)
        while data:
            self.TRAK_DATA.append(numpy.frombuffer(data, numpy.int16))
            data = trak_data.readframes(1024)

        max_value = max(self.TRAK_DATA)
        for index in range(len(self.TRAK_DATA)):
            self.TRAK_DATA[index] = self.TRAK_DATA[index] / max_value * VOLUME_SCALE

        self.IS_TRAK_LOADED = True

    def load_trak_with_new_path(self, trak_path):
        self.TRAK_PATH = trak_path
        self.load_trak()

    def play_trak(self):
        if not self.IS_TRAK_LOADED:
            return

        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(self.WIDTH),
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        output=True)

        for trak_frames in self.TRAK_DATA:
            if (not self.PLAY):
                continue
            trak_frames = (trak_frames * self.VOLUME).astype(numpy.int16).tobytes()
            stream.write(trak_frames)

        stream.stop_stream()
        stream.close()
        p.terminate()

    def correct_trak_path_format(self):
        if "." in self.TRAK_PATH:
            return

        for format in SUPORTED_FORMATS:
            if self.is_file_exist(self.TRAK_PATH + "." + format):
                self.TRAK_PATH += "." + format

    def transform_trak_format(self):
        file_name = "_Project/temp/temp_file.wav"
        form = self.TRAK_PATH[self.TRAK_PATH.rindex(".")+1:]
        audio = AudioSegment.from_file(self.TRAK_PATH, form)
        TrakPlayer.create_file(self.TRAK_PATH)
        audio.export(file_name, format="wav")
        return file_name

    def create_file(path_name):
        try:
            open(path_name, "x")
        except FileExistsError:
            pass
            #print("Error: file already exists")

    def is_file_exist(path: str):
        try:
            open(path)
        except:
            return False
        return True

if __name__ == "__main__":
    print("starting...")
    import sys
    player = TrakPlayer(sys.argv[1], 50 / 100.)
    print("loading trak...")
    player.load_trak()
    print("playing trak...")
    player.play_trak()
