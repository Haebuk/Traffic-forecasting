import json
from flask import Flask, jsonify
from traffic.traffic_forecasting import TrafficForecasting
app = Flask(__name__)

@app.route('/traffic/forecast', methods=['POST'])
def traffic_forecasting():
    result = TrafficForecasting().predict()
    return jsonify(result)

if __name__ == '__main__':
    app.run()