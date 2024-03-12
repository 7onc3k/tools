import os
import subprocess

# Nastavte cestu k adresáři s audio soubory a název výstupního souboru
audio_directory = r'D:\Nová složka\softwareko'
output_file_path = 'transcription/transkripce.txt'

whisper_path = r'C:\Users\thanh\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts\whisper.exe'

# Projde audio soubory v zadaném adresáři
for filename in os.listdir(audio_directory):
    if filename.endswith(('.mp3', '.wav')):
        full_audio_path = os.path.join(audio_directory, filename)
        print(f"Zpracovávám {full_audio_path}...")

        # Sestavení a spuštění příkazu Whisper
        command = [whisper_path, full_audio_path]
        result = subprocess.run(command, capture_output=True, text=True)

        # Kontrola, zda proces proběhl úspěšně
        if result.returncode == 0:
            # Výpis a uložení transkripce
            print(f"Transkripce {filename} dokončena.")
            with open(output_file_path, 'a') as output_file:
                output_file.write(f"Transkripce pro {filename}:\n{result.stdout}\n\n")
        else:
            print(f"Chyba při zpracování {filename}: {result.stderr}")
