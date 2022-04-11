#! python3

import pyperclip
import re



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

regex_email = re.compile(r"""
[a-zA-Z0-9_.+]+                                 #part1 simone.benati@outlook.com.com I made this ((\w+) | (\w+\.\w+)) but guide uses
\@                                                # at sign @
[a-zA-Z0-9_.+]+                                    #part2
#\.                                                #dot .
#(\w+)                                             #part 3
#\.?                                                  
#(\w+)?

""",re.VERBOSE)

document = pyperclip.paste()

mo_phone = regex_phone.findall(document)
mo_mail = regex_email.findall(document)

new_mo_phone = []

for p_numbers in mo_phone: #for clear phone number viewing: findall() returns a list of tuples we need to iterate each tuple and return the first element of it so: tuple[0]
    new_mo_phone.append(p_numbers[0])

parsed_document = '\n'.join(new_mo_phone) + '\n' + '\n'.join(mo_mail)


pyperclip.copy(parsed_document)
print(parsed_document)