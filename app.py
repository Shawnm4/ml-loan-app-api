from flask import Flask,request,jsonify
import predictor
app = Flask(__name__)

@app.route("/")
def home():
    return "Goodbye World"

@app.route("/predict",methods=["POST"])
def predict():
    data=request.get_json(force=True)
    features = data.get('features',[])
    
    prediction = predictor.predictor(features)
    response ={
        'prediction':prediction,
        'recieved_feats':features
    }
    return jsonify(response)

if __name__ == 'main':
    app.run(debug=True)