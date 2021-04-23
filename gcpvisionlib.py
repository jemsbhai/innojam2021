import io
import os
import sys

# Imports the Google Cloud client library
from google.cloud import vision
# from google.cloud.vision import types

def describe(file_name):

    # Instantiates a client
    client = vision.ImageAnnotatorClient.from_service_account_json('googlecreds.json')

    # The name of the image file to annotate
    # file_name = sys.argv[1]

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    contents = ""

    print('Labels:')
    for label in labels:
        #print(label.description)
        contents = contents + " " + label.description


    print(contents)

    return contents