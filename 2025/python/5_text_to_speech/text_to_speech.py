import gtts
#from playsound import playsound
import PyPDF2

#opens the pdf file
with open("design_interfaces.pdf", "rb") as file :
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text +=page.extract_text()
    
#make request to google get synthesis. 
#we define the pdf book that we want it to synthesize and then the language
tts = gtts.gTTS(text, lang='en')

#the text to speech object is saved into an mp3 file
tts.save("design_interfaces.mp3")

#plays the audio file created
#playsound("design_interfaces.mp3")

