import flask
from flask import Flask, render_template, url_for, request, send_file
# from flask_socketio import SocketIO, emit, join_room, leave_room
from matplotlib.figure import Figure
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
                final_pred = None
                #Preprocess the image: set the image to 28x28 shape
                #Access the image
                draw = request.form['url']

                #Removing the useless part of the url.
                draw = draw[init_Base64:]
                #Decoding
                draw_decoded = base64.b64decode(draw)
                image = np.asarray(bytearray(draw_decoded), dtype="uint8")
                image = cv2.imdecode(image, cv2.IMREAD_COLOR)

                #Resizing and reshaping to keep the ratio.
                resized = cv2.resize(image, (28,28), interpolation = cv2.INTER_AREA)
                vect = np.asarray(resized, dtype="uint8")
                # vect = vect.reshape(1, 1, 28, 28).astype('float32')

                #Launch prediction
                my_prediction = [np.random.random(6)]
                #Getting the index of the maximum prediction
                index = np.argmax(my_prediction[0])

                #Associating the index and its value within the dictionnary
                final_pred = index

                # encode
                # fig = Figure()
                # ax = fig.subplots()
                # ax.imshow(vect)
                # ax.plot()
                cv2.imwrite('static/images/input.png', image)
                cv2.imwrite('static/images/output.png', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

                # buf = io.BytesIO()
                # fig.savefig(buf, format="png")
                # data = base64.b64encode(buf.getbuffer()).decode("ascii")

                # is_success, buffer = cv2.imencode(".png", vect)
                # io_buf = io.BytesIO(buffer)
                # data = base64.b64encode(buffer.getbuffer()).decode("ascii")

                # html_code = f"<img src='data:image/png;base64,{data}'/>"


        return render_template('results.html', prediction=final_pred)



if __name__ == '__main__':
	app.run(debug=True)
