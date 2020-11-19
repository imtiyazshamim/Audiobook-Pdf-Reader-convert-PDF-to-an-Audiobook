import pyttsx3
import PyPDF2
book =open('enter file name.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
speaker =pyttsx3.init()
for num in range('enter the page number',pages):
    page =pdfReader.getPage()
    text =page.extractText()
    speaker.say(text)
    speaker.runAndWait()