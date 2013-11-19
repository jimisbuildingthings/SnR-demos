from flask import Flask
import csv

app = Flask(__name__)


@app.route('/')
def index():
	mortarrecs=None
	rows = []
	with open('initial_result.tsv', 'rb') as f:
		print 'x'
		mortarrecs = csv.reader(f, delimiter=' ', quotechar="|")
		for row in mortarrecs:
   			print rows.append(row)
	return str(rows)


if __name__ == '__main__':
    app.run(debug=True)