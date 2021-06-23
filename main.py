import time
from bs4 import BeautifulSoup
import requests
from gtts import gTTS
import os

previous=" "

while(1):
    url="https://www.espncricinfo.com/series/icc-world-test-championship-2019-2021-1195334/india-vs-new-zealand-final-1249875/live-cricket-score"
    # replace this URL with present match url
    cricInfo=requests.get(url).text
    soup=BeautifulSoup(cricInfo,'lxml')
    comm=soup.find('div',{"class":"d-flex match-comment-padder align-items-center"})
    runs=comm.find("div",{"class":"match-comment-run"}).text
    shortText=comm.find("div",{"class":"match-comment-short-text"}).text
    comment=comm.find("div",{"class":"match-comment-long-text"}).text
    finalText=shortText+"\n"+comment
    if previous!=finalText:
        previous=finalText
        output=gTTS(finalText,lang='en-us',slow=False,)
        output.save("output.mp3")
        file="output.mp3"
        os.system("mpg123 " +file)
        time.sleep(5)
