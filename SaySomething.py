import win32com.client

def SaySomething(chosenWords):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(chosenWords)

if __name__ == '__main__': 
    SaySomething("Get out of my office Pam!")