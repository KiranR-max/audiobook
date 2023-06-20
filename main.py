import pyttsx3
import PyPDF3
book=open(r'C:/Users/kirakum1/Downloads/bigtable-osdi06.pdf','rb')
pdfReader=PyPDF3.PdfFileReader(book)
pages=pdfReader.numPages

speaker=pyttsx3.init()
for n in range(7,pages):
    page=pdfReader.getPage(n)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()
