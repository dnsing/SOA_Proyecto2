# pylint: disable=bad-indentation, missing-module-docstring,unspecified-encoding, trailing-whitespace, invalid-name, missing-timeout  
import json
import sys
import base64
import requests
from flask import Flask, request
import include.visionAPI as vi

app = Flask(__name__)
@app.route("/calc", methods = ['POST', 'GET'])
def calc():
       """
       Method for analyzing images.

       :return: text confirming analysis done
       """ 
       jsondata = request.get_json()
       b64_list = json.loads(jsondata)
       listresults={}
       for image in b64_list:
              imageResults=vi.visionAnalyze(base64.decodebytes(b64_list[image].encode("utf-8")))
              listresults[image]=imageResults
       print(listresults)
       sys.stdout.flush()
       requests.post("http://writer-app-deploy:10000/write", json=json.dumps(listresults))
   
       result = "Analisis listo"
                     
       return result
       
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=9000)
