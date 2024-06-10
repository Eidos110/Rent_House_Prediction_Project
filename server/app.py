from flask import Flask, request, jsonify
import utils


app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'location' : utils.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response



@app.route('/predict_house_rent', methods=['GET', 'POST'])
def predict_house_rent():
    bhk = int(request.form['bhk'])
    size = float(request.form['size'])
    city = request.form['city']
    bathroom = int(request.form['bathroom'])

    response = jsonify({
        'estimated_price' : utils.get_estimate_price(city,bhk,size,bathroom)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response




if __name__ == "__main__":
    utils.load_saved_artifacts()
    app.run(host='0.0.0.0', port=8080)