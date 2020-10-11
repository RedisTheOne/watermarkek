from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from uuid import uuid4
from flask import jsonify, request
from .uploadImageFunctions import uploadImageFromWebToServer
import os

def checkIfPathsExist():
    #CHECK IF OUR PATHS EXISTS
    if os.path.exists('static/uploadedImages') == False:
        os.mkdir('static/uploadedImages')
    if os.path.exists('static/watermarkedImages') == False:
        os.mkdir('static/watermarkedImages')
    
def addWatermarkCentered(text, path, size):
    #IMAGE
    img = Image.open(path).convert("RGBA")
    img_width, img_height = img.size
    draw = ImageDraw.Draw(img, "RGBA")
    sub_val = 13
    if size == 'l':
        sub_val = 6
    elif size == 'm':
        sub_val = 8
    
    #TEXT
    font = ImageFont.truetype("font.ttf", int(img_width / sub_val))
    text_width, text_height = draw.textsize(text, font)
    draw.text(((img_width / 2) - (text_width / 2), (img_height / 2) - (text_height / 2)), text, fill=(255, 255, 255, 200), font=font)
    
    #SAVE
    new_path = str(uuid4()) + '.png'
    img.save('static/watermarkedImages/' + new_path)
    return new_path

def addWatermarkBottomLeft(text, path, size):
    #IMAGE
    img = Image.open(path).convert("RGBA")
    img_width, img_height = img.size
    draw = ImageDraw.Draw(img, "RGBA")
    sub_val = 13
    if size == 'l':
        sub_val = 6
    elif size == 'm':
        sub_val = 8
    
    #TEXT
    font = ImageFont.truetype("font.ttf", int(img_width / sub_val))
    text_width, text_height = draw.textsize(text, font)
    draw.text((20, (img_height - text_height) - 20), text, fill=(255, 255, 255, 200), font=font)
    
    #SAVE
    new_path =  str(uuid4()) + '.png'
    img.save('static/watermarkedImages/' + new_path)
    return new_path

def addWatermarkBottomRight(text, path, size):
    #IMAGE
    img = Image.open(path).convert("RGBA")
    img_width, img_height = img.size
    draw = ImageDraw.Draw(img, "RGBA")
    sub_val = 13
    if size == 'l':
        sub_val = 6
    elif size == 'm':
        sub_val = 8
    
    #TEXT
    font = ImageFont.truetype("font.ttf", int(img_width / sub_val))
    text_width, text_height = draw.textsize(text, font)
    draw.text(((img_width - text_width) - 20, (img_height - text_height) - 20), text, fill=(255, 255, 255, 200), font=font)
    
    #SAVE
    new_path = str(uuid4()) + '.png'
    img.save('static/watermarkedImages/' + new_path)
    return new_path

def addWatermarkTopRight(text, path, size):
    #IMAGE
    img = Image.open(path).convert("RGBA")
    img_width, img_height = img.size
    draw = ImageDraw.Draw(img, "RGBA")
    sub_val = 13
    if size == 'l':
        sub_val = 6
    elif size == 'm':
        sub_val = 8
    
    #TEXT
    font = ImageFont.truetype("font.ttf", int(img_width / sub_val))
    text_width, text_height = draw.textsize(text, font)
    draw.text(((img_width - text_width) - 20, 20), text, fill=(255, 255, 255, 200), font=font)

    #SAVE
    new_path = str(uuid4()) + '.png'
    img.save('static/watermarkedImages/' + new_path)
    return new_path

def addWatermarkTopLeft(text, path, size):
    #IMAGE
    img = Image.open(path).convert("RGBA")
    img_width, img_height = img.size
    draw = ImageDraw.Draw(img, "RGBA")
    sub_val = 13
    if size == 'l':
        sub_val = 6
    elif size == 'm':
        sub_val = 8
    
    #TEXT
    font = ImageFont.truetype("font.ttf", int(img_width / sub_val))
    text_width, text_height = draw.textsize(text, font)
    draw.text((20, 20), text, fill=(255, 255, 255, 200), font=font)
    
    #SAVE
    new_path = str(uuid4()) + '.png'
    img.save('static/watermarkedImages/' + new_path)
    return new_path

def createWatermarkFunc():
    checkIfPathsExist()
    body = request.form
    text = body['text']
    image_name = uploadImageFromWebToServer()
    size = body['size']
    watermark_position = body['watermarkPosition']

    if watermark_position == 'center':
        img = image=addWatermarkCentered(text, os.path.join(os.getcwd(), 'static', 'uploadedImages', image_name), size)
        os.remove(os.path.join(os.getcwd(), 'static', 'uploadedImages', image_name))
        return jsonify(image=img)
    elif watermark_position == 'topLeft':
        img = addWatermarkTopLeft(text, os.path.join(os.getcwd(), 'static', 'uploadedImages', image_name), size)
        os.remove(os.path.join(os.getcwd(), 'static', 'uploadedImages', image_name))
        return jsonify(image=img)
    elif watermark_position == 'topRight':
        img = addWatermarkTopRight(text, os.path.join(os.getcwd(), 'static', 'uploadedImages', image_name), size)
        os.remove(os.path.join(os.getcwd(), 'static', 'uploadedImages', image_name))
        return jsonify(image=img)
    elif watermark_position == 'bottomLeft':
        img = addWatermarkBottomLeft(text, os.path.join(os.getcwd(), 'static', 'uploadedImages', image_name), size)
        os.remove(os.path.join(os.getcwd(),'static', 'uploadedImages', image_name))
        return jsonify(image=img)
    elif watermark_position == 'bottomRight':
        img = addWatermarkBottomRight(text, os.path.join(os.getcwd(), 'static', 'uploadedImages', image_name), size)
        os.remove(os.path.join(os.getcwd(), 'static', 'uploadedImages', image_name))
        return jsonify(image=img)
    else:
        return jsonify(status=False)

## BODY EXAMPLE
# {
#     "text": "AAAAA",
#     "imageName": "220d9ca5-b628-45b3-990c-04ae523767e5.jpg",
#     "watermarkPosition": "center/topLeft/topRight/bottomLeft/bottomRight",
#     "size": "sm/m/l",
#     "image": <file>    
# }