from moviepy.editor import *

#mp4_file i  mp3_file mają zawierać ścieżki plików

#plik.mp4 - twój plik mp4 
mp4_file = r'C: plik.mp4'

#plik.mp3 - nowy plik mp3, nazwa może być dowolna
mp3_file = r'C: plik.mp3'

videoclip = VideoFileClip(mp4_file)
audioclip = videoclip.audio
audioclip.write_audiofile(mp3_file)
audioclip.close()
videoclip.close()