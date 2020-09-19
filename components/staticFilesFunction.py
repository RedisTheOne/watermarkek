from flask import send_from_directory, send_file, request
import os

def sendMainJs():
    return send_from_directory('js', 'main.js')

def sendUploadedFile():
    try:
        img_name = request.args.get('image')
        return send_file(os.path.join(os.getcwd(), 'uploadedImages', img_name))
    except:
        return send_file(os.path.join(os.getcwd(), 'images', 'not_found_img.jpg'))

def sendWatermarkedFile():
    try:
        img_name = request.args.get('image')
        return send_file(os.path.join(os.getcwd(), 'watermarkedImages', img_name))
    except:
        return send_file(os.path.join(os.getcwd(), 'images', 'not_found_img.jpg'))