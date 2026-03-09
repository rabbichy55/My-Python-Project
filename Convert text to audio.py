import pyttsx3 # Importing the pyttsx3 library to enable text-to-speech functionality.
import PyPDF2 # Importing the PyPDF2 library to work with PDF files.
book = open("The-Metamorphosis.pdf", "r") # Opening the file 'book.txt' in read mode and assigning it to the variable 'book'.
pdfReader = PyPDF2.PdfFileReader(book) # Creating a PDF reader object using the 'PdfFileReader' class from the PyPDF2 library and passing the 'book' variable as an argument.
pages = pdfReader.numPages # Getting the total number of pages in the PDF document and assigning it to the variable 'pages'.
print(pages) # Printing the total number of pages in the PDF document.
friend = pyttsx3.init() # Initializing the text-to-speech engine and assigning it to the variable 'friend'.
page = pdfReader.getPage(5) # Getting the first page of the PDF document using the 'getPage' method and assigning it to the variable 'page'.
text = page.extractText() # Extracting the text from the page using the 'extractText' method and assigning it to the variable 'text'.
friend.say(text) # Using the 'say' method of the 'friend' object to convert the given text into speech.
friend.runAndWait() # Calling the 'runAndWait' method to process the speech commands and play the audio output.
