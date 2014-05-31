import urllib2
from bs4 import BeautifulSoup


#cap_source = 'http://a8.akadl.mtvnservices.com/9950/mtvnorigin/gsp.comedystor/com/tve/keyandpeele/season03/0312/HDKAP312L/keyandpeele_03_0312_act1.dfxp.xml'
cap_source = raw_input('Give me a caption file, please: ')
f = urllib2.urlopen(cap_source)
data = f.read()
f.close()
soup = BeautifulSoup(data)
for i in soup.findAll('br'):
    i.replaceWith(' ')
soup = soup.find('div').get_text()
s = soup.encode(encoding='ascii',errors='ignore')
print s

