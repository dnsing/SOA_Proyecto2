# pylint: disable=bad-indentation, missing-module-docstring,unspecified-encoding, trailing-whitespace, missing-function-docstring, invalid-name, missing-timeout, consider-using-enumerate, line-too-long, no-else-return  
import sys
import base64
import json
from datetime import date
import requests
from flask import Flask, render_template, request


def images2base64(imagelist):
   """
   Method for converting image to base64.
   
   :imagelist: images list 
   :return: base64 of multiple images 
   """
   base64_list={}
   for i in range(0,len(imagelist)):
      image_b64 = base64.b64encode(imagelist[i].read()).decode('utf-8')
      base64_list[imagelist[i].filename]= str(image_b64)

   return base64_list

app = Flask(__name__,template_folder='template')
@app.route('/')
def main():
   # main window render
   return render_template('index.html')
   
   
@app.route("/result", methods = ['POST', 'GET'])
def uploadImages():
   """
   Method for uploading images.
   
   :return: rendered table with response
   """
   # sends data to the analizer 
   if request.form['submit_data'] == "Analizar":
      imagelist = request.files.getlist("image")  # get file
      base64_list=images2base64(imagelist)

      results = requests.post("http://reader-app-deploy:11000/read", json="send data").json()
      if str(date.today()) not in results:
         if len(base64_list)==10:
            data = requests.post("http://analyzer-app-deploy:9000/calc", json=json.dumps(base64_list))
            sys.stdout.flush()
            return render_template('index.html', texto = data.text)
         else:
            return render_template('index.html', texto = "Por favor ingrese 10 imagenes")
      else:
         return render_template('index.html', texto = "Resultados ya existentes para " + str(date.today()))
   else:
      return render_template('index.html')

@app.route("/result1", methods = ['POST', 'GET'])          
def updateTable():
   """
   Method for updating the table.
    
   :return: rendered table with updated table 
   """
   if request.form['results_button'] == "Desplegar tabla":
      print("reading data from webapp")
      results = requests.post("http://reader-app-deploy:11000/read", json="send data")
      data=results.json()
      dates = data.keys()
      row_headers = list(list(data.values())[0].values())[0].keys()
      print(data)
      print(dates)
      print(row_headers)
      sys.stdout.flush()
      return render_template('index.html', dates=dates, row_headers=row_headers, mfp_data=data)
   else:
      return render_template('index.html')


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8000, debug=True)
