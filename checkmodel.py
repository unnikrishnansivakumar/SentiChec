from keras.models import model_from_json
import matplotlib.pyplot as plt


data = plt.imread('outfile.jpg')

actdata = data.reshape(1,1,48,48)

json_file = open('model.json', 'r')

loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
ss = loaded_model.predict(actdata)

label_map = ['Anger', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
print ss

