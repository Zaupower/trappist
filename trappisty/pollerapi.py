from flask import Flask, jsonfy
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return "working webserver"

@app.route('/api/host/<string:host>', methods=['GET'])
def get_host(host):
    output= []
    with open('results.csv') as results:
        resultscsv = csv.reader(results)
        for row in resultscsv: 
            if row[1] == host:
                output.append({'hostname': row[1],
                                'timestamp': row[0],
                                'mib': row[2],
                                'output': row[3]},)
        return jsonfy(output)

app.run(debug-True)

