# pylint: disable=bad-indentation, missing-module-docstring,unspecified-encoding, trailing-whitespace, invalid-name, unused-import  
import sys
import json

from flask import Flask, request

def readFile():
       """
       Method for reading json from file.

       :return: json data 
       """ 
       with open('/db/data/localDatabase.txt', 'r+') as file:
              file_data = json.load(file)
       return file_data


app = Flask(__name__)
@app.route("/read", methods = ['POST', 'GET'])
def reader():
       """
       Method for reading Database.

       :return: database content
       """ 
       print("Reader init")
       databaseContent = readFile()
       print(databaseContent)
       print("Loaded from localDatabase.txt")
       sys.stdout.flush()
       return databaseContent
       
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=11000)
