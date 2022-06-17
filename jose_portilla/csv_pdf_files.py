import csv
import os

csv_files_url = "/jose_portilla/csv_files/"

data = open(os.getcwd() + csv_files_url + "example.csv", encoding="utf-8")
csv_data = list(csv.reader(data))

print(csv_data[0], "\n")
for data in csv_data[:3]:
    print(data[0], data[1], data[2], data[3])


###################################################################################################################################################


file_output = open(os.getcwd() + csv_files_url + "file_output.csv", "w", newline="")
csv_writer = csv.writer(file_output, delimiter=",")
csv_writer.writerow(["H1", "H2", "H3"])
csv_writer.writerows([["01", "02", "03"], ["04", "05", "06"]])
file_output.close()

file_output = open(os.getcwd() + csv_files_url + "file_output.csv", "a", newline="")
csv_writer = csv.writer(file_output)
print("Number of characters written:", csv_writer.writerow(["07", "08", "09"]))
file_output.close()


###################################################################################################################################################


import PyPDF2

pdf_files_url = "/jose_portilla/pdf_files/"

# Read binary
file = open(os.getcwd() + pdf_files_url + "Working_Business_Proposal.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(file)
print("Working_Business_Proposal page number:", pdf_reader.numPages)

p0 = pdf_reader._get_page(0)
# print(p0.extract_text())

pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.add_page(p0)
pdf_output = open(os.getcwd() + pdf_files_url + "file_output.pdf", "wb")
pdf_writer.write(pdf_output)
file.close()


###################################################################################################################################################


import re

data = open(os.getcwd() + csv_files_url + "find_the_link.csv", encoding="utf-8")
csv_data = list(csv.reader(data))
link_str = ""

for row_num, data in enumerate(csv_data):
    link_str += data[row_num]

print(link_str)  # Google drive download link

file = open(os.getcwd() + pdf_files_url + "Find_the_Phone_Number.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(file)

pattern = r"\d{3}"
pattern2 = r"\d{3}.\d{3}.\d{4}"
all_text = ""

for n in range(pdf_reader.numPages):
    page = pdf_reader.getPage(n)
    page_text = page.extract_text()
    all_text = all_text + " " + page_text

for match in re.finditer(pattern, all_text):
    print(match)

print(all_text[43908 : 43908 + 20])

match = re.search(pattern2, all_text)
print(match.group())


###################################################################################################################################################
