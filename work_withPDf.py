import PyPDF2

filename = str(input("Enter the filename"))
path = "D:\\python_envs\\All_other_codes\\" + filename+'.pdf'# can be changed  
file = PyPDF2.PdfFileReader(path)

print("The book" , filename, "was authored by" , file.getDocumentInfo()['/Author'] , "and is " , file.getNumPages() , "pages long")# print the author name


firstpage , lastpage = int(input("Enter the first page")) , int(input('Enter the last page'))
text = " "

for i in range(firstpage, lastpage+1):#iterate over the pages
	text+= file.getPage(i).extractText() # so that all the content in the pages is stored in a global variable


with open('Contents.txt' , 'w') as f:
	f.write(text)#dump the contents in the range of pages in a *.txt file



print(text)#reference


