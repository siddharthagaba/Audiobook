import pyttsx3
import PyPDF2

book = open('moby-dick.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print('Number of pages:')
print(pages)
speaker = pyttsx3.init()
speaker.setProperty("rate", 150)
voices = speaker.getProperty('voices')

print('Choose voice (enter number 1-3):')
v = int(input())
if v == 1:
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    speaker.setProperty('voice', voice_id)
if v == 2:
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0"
    speaker.setProperty('voice', voice_id)
if v == 3:
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    speaker.setProperty('voice', voice_id)
print('Enter the page to start reading from:')
start = int(input())
print('Enter the page number till you want to end, or press 0 to read full:')
end = int(input())
if end == 0:
    for num in range(start-1, pages):
        page = pdfReader.getPage(num)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()
else:
    for num in range(start-1, end):
        page = pdfReader.getPage(num)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()