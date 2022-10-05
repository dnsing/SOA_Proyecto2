from flask import Flask, render_template, request
import requests
import json
import ast

def getSuma(numero1, numero2):
       if numero1 != '' and numero2 != '':
              return int(numero1) + int(numero2)
       else:
              return ''

app = Flask(__name__,template_folder='../template')
@app.route("/sum", methods = ['POST', 'GET'])
def sum():
       dict_resquest = ast.literal_eval(request.get_data().decode('utf-8'))
       print(dict_resquest)
       suma = getSuma(dict_resquest['numero_1'], dict_resquest["numero_2"])
       print("suma es : " + str(suma))
       requests.post("http://writer-app-deploy:10000/write", json=suma)

       result = str(suma)
                     
       return result
       
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=9000)
