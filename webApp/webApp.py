from flask import Flask, render_template, request
from test1 import test
from calcAnalyzer import calc
import requests
import json
import ast

def helper(str):
   return str

app = Flask(__name__,template_folder='../template')
@app.route('/')
def main():
   return render_template('index.html')
   # return test.getDatos()
   
   
@app.route("/result", methods = ['POST', 'GET'])
def setNumbers():
   output = request.form.to_dict()
   requests.post("http://127.0.0.1:9000/sum", json=output)

   suma = helper(request.get_data().decode('utf-8'))
   print(suma)
   # if suma != '':
   #    suma1 = suma
   #    print("ta la suma " + suma)
   # else:
   #    suma = suma1
   #    # suma = ast.literal_eval(suma.decode('utf-8'))
   # suma = suma1
   return render_template('index.html', suma = request.get_data().decode('utf-8'))
              
      #  json_loads = json.loads(suma)
      #  print(json_loads)
          
      

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8000)
