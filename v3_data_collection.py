#this program will scrape for emails and us/canadians phone numbers in a given text
#! python3

import re
import os
import pdftotext

#this regex identifies and us/canadian phone number

regex_phone = re.compile(r"""
(
((\d\d\d) | (\(\d\d\d\)) | (\(\d\d\d\) ))?    #ZIP CODE AREA opt.
(\s|-)                                      #SEPARATOR 1
\d\d\d                                        #3 NUM GROUP
(\s|-)                                      #SEPARATOR 2
\d\d\d\d                                      #4 NUM GROUP
((ext(\.)?\s|x?)                               #EXTENSION word opt.
(\d{2,5}))?                                   #EXTENSION number opt.
)
"""
, re.VERBOSE)

#this regex identifies an email

regex_email = re.compile(r"""
[a-zA-Z0-9_.+]+                                 #part1  I made this ((\w+) | (\w+\.\w+)) but it's better to use what's running now for cleaner reading
\@                                                # at sign @
[a-zA-Z0-9_.+]+                                    #part2
#\.                                                #dot .
#(\w+)                                             #part 3
#\.?                                                  
#(\w+)?

""",re.VERBOSE)

#We open a given pdf to analyze

with open("/home/simone/examplePhoneEmailDirectory.pdf","rb") as wrk: #rb READ BINARY OR -> UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb5 in position 11: invalid start byte
    pdf = pdftotext.PDF(wrk)

#We create the string variable to parse with regex expressions
pdf_final = ""

for page in pdf:
    pdf_final = pdf_final + str(page)
    
#we search for phone numbers and emails
mo_phone = regex_phone.findall(pdf_final)
mo_mail = regex_email.findall(pdf_final)
#we create a cleaner output for phone findall 
new_mo_phone = []
#
for p_numbers in mo_phone: #for clear phone number viewing: findall() returns a list of tuples we need to iterate each tuple and return the first element of it so: tuple[0]
    new_mo_phone.append(p_numbers[0])
#we create a list by joining two lists
end_document = '\n'.join(new_mo_phone) + '\n' + '\n'.join(mo_mail)

print(end_document)