import os
from moviepy.editor import VideoFileClip

# Nastavte cestu ke složce s videi
video_folder = r'D:\Nová složka\softwareko'


# Projděte všechny soubory ve složce
for file_name in os.listdir(video_folder):
    # Zkontrolujte, zda je soubor video
    if file_name.endswith((".mp4", ".avi", ".mov", ".mkv")):
        # Složte cestu k videu
        video_path = os.path.join(video_folder, file_name)
        
        # Načtěte video pomocí moviepy
        video = VideoFileClip(video_path)
        
        # Extrahujte audio stopu jako mp3
        audio_path = os.path.join(video_folder, os.path.splitext(file_name)[0] + ".mp3")
        video.audio.write_audiofile(audio_path)
        
        # Uzavřete video
        video.close()
        
        print(f"Převedeno video {file_name} na {os.path.basename(audio_path)}")