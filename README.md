# Bilingual-TTS-Reader
A cross-platform (TTS-enabled) command-line script for foreign language practice using bilingual tab-delimited CSV files

The script was initially meant to be used with the output of https://github.com/jartificer/sentence-pairs (originally by Ken Micklas: https://github.com/kmicklas/sentence-pairs) but can take any bilingual tab-delimited CSV file as an input, as long as the file name is ```[learned_language][native_language].csv```. So if for instance you are an English speaker wanting to learn Italian, your file should be called ```iten.csv```. Moreover, it should be located in the same folder as the script.
For now, what the script does is to display a foreign language sentence, read it out using Google Translate's text-to-speech API (via gTTS), wait for user input, then display the equivalent sentence in the user's native language. This is done sequentially for all sentence pairs in the CSV file.

Prerequisites:
* Python 3 with the following packages installed:
  * gTTS
  * pydub
  * simpleaudio (optional, but should be installed in case of Permission Denied errors)

```Usage: python3 reader.py learned_language native_language starting_row step``` 

```e.g. python3 reader.py fr en 50 2 (this would read a document named fren.csv starting from row 50, then read row 52, 54 etc.)```
