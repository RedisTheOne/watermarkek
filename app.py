from flask import Flask, jsonify, render_template, request, redirect
from components.staticFilesFunction import sendMainJs, sendUploadedFile, sendWatermarkedFile
from components.uploadImageFunctions import uploadImageFromWebToServer, addTextView
from components.imageWatermarkFunctions import createWatermarkFunc

app = Flask(__name__)

#HOMEPAGE
@app.route('/')
def index():
    return render_template('home.html')

#UPLOAD IMAGE POST METHOD
@app.route('/upload-image', methods=["POST"])
def uploadImage():
    return uploadImageFromWebToServer(request)

#CREATE WATERMARK
@app.route('/watermark/create', methods=["POST"])
def createWatermark():
    return createWatermarkFunc()

#RENDER THe VIEW TO ADD TEXT 
@app.route('/edit')
def editImage():
    addTextView()
        

#STATIC FILES
#SEND UPLOADED IMAGE
@app.route('/uploads')
def sendUploadedImage():
    return sendUploadedFile()

@app.route('/watermarked')
def sendWatermarkedImages():
    return sendWatermarkedFile()

#JS FILES
@app.route('/static/js/main')
def sendJs():
   return sendMainJs()

if __name__ == '__main__':
    app.run(debug=True)