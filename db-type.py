import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '100,100'
import random
import pgzrun
import pygame
import socket

pygame.mixer.music.load("song.mp3") #SubspaceAudio
pygame.mixer.music.play(-1)

level=-2
url="http://localhost"
message=""
gemacht=False

db_ports = {
    "MySQL/MariaDB": 3306,
    "PostgreSQL": 5432,
    "SQL Server": 1433,
    "Oracle DB": 1521,
}

def check_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((host, port))
        s.close()
        return True
    except:
        return False

def detect_local_db():
    global message
    found = []
    for db_name, port in db_ports.items():
        if check_port("localhost", port):
            found.append(db_name)
    if found:
        message+="Founded databases on "+url+": "+found[0]+"\n"
    else:
        message+="No known open database-ports"

def draw():
    global level, url,message
    screen.clear()
    if level==-2:
        screen.blit("disclaimer",(0,0))
    if level == -1:
        screen.blit("title", (0, 0))
    elif level == 0:
        screen.blit("intro", (0, 0))
    elif level == 1:
        screen.blit("back", (0, 0))
        screen.draw.text("Website to scan:", center=(400, 130), fontsize=24, color=(25, 200, 255))
        screen.draw.text(url, center=(400, 180), fontsize=24, color=(255, 255, 0))
    elif level == 2:
        screen.blit("back", (0, 0))
        screen.draw.text(message, center=(400, 130), fontsize=24, color=(225, 200, 255))

def on_key_down(key, unicode=None):
    global level, url
    if key==keys.ESCAPE:
        pygame.quit()
    if key == keys.BACKSPACE:
        url = ""
    elif key == keys.RETURN and level == 1:
        level = 2
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
    elif unicode and key != keys.RETURN and level==1:
        url += unicode

def update():
    global level,checker,gemacht,url
    if (level == 0 or level==-2) and keyboard.RETURN:
        level +=1
    elif level -1 and keyboard.space:
        level = 0
    if level==1:
        pass
    if level==2:
        if not gemacht:
            detect_local_db()
            gemacht=True
    if level==2 and keyboard.space:
        level=0

pgzrun.go()
