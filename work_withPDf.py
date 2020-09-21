import PyPDF2
import Speaker 
import time

filename = str(input("Enter the filename\t"))
path = "D:\\python_envs\\All_other_codes\\" + filename+'.pdf'# can be changed  
file = PyPDF2.PdfFileReader(path)
try: 
	print("The book" , filename, "was authored by" , file.getDocumentInfo()['/Creator'] , "and is " , file.getNumPages() , "pages long")# print the author name
	firstpage , lastpage = int(input("Enter the first page\t")) , int(input('Enter the last page\t'))
	text = " "

	for i in range(4 , 7):#iterate over the pages
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





