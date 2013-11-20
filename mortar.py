from flask import Flask
from flask import render_template
from string import replace
from string import split
import urllib2
from xml.dom.minidom import parseString
import csv
import sys

app = Flask(__name__)

# prints out contents of file
@app.route('/')
def index():
	mortarrecs=None
	rows = []
	with open('initial_result.tsv', 'rb') as f:
    		mortarrecs = csv.reader(f, delimiter='\t', quotechar="|")
		for row in mortarrecs:
			rows.append(row)
			playlistId = [row[1].replace('mgid:uma:videolist:mtv.com:','').split(',')]
			recsId = [row[2].replace('mgid:uma:videolist:mtv.com:','').split(',')]
			for l in playlistId:
				for i in l:
					url = 'http://api.mtv.com/api/c0K1gE5tQgoB/articles/' + str(i) + '/videos'
					file = urllib2.urlopen(url)
					data = file.read()
					file.close()
					dom = parseString(data)
					pTitle = dom.getElementsByTagName("headline")[0].toxml().replace('<headline>','').replace('</headline>','')
		return render_template('index.html', rows=rows, pTitle=pTitle) 


if __name__ == '__main__':
    app.run(debug=True)


