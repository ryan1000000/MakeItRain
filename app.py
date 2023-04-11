pip install flask
from flask import Flask, render_template, request
import update_feature_layer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update():
    update_feature_layer.update_maintenance_dates()
    return 'Field updated successfully'

if __name__ == '__main__':
    app.run(debug=True)
