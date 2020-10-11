from flask import Flask
from components.blueprints.viewsBlueprint import viewsBlueprint
from components.blueprints.imagesBluepint import imagesBlueprint

app = Flask(__name__)

# BLUEPRINTS
app.register_blueprint(viewsBlueprint)
app.register_blueprint(imagesBlueprint)


if __name__ == '__main__':
    app.run(debug=True)