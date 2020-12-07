import os
import pandas as pd 
from pydub import AudioSegment
from gtts import gTTS


def textToSpeech(text,filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language ,slow=False)
    myobj.save(filename)

def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    #genarate1 krupaya dyaan de
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3",format = "mp3")

    #generate3 se chal kar
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 91000
    finish = 92000
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3",format = "mp3")

    #generate5 se raaste
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3",format = "mp3")
   
    #generate7 ko jane wali train 
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3",format = "mp3")  
      
    #generate9 kuch hi samay me
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3",format = "mp3")

    #generate11 pe aarahi h
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3",format = "mp3")

def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        textToSpeech(item['se'],'2_hindi.mp3')                                #generate2 is from city
        textToSpeech(item['via'],'4_hindi.mp3')                                 #generate4 is via
        textToSpeech(item['city'],'6_hindi.mp3')                                #generate6 is too city
        textToSpeech(str(item['train_no'])+str(item['train_name']),'8_hindi.mp3')   #generate8 train number and name
        textToSpeech(item['platform'],'10_hindi.mp3')                           #generate10 platform number

        audios = [f"{i}_hindi.mp3" for i in range(1,12)]
        announcement = mergeAudios(audios)
        announcement.export(f"anouncement_{item['train_no']}_{index+1}.mp3",format="mp3")

   




if __name__ == "__main__":
    print("Genrating skeleton....")
    generateSkeleton()
    print("Genreating announcemnet....")
    generateAnnouncement("announce_hindi.xlsx")
    
   


    

    
    

    

    

    

    



