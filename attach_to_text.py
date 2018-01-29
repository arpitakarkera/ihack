import textract
import re

# def extract_attach(filename):
# 	text = textract.process(filename)
# 	if ".csv" in filename:
# 		return re.sub('[^a-z\ \']+', " ", text)
# 	else:
# 		text = text.lower()
# 		return re.sub('[^a-z\ \']+', " ", text)

def extract_attach(file):
	# print file
	text = open(file,'r')
	return text.read()
