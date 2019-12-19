#!python3

import PyPDF2, sys

def valid():
   try:
      if len(sys.argv) < 4:
         raise Exception('Command requries pdf file name and page number(s)')
   except Exception as e:
      print(str(e))
      return False
   return True


def split(filename, pageNumber):

   try:
      reader = PyPDF2.PdfFileReader(open(filename,'rb'))
      reader.getPage(pageNumber)
      writer = PyPDF2.PdfFileWriter()
      for p in range(pageNumber):
         writer.addPage(reader.getPage(p))
      splitFile = open('split_1.pdf','wb')
      writer.write(splitFile)
      splitFile.close()
      writer = PyPDF2.PdfFileWriter()
      for p in range(pageNumber,reader.numPages):
         writer.addPage(reader.getPage(p))
      splitFile = open('split_2.pdf','wb')
      writer.write(splitFile)
      splitFile.close()
   except Exception as e:
      print(str(e))
      return
   

if __name__== "__main__":
   if not valid():
      exit()
   else:
      filename = sys.argv[2]
      pageNumbers = int(sys.argv[3])
      if sys.argv[1] == "split":
         split(filename, pageNumbers)

