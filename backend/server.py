from flask import Flask, send_file
from google.cloud import bigquery
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:/Users/jason/Documents/analyzequicker-bigquery-sa.json'

app = Flask(__name__)

@app.route("/")
def hello_world():
    client = bigquery.Client()
    query = """
        SELECT subject AS subject, COUNT(*) AS num_duplicates
        FROM bigquery-public-data.github_repos.commits
        GROUP BY subject 
        ORDER BY num_duplicates 
        DESC LIMIT 10 
    """

    # return client.query(query).to_dataframe().to_html(index=False)

    client.query(query).to_dataframe().to_csv('test.csv',index=False)

    return send_file('test.csv', mimetype='text/csv')
    
    