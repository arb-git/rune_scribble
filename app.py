import flask
from flask import Flask, render_template, url_for, request, send_file
import base64
import numpy as np
import cv2
from PIL import Image
import io

#Initialize the useless part of the base64 encoded image.
init_Base64 = 21

#Initializing new Flask instance. Find the html template in "templates".
app = flask.Flask(__name__, template_folder='templates', static_folder='static')

#First route : Render the initial drawing template
@app.route('/')
def home():
	return render_template('draw.html')


@app.route('/api/a', methods=['GET'])
def send_image(img):
    if request.method == 'GET':
        img = Image.fromarray(img.astype('uint8')) # convert arr to image

        file_object = io.BytesIO()   # create file in memory
        img.save(file_object, 'PNG') # save PNG in file in memory
        file_object.seek(0)          # move to beginning of file

        return send_file(file_object,  mimetype='image/png')


#Second route : Use our model to make prediction - render the results page.
@app.route('/predict', methods=['POST'])
def predict():
        if request.method == 'POST':
                #Access the image
                draw = request.form['url']

                #Removing the useless part of the url.
                draw = draw[init_Base64:]

                #Decoding
                draw_decoded = base64.b64decode(draw)
                image = np.asarray(bytearray(draw_decoded), dtype="uint8")
                image = cv2.imdecode(image, cv2.IMREAD_COLOR)


                #Associating the index and its value within the dictionnary
                final_pred = 0

                cv2.imwrite('static/images/input.png', image)
                cv2.imwrite('static/images/output.png', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

        return render_template('results.html', prediction=final_pred)



if __name__ == '__main__':
	app.run(debug=True)
