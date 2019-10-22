from tkinter import *
import speech_recognition as sr

recognizer = sr.Recognizer
returnMsg = ""

class CB:
    def listenMessage(self, master):
        frame = Frame(master)
        frame.pack()
        self.lbl = Label(frame, text="Parla pure")
        self.lbl.pack()

        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Parla qualsiasi cosa: ")
            audio = r.listen(source)
            print("Un attimo che sto elaborando questo messaggio...")
            try:
                text = r.recognize_google(audio, language="it-IT")
                print("Hai detto: {}\n".format(text))
                return text
            except:
                print("Ammazza, non ce l'ho fatta riconosscere la tua voce, mi dispiace")
                text = "Error"
                return text

        #master.mainloop()

        self.returnMessage(text)


    def returnMessage(self, msg):
        returnMessage = msg
        return returnMsg
