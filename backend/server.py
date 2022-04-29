from flask import Flask, send_file, request
from google.cloud import bigquery
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:/Users/jason/Documents/analyzequicker-bigquery-sa.json'

app = Flask(__name__)

@app.route("/query",methods = ['POST'])
def hello_world():
    client = bigquery.Client()

    # form = request.form
    # parameters = {}
    # for key in form.keys():
    #     parameters[key] = form[key]

    # return parameters

    limit = request.form['limit']

    query = """
        SELECT subject AS subject, COUNT(*) AS num_duplicates
        FROM bigquery-public-data.github_repos.commits
        GROUP BY subject 
        ORDER BY num_duplicates 
        DESC LIMIT {limit} 
    """.format(limit=limit)

    # return client.query(query).to_dataframe().to_json()

    client.query(query).to_dataframe().to_excel('test.xlsx',sheet_name='Sheet1',index=False)

    return send_file('test.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
