from flask import request, redirect, request
from uuid import uuid4
import os

#UPLOAD THE IMAGE FROM WEB TO THE SERVER
def uploadImageFromWebToServer():
    image = request.files["image"]
    ext = os.path.splitext(image.filename)[len(os.path.splitext(image.filename)) - 1]
    image.save(os.path.join('./uploadedImages', str(uuid4()) + ext))
    return redirect('/')

#ADD TEXT VIEW
def addTextView():
    return ''