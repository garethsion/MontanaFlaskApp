import subprocess

# This is not a good way of doing this, but works right now. better to search for the file in the directory.
def call_toptica():
    oprog = subprocess.call(["C:\Program Files (x86)\TOPTICA\TOPAS DLC pro 2.4.0.0a0df44\TOPAS_DLC_pro.exe"])
    return