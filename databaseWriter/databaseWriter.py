# pylint: disable=bad-indentation, missing-module-docstring,unspecified-encoding, trailing-whitespace, invalid-name  
import sys
import json
from datetime import date
from flask import Flask, request

def writeFile(analysis_result):
       """
       Method for writing json to file.

       :param analysis_result: json of the images analysis 
       """ 
       with open('/db/data/localDatabase.txt', 'r+') as file:
              file_data = json.load(file)
              print(analysis_result)
              file_data[str(date.today())]=analysis_result
              file.seek(0)
              json.dump(file_data, file, indent = 4)

app = Flask(__name__)
@app.route("/write", methods = ['POST', 'GET'])
def writer():
       """
       Method for writing to Database.

       :return: text confirming writing done
       """ 
       print("Writer init")
       writeFile(json.loads(request.get_json()))
       print("Saved in localDatabase.txt")
       sys.stdout.flush()
       return 'done'
       
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=10000)
