import os, sys, json

# image_url = sys.argv[1]


def detect_text_uri(uri):
    """Detects text in the file on the Web.
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient.from_service_account_json('googlecreds.json')
    # client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    # print('Texts:')
    # print (texts)

    words = ""
    for text in texts:
        # print('eee ')
        # print('\n"{}"'.format(text.description))
        words = words + ' ' + text.description.strip()
        break
        # print(text.description)

        # vertices = (['({},{})'.format(vertex.x, vertex.y)
        #             for vertex in text.bounding_poly.vertices])

        # print('bounds: {}'.format(','.join(vertices)))
    
    # print (words)
    words = words.replace('\n',' ')
    return words


# words = detect_text_uri(image_url)
# words = words.replace('\n',' ')

# print(words)