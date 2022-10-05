from unittest import result
from flask import Flask, render_template, request
import requests

def helper(str):
   return str

app = Flask(__name__,template_folder='template')
@app.route('/')
def main():
   # main window render
   return render_template('index.html')
   
   
@app.route("/result", methods = ['POST', 'GET'])
def setNumbers():
   # sends data to the analizer 
   if request.form['submit_data'] == "send data":
      output = request.form.to_dict()
      suma_result = requests.post("http://calc-app-deploy:9000/sum", json=output)
      # print(suma_result.text)
      return render_template('index.html', suma = suma_result.text)
   else:
      return render_template('index.html')

@app.route("/result1", methods = ['POST', 'GET'])          
def getResults():
   if request.form['results_button'] == "Do Something":
      print("reading data from webapp")
      results = requests.post("http://reader-app-deploy:11000/read", json="send data")
      return render_template('index.html', results = results.text)
   else:
      return render_template('index.html')


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8000, debug=True)
