from flask import Flask,request,jsonify
# import predictor
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route("/",methods=["POST"])
def home():
    return jsonify()

@app.route("/predict",methods=["POST"])
def predict():
    # data=request.get_json(force=True)
    # features = data.get('features',[])
    
    # # prediction = predictor.predictor(features)
    # response ={
    #     'prediction':prediction,
    #     'recieved_feats':features
    # }
    return jsonify({
        'test':"test",
        'recieved_feats':"test"
    })

@app.route('/favicon.ico')
def favicon():
    return jsonify(success=True)



if __name__ == 'main':
    app.run(debug=True)