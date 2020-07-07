#!python3
#Usage: copy a list with emails and phone numbers and then run the code and then when you use paste, it will only display
#the emails and phone numbers found in the document
import re
import pyperclip
#Create a regex for phone numbers
PhoneRegex = re.compile(r'''
#514-123-4123, 555-0000, (514) 123-1234, 555-000 ext 1234, ext. 1234, x 1234
(
((\d\d\d) | (\(\d\d\d\d\)))? #area code first or optional
(\s|-)                  #first dash or seperator
\d\d\d                  #first 3 digits of numbers
-                       #second seperator or dash
\d\d\d\d                        #last 4 digits
(((ext(\.)?\s)|x)               #extension word-part
 (\d{2,5}))?               #extension number type
)
''', re.VERBOSE)
#Create Regex for email addresses
EmailRegex = re.compile(r'''
# some.+thing@(\d{2,5})))?.com

[a-zA-Z0-9_.+]+    #name part we have to create our own char class. range of everything and we added underscore, plus and period
@   # @ symbol
[a-zA-Z0-9_.+]+ #domain part - same as name part
''', re.VERBOSE)
#Get the text off the clipboard
text = pyperclip.paste()

#Extract the phone numbers/emails from the text
ExtractedPhone = PhoneRegex.findall(text)
ExtractedEmail = EmailRegex.findall(text)
AllPhoneNumbers = []
for phonenumbers in ExtractedPhone:
    AllPhoneNumbers.append(phonenumbers[0]) #we only want the first string in the tuple for numers bc thats the full number
print(ExtractedEmail)
print(AllPhoneNumbers)
#Extract the email/phones to the clipboard
results = '\n'.join(AllPhoneNumbers) + '\n' + '\n'.join(ExtractedEmail)#this is where you change the format of how you want it displayed when you paste
pyperclip.copy(results)