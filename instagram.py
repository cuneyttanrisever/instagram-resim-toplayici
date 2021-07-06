from urllib.request import urlopen, Request , urlretrieve
import re
import os
os.system('cls' if os.name == 'nt' else 'clear')
print ("""
###############################################
#                                             #  
# By DexmoD // instagram resim toplama aracı  #
#                                             #  
###############################################

""")
sor=input("İnstagram user adı giriniz. = ")
adres=f"https://www.instagram.com/{sor}/?__a=1"

headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }

f = urlopen(Request(adres, headers=headers))
content=f.read().decode('utf-8')


dex=re.findall("\"thumbnail_src\"\:\"(.*?)\",",str(content))
yaz=open("insta.txt","w")
sira=0

for i in dex:
        urlretrieve(i,sor+str(sira)+".jpeg")
        sira+=1
        yaz.write( str((i))+"\n")
        print (sor+str(sira)+".jpeg adında resim kaydedildi")
print ("Toplam ",len(dex), "tane resim indirildi")
yaz.close()
if dex !="":
        print ("İndirilen resim linkleride insta.txt dosyasına kayıt edilmiştir")
