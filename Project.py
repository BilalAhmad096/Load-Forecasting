def project():
    #Driver Code:
    introduction()
    ijazat=getpermission()
    if ijazat=="True":
        questionnaire()
    else:
        baharniklo()
    

def aawaazdo():
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=0.2)
            print ("Please respond now:")
            audio = r.listen(source)
            try:
                    text=r.recognize_google(audio)
                    print(text)
                    return text
            except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
	
            except sr.RequestError as e:
                    print("Could not request results from Google")

                    
def bulwao(b):
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(b)
    engine.runAndWait()

def savekarlo(lst):
    import json
    with open('test.txt', 'a') as f:
        f.write(json.dumps(lst))

def introduction():
    b="Hello This is Bilals Bot:"
    bulwao(b)
    print (b)
    b = "I am an automated System, I shall be very thankful if you could answer my questions"
    print (b)
    bulwao(b)

def getpermission():
    b = "Can I have a few minutes of your time"
    print (b)
    bulwao(b)
    text=aawaazdo()
    baharbhejo=sentiment_analyse(text)
    return baharbhejo

def questionnaire():
    lst=[]
    b ="What is your name?"
    print (b)
    bulwao(b)
    a=aawaazdo()
    lst.append(a)
    b ="How old are you?"
    print (b)
    bulwao(b)
    a=aawaazdo()
    lst.append(a)
    b ="Were you tested positive for corona Virus?"
    print (b)
    bulwao(b)
    a=aawaazdo()
    lst.append(a)
    if a=="yes":
        b ="Did you have high fever?"
        print (b)
        bulwao(b)
        a=aawaazdo()
        lst.append(a)
        b = "Thanks for your time Really appreciate it."
        print (b)
        bulwao(b)
        savekarlo(lst)
            
    else:
        baharniklo()
        savekarlo(lst)
    
def baharniklo():
    b ="Thanks for your time Have a good Day."
    bulwao(b)
    print (b)
    

def sentiment_analyse(sentiment_text):
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    if score['neg'] > score['pos']:
        return "False"
    elif score['neg'] < score['pos']:
        return "True"
    else:
        return "False"

#Running the driver coder:
project()

