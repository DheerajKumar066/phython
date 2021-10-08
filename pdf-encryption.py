# import PdfFileWriter and PdfFileReader
# class from PyPDF2 library
from PyPDF2 import PdfFileWriter, PdfFileReader

password_values = ['0910','2345','5367','9871']
files_names = ["dheeraj.pdf","pradeep.pdf","dhk.pdf","ganesh.pdf"]

for j in range(0,4):
	# create a PdfFileWriter object
	out = PdfFileWriter()

	# Open our PDF file with the PdfFileReader
	file = PdfFileReader("/home/linux/DHK/Span/MailSent/Encrypted_PDF-Files/"+files_names[j])

	# Get number of pages in original file
	num = file.numPages

	# Iterate through every page of the original
	# file and add it to our new file.
	for idx in range(num):

		# Get the page at index idx
		page = file.getPage(idx)

		# Add it to the output file
		out.addPage(page)


	# Create a variable password and store
	# our password in it.
	password = password_values[j]

	# Encrypt the new file with the entered password
	out.encrypt(password)

	# Open a new file "myfile_encrypted.pdf"
	with open("/home/linux/DHK/Span/MailSent/Encrypted_PDF-Files/"+files_names[j], "wb") as f:

		# Write our encrypted PDF to this file
		out.write(f)