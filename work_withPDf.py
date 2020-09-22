import PyPDF2# to be pip installed
import Speaker # find file in this repo
import time# optional
#Speaker uses the default voices available in your os . The speed and voice settings can be changed from the control panel in Windows
filename = str(input("Enter the filename\t"))
path = "D:\\python_envs\\All_other_codes\\" + filename+'.pdf' # can be changed  
file = PyPDF2.PdfFileReader(path)
try: #there may be errors wrt to pdf file reffered to 
	print("The book" , filename, "was authored by" , file.getDocumentInfo()['/Creator'] , "and is " , file.getNumPages() , "pages long")# print the author name
	firstpage , lastpage = int(input("Enter the first page\t")) , int(input('Enter the last page\t'))# 'creator' can be swapped with 'author'
	text = " "
	startpage, endpage = int(input("Enter the startpage")) , int(input("Enter the lastpage"))
	for i in range(startpage , endpage):#iterate over the pages
		text += file.getPage(i).extractText() # so that all the content in the pages is stored in a global variable


	with open('Contents.txt' , 'w' , encoding="utf-8") as f:
		f.write(text)#dump the contents in the range of pages in a *.txt file
	print(text)

	time.sleep(1)
	Speaker.speak("Reading out the contents.")
	time.sleep(2)
	Speaker.speak(text)

except:
	print("error")





