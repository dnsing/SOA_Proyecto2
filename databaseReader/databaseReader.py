from flask import Flask, render_template, request

def readFile():
       # cambiar path a generico
       with open('../databaseWriter/localDatabase.txt') as f:
              content = f.readlines()

       for line in content:
              print(line)
       return content


app = Flask(__name__,template_folder='../template')
@app.route("/read", methods = ['POST', 'GET'])
def reader():
       print("Reader init")
       databaseContent = readFile()
       # readFile(request.get_data().decode('utf-8'))
       print("Loaded from localDatabase.txt")
       return "\n".join(databaseContent)
       
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=11000)
