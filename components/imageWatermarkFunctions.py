from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from uuid import uuid4
from flask import jsonify, request
import os

def addWatermarkCentered(text, path):
    #IMAGE
    img = Image.open(path).convert("RGBA")
    img_width, img_height = img.size
    draw = ImageDraw.Draw(img, "RGBA")
    
    #TEXT
    font = ImageFont.truetype("font.ttf", int(img_width / 8))
    text_width, text_height = draw.textsize(text, font)
    draw.text(((img_width / 2) - (text_width / 2), (img_height / 2) - (text_height / 2)), text, fill=(255, 255, 255, 200), font=font)
    
    #SAVE
    new_path = str(uuid4()) + '.png'
    img.save('watermarkedImages/' + new_path)
    return new_path

def addWatermarkBottomLeft(text, path):
    #IMAGE
    img = Image.open(path).convert("RGBA")
    img_width, img_height = img.size
    draw = ImageDraw.Draw(img, "RGBA")
    
    #TEXT
    font = ImageFont.truetype("font.ttf", 200)
    text_width, text_height = draw.textsize(text, font)
    draw.text((20, (img_height - text_height) - 20), text, fill=(255, 255, 255, 200), font=font)
    
    #SAVE
    new_path =  str(uuid4()) + '.png'
    img.save('watermarkedImages/' + new_path)
    return new_path

def addWatermarkBottomRight(text, path):
    #IMAGE
    img = Image.open(path).convert("RGBA")
    img_width, img_height = img.size
    draw = ImageDraw.Draw(img, "RGBA")
    
    #TEXT
    font = ImageFont.truetype("font.ttf", 200)
    text_width, text_height = draw.textsize(text, font)
    draw.text(((img_width - text_width) - 20, (img_height - text_height) - 20), text, fill=(255, 255, 255, 200), font=font)
    
    #SAVE
    new_path = str(uuid4()) + '.png'
    img.save('watermarkedImages/' + new_path)
    return new_path

def addWatermarkTopRight(text, path):
    #IMAGE
    img = Image.open(path).convert("RGBA")
    img_width, img_height = img.size
    draw = ImageDraw.Draw(img, "RGBA")
    
    #TEXT
    font = ImageFont.truetype("font.ttf", 200)
    text_width, text_height = draw.textsize(text, font)
    draw.text(((img_width - text_width) - 20, 20), text, fill=(255, 255, 255, 200), font=font)

    #SAVE
    new_path = str(uuid4()) + '.png'
    img.save('watermarkedImages/' + new_path)
    return new_path

def addWatermarkTopLeft(text, path):
    #IMAGE
    img = Image.open(path).convert("RGBA")
    img_width, img_height = img.size
    draw = ImageDraw.Draw(img, "RGBA")

    #TEXT
    font = ImageFont.truetype("font.ttf", 200)
    text_width, text_height = draw.textsize(text, font)
    draw.text((20, 20), text, fill=(255, 255, 255, 200), font=font)
    
    #SAVE
    new_path = str(uuid4()) + '.png'
    img.save('watermarkedImages/' + new_path)
    return new_path

def createWatermarkFunc():
    body = request.get_json()
    text = body['text']
    image_name = body['imageName']
    watermark_position = body['watermarkPosition']

    if watermark_position == 'center':
        return jsonify(image=addWatermarkCentered(text, os.path.join(os.getcwd(), 'uploadedImages', image_name)))
    elif watermark_position == 'topLeft':
        return jsonify(image=addWatermarkTopLeft(text, os.path.join(os.getcwd(), 'uploadedImages', image_name)))
    elif watermark_position == 'topRight':
        return jsonify(image=addWatermarkTopRight(text, os.path.join(os.getcwd(), 'uploadedImages', image_name)))
    elif watermark_position == 'bottomLeft':
        return jsonify(image=addWatermarkBottomLeft(text, os.path.join(os.getcwd(), 'uploadedImages', image_name)))
    elif watermark_position == 'bottomRight':
        return jsonify(image=addWatermarkBottomRight(text, os.path.join(os.getcwd(), 'uploadedImages', image_name)))

## BODY EXAMPLE
# {
#     "text": "AAAAA",
#     "imageName": "220d9ca5-b628-45b3-990c-04ae523767e5.jpg",
#     "watermarkPosition": "center"
# }