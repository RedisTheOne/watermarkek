from flask import Blueprint
from components.imageWatermarkFunctions import createWatermarkFunc

imagesBlueprint = Blueprint('images', __name__, url_prefix='/images')

@imagesBlueprint.route('/watermark/create', methods=["POST"])
def createWatermark():
    return createWatermarkFunc()