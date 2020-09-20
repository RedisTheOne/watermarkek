from flask import send_file, request, jsonify
import os

def sendJsFile():
    try:
        name = request.args.get('name')
        return send_file(os.path.join(os.getcwd(), 'static', 'js', name))
    except:
        return jsonify(status=False)

def sendCssFile():
    try:
        name = request.args.get('name')
        return send_file(os.path.join(os.getcwd(), 'static', 'css', name))
    except:
        return jsonify(status=False)

def sendFontFile():
    try:
        name = request.args.get('name')
        return send_file(os.path.join(os.getcwd(), 'static', 'fonts', name))
    except:
        return jsonify(status=False)

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