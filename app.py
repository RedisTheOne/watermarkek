from flask import Flask, jsonify, render_template, request, redirect
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


if __name__ == '__main__':
    app.run(debug=True)