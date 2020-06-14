# extracting mails and phone numbers from file

# replace name_and_mail.txt with your own text file name

import re
import pandas as pd

file = open('name_and_mail.txt', 'r')

mail_re = r'\s?(\w+[@]\w+[.]com)\s?'
phone_re = r'\s?([+]?[0-9]+?\s[0-9]{10})\s?'

# if there is no string matched in a certain line
# then re might return [] for that line
# to avoid that we will simply not append it during check

def get_mails(lines):
    mails = []
    for line in lines:
        x = re.findall(mail_re, line)
        if x != []: mails.append(x) 
    return mails

def get_phones(lines):
    phones = []
    for line in lines:
        x = re.findall(phone_re, line)
        if x != []: phones.append(x)
    return phones

lines = file.readlines()

mails = get_mails(lines)
phones = get_phones(lines)
print(mails)
print(phones)
