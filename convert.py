import os
from eml import eml_to_json
dir = 'spam_mails'

for filename in os.listdir(dir):
    email = eml_to_json(dir+"/"+filename)
