#! Python3
import PyPDF2, sys

# Combine any number of pdf files into one pdf

if len(sys.argv) < 2:
   exit()

writer = PyPDF2.PdfFileWriter()

# Read through all pdf files and combine
for pdf in sys.argv[1:]:
   try: # Skip any invalid file
      reader = PyPDF2.PdfFileReader(pdf)
      for pageNum in range(reader.numPages):
         writer.addPage(reader.getPage(pageNum))
   except:
      continue

outputFile = open('COMBINED_OUTPUT.pdf', 'wb')
writer.write(outputFile)
print(outputFile.name)

outputFile.close()



