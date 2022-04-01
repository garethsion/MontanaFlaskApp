import subprocess

# This is not a good way of doing this, but works right now. better to search for the file in the directory.
def call_lq():
    oprog = subprocess.call(["C:\Program Files (x86)\Laser Quantum Ltd\LQ Remote App\RemoteApp Laser Control.exe"])
    return