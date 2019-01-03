import re
from urllib.request import urlopen

def get_image(url):

    total  = 0
    page   = urlopen(url).readlines()

    for line in page:

        hit   = re.findall('<img.*?>', str(line))
        total += len(hit)

    print('{0} Images total: {1}'.format(url, total))

get_image("http://google.com")