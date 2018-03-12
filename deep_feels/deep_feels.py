# get predictions for each of your new texts
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import pickle
import json
from twitter import tweets
from flask import Flask
from flask import jsonify

# load the tokenizer and the model
with open("model/keras_tokenizer.pickle", "rb") as f:
   tokenizer = pickle.load(f)
 
model = load_model("model/yelp_sentiment_model.hdf5")
 
# replace with the data you want to classify
# newtexts = ["Your new data", "More new data", "This is terrible"]
 
# note that we shouldn't call "fit" on the tokenizer again
def predict(comments):
    sequences = tokenizer.texts_to_sequences(comments)
    data = pad_sequences(sequences, maxlen=300)
 
    # get predictions for each of your new texts
    predictions = model.predict(data)
    return predictions

app = Flask(__name__)

@app.route('/predict')
def get_prediction():
    statuses = tweets()
    predictions = predict(statuses)
    
    res = []
    for s, _ in enumerate(statuses):
        pred = {u"text": statuses[s], u"prediction": predictions[s].tolist()}
        res.append(json.dumps(pred))

    print(res)
    return jsonify(predictions = res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 80)
