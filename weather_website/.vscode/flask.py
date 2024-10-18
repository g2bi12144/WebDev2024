import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def query_weather_data(city):
    connection = sqlite3.connect('weather_data.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM WeatherData WHERE city = ?", (city,))
    data = cursor.fetchone()
    connection.close()
    return data

@app.route('/get_weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    data = query_weather_data(city)
    if data:
        return jsonify({
            'city': data[0],
            'country': data[1],
            'temperature': data[2],
            'humidity': data[3],
            'wind_speed': data[4],
            'condition': data[5]
        })
    else:
        return jsonify({'error': 'City not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)