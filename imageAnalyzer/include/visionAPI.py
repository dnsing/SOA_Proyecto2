import os

from google.cloud import vision

KEY = './key.json'

os.environ['GOOGLE_APPLICATION_CREDENTIALS']=KEY

vision_client = vision.ImageAnnotatorClient()

def visionAnalyze(content):
    """
    Method for connecting to Vision API and analyze images.

    :param content: image to analyze 
    :return: json of the emotions analysis
    """ 
    
    image = vision.Image(content=content)
    response = vision_client.face_detection(image=image)
    faces = response.face_annotations
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    i=0
    result={}
    for face in faces:
        result={  'anger': likelihood_name[face.anger_likelihood],
                  'joy': likelihood_name[face.joy_likelihood],
                  'sorrow': likelihood_name[face.sorrow_likelihood],
                  'surprise': likelihood_name[face.surprise_likelihood]
                }
    return result
