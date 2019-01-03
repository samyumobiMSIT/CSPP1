#Open and prints the URL
#import urllib.request
#url = "file:///E:/Cspp/CSPP1-Remedial/CSPP-1Week1Exam/webpage5.html"
#request = urllib.request.Request(url)
#response = urllib.request.urlopen(request)
#print (response.read())
#print(request)

#Print Image URL
import urllib.request
from urllib.request import urlopen
from PIL import Image
url = "file:///E:/Cspp/CSPP1-Remedial/CSPP-1Week1Exam/webpage5.html"
image = Image.open(urllib.request.urlopen(url))
print (image)

#count no. of images in website
total  = 0
page   = urlopen(url).readlines()
for line in page:
    hit = re.findall('<img.*?>', str(line))
    total += len(hit)
    print('{0} Images total: {1}'.format(url, total))

import urllib.request
import re
import sys

def fetchHTML(url):
	urlOpened = urllib.request.urlopen(url)
	htmlBytes = urlOpened.read()
	htmlString = htmlBytes.decode("utf8")
	urlOpened.close()
	return htmlString
