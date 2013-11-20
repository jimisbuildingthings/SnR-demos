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
			newRow = []
			userId = row[0]
			content = []
			recs = []
			newRow.append(userId)
			contentItems = [row[1].replace('mgid:uma:videolist:mtv.com:','').split(',')]
			recsItems = [row[2].replace('mgid:uma:videolist:mtv.com:','').split(',')]
			for l in contentItems:
				for i in l:
					url = 'http://api.mtv.com/api/c0K1gE5tQgoB/articles/' + str(i) + '/videos'
					f = urllib2.urlopen(url)
					data = f.read()
					f.close()
					dom = parseString(data)
					cTitle = dom.getElementsByTagName("headline")[0].firstChild.nodeValue
					content.append(cTitle)
			newRow.append(content)
			for l in recsItems:
				for i in l:
					url = 'http://api.mtv.com/api/c0K1gE5tQgoB/articles/' + str(i) + '/videos'
					f = urllib2.urlopen(url)
					data = f.read()
					f.close()
					dom = parseString(data)
					rTitle = dom.getElementsByTagName("headline")[0].firstChild.nodeValue
					recs.append(rTitle)
			newRow.append(recs)
			rows.append(newRow)
		return render_template('index.html', rows=rows) 


if __name__ == '__main__':
    app.run(debug=True)


