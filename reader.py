import sys
import csv
from itertools import islice
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

if len(sys.argv) != 5:
    print('Usage: python3 reader.py learned_language native_language starting_row step (e.g. python3 reader.py fr en 50 1)')
    sys.exit(1)

lang1 = sys.argv[1]
lang2 = sys.argv[2]
fromrow = sys.argv[3]
step = sys.argv[4]


with open('%s%s.csv' %(lang1, lang2), 'r', encoding='utf-8') as sortedFile:
    reader = csv.reader(sortedFile, delimiter='\t')
    i=1
    for row in islice(reader, int(fromrow)-1, None, int(step)):
        print(int(fromrow)-1+i, row[0])
        i+=int(step)
        tts = gTTS(row[0], lang1)
        with open('tts.mp3', 'wb') as f:
            tts.write_to_fp(f)
        with open('tts.mp3', 'rb') as f:
            sound = AudioSegment.from_file(f, format="mp3")
            play(sound)
        input()
        print("\t", row[1])
        input()        
