from flask import Flask, jsonify, render_template, request, redirect
from components.staticFilesFunction import sendJsFile, sendUploadedFile, sendWatermarkedFile, sendCssFile, sendFontFile
from components.imageWatermarkFunctions import createWatermarkFunc

app = Flask(__name__)

#HOMEPAGE
@app.route('/')
def index():
    return render_template('home.html')

#CREATE WATERMARK
@app.route('/watermark/create', methods=["POST"])
def createWatermark():
    return createWatermarkFunc()
        
#STATIC FILES
#SEND WATERMARKED IMAGE
@app.route('/watermarked')
def sendWatermarkedImages():
    return sendWatermarkedFile()

#JS FILES
@app.route('/static/js')
def sendJs():
   return sendJsFile()

#CSS FILES
@app.route('/static/css')
def sendCss():
   return sendCssFile()

#FONT FILES
@app.route('/static/fonts')
def sendFont():
   return sendFontFile()

if __name__ == '__main__':
    app.run(debug=True)