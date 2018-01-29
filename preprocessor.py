from eml import eml_to_json
from html_to_txtimg import extract
from dict_to_csv import write_csv
from image_to_text import get_text
from attach_to_text import extract_attach
import os
import csv
import re

dir = 'test_mails'
# batch_size = '10'

def get_from_email(text):
    # print text
    email = re.search("<.+@.+>", text)
    return email.group()[1:-1]

def remove_text_links(text):
    text = re.sub(r'<http:\/\/.*[\r\n]*.*>', '', text, flags=re.MULTILINE)
    return text

def strip_spaces(text):
    return re.sub('(\s|\n)+', ' ', text).strip()

def get_filename(text_file):
    l = len(text_file)
    for i in range(l-1,0,-1):
		if(text_file[i])=='.':
			return text_file[:i]+'.txt'
    return '.txt'

data = []
c=0
x = ['1517065472_6804','1517065472_8279']
# for filename in os.listdir(dir):
directories = os.listdir(dir)
for filename in x:

# for i in range(1000,2000,20):
    # filename = directories[i]
    print str(c+1)+": "+filename
    email = eml_to_json(dir+"/"+filename)
    body, image_links = extract(email['html'])

    eml_data = {}
    # eml_data['from'] = get_from_email(email['from'])
    eml_data['from'] = ""
    eml_data['subject'] = email['subject']


    eml_data['attachment'] = ""
    # try:
    # print email['files']
    try:
        for attachment in email['files'].keys():
            # print email['files'][attachment][0]
            eml_data['attachment'] += ' '+extract_attach('attachments/'+get_filename(email['files'][attachment][0]))
            eml_data['attachment'] = strip_spaces(eml_data['attachment'])
        # print "attach "
    except:
        pass
    # except:
        # pass
    # print eml_data['attachment']

    # print email['text']
    # print remove_text_links(email['text'])
    eml_data['body'] =  body + remove_text_links(unicode(email['text'],errors='ignore'))
    # print remove_text_links(email['text'])
    # break
    eml_data['label'] = 0

    image_text = ""
    for image_link in image_links:
        image_text = image_text + ' ' + get_text(image_link)

    eml_data['body'] += image_text
    eml_data['body'] = strip_spaces(eml_data['body'].encode('ascii', 'ignore').decode('ascii'))
    # print eml_data['body']
    # break
    write_csv(eml_data,'test_final.csv')
    data.append(eml_data)
    c = c+1

# print data
# email = eml_to_json(dir+"/"+'1515580207_2861')

# employ_eml_data = open('email_eml_data.csv', 'w')
# # create the csv writer object
write_csv(data,'test_final.csv')
# for i in range(batch_size,len(data),batch_size):
#     write_csv(data[i:min(len(data),i+batch_size)],'ham.csv')
