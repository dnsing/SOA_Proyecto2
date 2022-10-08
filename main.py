import os
import threading
import subprocess
import time

# threads functions
def webAppThread():
    os.system("cd webApp && docker build -f Dockerfile -t web-app . && minikube image load web-app:latest && kubectl create --filename deployment.yaml && kubectl expose deployment web-app-deploy --type=NodePort --port=8000 && minikube service web-app-deploy")

def imageAnalizerThread():
    # cambiar
    os.system("cd calcAnalyzer && docker build -f Dockerfile -t calc-app . && minikube image load calc-app:latest && kubectl create --filename deployment.yaml && kubectl expose deployment calc-app-deploy --type=NodePort --port=9000 && minikube service calc-app-deploy --url")

def databaseWriterThread():
    os.system("cd databaseWriter && docker build -f Dockerfile -t writer-app . && minikube image load writer-app:latest && kubectl create --filename deployment.yaml && kubectl expose deployment writer-app-deploy --type=NodePort --port=10000 && minikube service writer-app-deploy --url")
    
def databaseReaderThread():
    os.system("cd databaseReader && docker build -f Dockerfile -t reader-app . && minikube image load reader-app:latest && kubectl create --filename deployment.yaml && kubectl expose deployment reader-app-deploy --type=NodePort --port=11000 && minikube service reader-app-deploy --url")

# code checker
print("----------Code Check-------------")
print("----------webApp-------------")
os.system("cd webApp && pylint webApp.py & pause")
print("----------imageAnalyzer-------------")
os.system("cd calcAnalyzer && pylint calc.py & pause") #cambiar
print("----------databaseWriter-------------")
os.system("cd databaseWriter && pylint databaseWriter.py & pause")
print("----------databaseReader-------------")
os.system("cd databaseReader && pylint databaseReader.py & pause")

# deleting existing k8s and starting a new one
print("Deleting minikube")
os.system("minikube delete --all")
print("Starting minikube in docker")
os.system("minikube start --driver=docker")

# threads 
webApp = threading.Thread(target=webAppThread)
imageAnalizer = threading.Thread(target=imageAnalizerThread)
databaseWriter = threading.Thread(target=databaseWriterThread)
databaseReader = threading.Thread(target=databaseReaderThread)

webApp.start()
imageAnalizer.start()
databaseWriter.start()
databaseReader.start()

webApp.join()
imageAnalizer.join()
databaseWriter.join()
databaseReader.join()

