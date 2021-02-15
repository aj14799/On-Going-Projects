# importing required modules 
import PyPDF2 

# creating a pdf file object 
pdfFileObj = open('C:/Users/Aditya Jha(Adi)/Downloads/Resume-Aditya-Jha.pdf', 'rb') 

# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

# printing number of pages in pdf file 
print("Totoal",pdfReader.numPages) 

# creating a page object 
pageObj = pdfReader.getPage(0) 

# extracting text from page 
print("/n/n/n****/n",pageObj.extractText()) 

# closing the pdf file object 
pdfFileObj.close() 
