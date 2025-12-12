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
    "SQL Server (MSSQL)": 1433,   # 1434 für Browser Service
    "Oracle DB": 1521,            # auch 2483/2484 für TCPS
    "IBM Db2": 50000,             # weitere Ports 50001-50050
    "SAP MaxDB": 7210,

    "SQLite": None,               # keine Netzwerkverbindung

    "MongoDB": 27017,             # 27018 Shard, 27019 Config
    "Redis": 6379,                # 26379 Sentinel, 16379 Cluster
    "Cassandra": 9042,            # 7000 intern
    "Elasticsearch": 9200,        # 9300 intern
    "CouchDB": 5984,              # 6984 HTTPS
    "Neo4j": 7474,                # 7473 HTTPS
    "ArangoDB": 8529,
    "Riak": 80,
    "HBase": 16000,               # 16020/16030 für RegionServer
    "DynamoDB": None,             # AWS-Service, kein Port
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
    global message,url
    found = []
    for db_name, port in db_ports.items():
        if check_port(url, port):
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
