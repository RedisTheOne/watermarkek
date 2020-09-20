from flask import request, redirect, render_template
from uuid import uuid4
import os

#UPLOAD THE IMAGE FROM WEB TO THE SERVER
def uploadImageFromWebToServer():
    image = request.files["image"]
    ext = os.path.splitext(image.filename)[len(os.path.splitext(image.filename)) - 1]
    name = str(uuid4()) + ext
    image.save(os.path.join('./uploadedImages', name))
    return name