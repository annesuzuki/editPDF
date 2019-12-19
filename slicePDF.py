#!python3

import PyPDF2, sys

# Check validity of command line arguments
def valid():
   try:
      if len(sys.argv) < 4:
         raise Exception('Command requries pdf file name and page number(s)')
   except Exception as e:
      print(str(e))
      return False
   return True

# Split creates two new documents as if one had "split" the document physcally
def split(filename, pageNumber):
   try:
      # Open pdf file that needs splitting
      reader = PyPDF2.PdfFileReader(open(filename,'rb'))
      reader.getPage(pageNumber)
      writer = PyPDF2.PdfFileWriter()

      # Create 2 pdf files
      for p in range(pageNumber):   # split_1.pdf contains pages 1 - pageNumber
         writer.addPage(reader.getPage(p))
      splitFile = open('split_1.pdf','wb')
      writer.write(splitFile)
      splitFile.close()
      writer = PyPDF2.PdfFileWriter()
      for p in range(pageNumber,reader.numPages): # split_2.pdf contains rest of document
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

