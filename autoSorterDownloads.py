import os 
import shutil

videoFile = open('VideoList.txt', 'r')
listaVideoEkstenzija = videoFile.readlines()
videoFile.close()

PicFile = open('PictureList.txt', 'r')
listaEkstenzijaSlika = PicFile.readlines()
PicFile.close()

OfficeList = open('OfficeList.txt', 'r')
listaOfficeEkstenzija = OfficeList.readlines()
OfficeList.close()

lokacija = 'C:/Users/Armin/Downloads'

files = os.listdir(lokacija)


for file in files:
    ekstenzija = file.split('.')[-1].lower()
    n = len(listaVideoEkstenzija)
    for i in range(0, n):
        if ekstenzija == listaVideoEkstenzija[i][:-1]:
            shutil.move(os.path.join(lokacija, file), 'C:/Users/Armin/Downloads/Video')
            break
    n = len(listaEkstenzijaSlika)
    for i in range(0,n):
        if ekstenzija == listaEkstenzijaSlika[i][:-1].lower():
            shutil.move(os.path.join(lokacija, file), 'C:/Users/Armin/Downloads/Slika')
            break
    n = len(listaOfficeEkstenzija)
    for i in range(0,n):
        if ekstenzija == listaOfficeEkstenzija[i][:-1].lower():
            shutil.move(os.path.join(lokacija, file), 'C:/Users/Armin/Downloads/office')
            break   
    
    if ekstenzija == 'mp3' or ekstenzija == 'wav':
        shutil.move(os.path.join(lokacija, file), 'C:/Users/Armin/Downloads/Audio')
    elif ekstenzija == 'pdf':
        shutil.move(os.path.join(lokacija, file), 'C:/Users/Armin/Downloads/pdf')
    elif ekstenzija == 'zip' or ekstenzija == 'rar':
        shutil.move(os.path.join(lokacija, file), 'C:/Users/Armin/Downloads/zip')
    elif ekstenzija == 'exe':
        shutil.move(os.path.join(lokacija, file), 'C:/Users/Armin/Downloads/exe')   
    elif ekstenzija == 'txt':
        shutil.move(os.path.join(lokacija, file), 'C:/Users/Armin/Downloads/txt')   
    