from flask import Flask, render_template, request
import requests
import json
import ast

def writeFile(analysis_result):
       with open('localDatabase.txt', 'a') as f:
              f.write("El resultado de la suma es: " + analysis_result + "\n")



app = Flask(__name__,template_folder='../template')
@app.route("/write", methods = ['POST', 'GET'])
def writer():
       print("Writer init")
       writeFile(request.get_data().decode('utf-8'))
       print("Saved in localDatabase.txt")
       return 'done'
       
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=10000)
