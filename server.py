from flask import *
from PIL import Image
from io import BytesIO
from resizeimage import resizeimage
from keras.models import model_from_json
# from functions import *
import numpy as np
import base64

app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('index.html')

@app.route('/photoinc',methods = ['GET','POST'])
def process_photo():
	photodata = request.form['userInput']	
	im = Image.open(BytesIO(base64.b64decode(photodata[22:]))).convert('LA')
	cover = resizeimage.resize_cover(im, [48,48])
	datanp = np.array(cover)
	json_file = open('model.json', 'r')
	loaded_model_json = json_file.read()
	json_file.close()
	loaded_model = model_from_json(loaded_model_json)
	# print('loaded model')
	print (loaded_model.predict('datanp'))
	return jsonify('hahaha')


if __name__ == '__main__':
   app.run(port = 8000, debug = True)