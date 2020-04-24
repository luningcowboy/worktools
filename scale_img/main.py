import os, sys, subprocess
from PIL import Image

def run():
    print('run')
    cmd = 'find ./emoji -name "*.png"'
    ret = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    out = ret.stdout.readlines()
    for fileName in out:
        fileName = fileName.split('\n')[0]
        print(fileName)
        img = Image.open(fileName)
        img.resize((135, 135), Image.ANTIALIAS).save(fileName)

run()
