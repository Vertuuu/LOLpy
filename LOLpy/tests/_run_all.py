import subprocess
import os

debug_dir = os.path.join("LOLpy/src/LOLpy_Vertuuu")
debug_files = os.listdir(debug_dir)
confirm = True         #change this boolean if you want it to ask you before running next debug file in each execution

for debug_file in debug_files:
    if debug_file.endswith("debug.py") and not debug_file.startswith("_"):
        debug_file_path = os.path.join(debug_dir, debug_file)
        process = subprocess.Popen(["python", debug_file_path])
        process.wait()
        if confirm:
            input(f"{debug_file} was executed. Wanna run next?")
            os.system("cls")
        