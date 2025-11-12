from flask import Flask, render_template, url_for, request, Response
import os
from detect import Start
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pista')
def pista():
    return render_template('pistapage.html')

@app.route('/LiveStream')
def LiveStream():
    from detect_live import StartLive
    StartLive(0)
    return render_template('pistapage.html')

@app.route('/getData', methods=['GET', 'POST'])
def getData():
    if request.method == 'POST':
        File = request.form['file']
        File = File.replace('http://127.0.0.1:5000/', '')
        print(File)
        from detect import Start
        Start(File)
        
        return render_template('pistapage.html', output_image="http://127.0.0.1:5000/static/result.jpg", inputImage='http://127.0.0.1:5000/'+File)

@app.route('/execute', methods=['GET', 'POST'])
def execute():
    
    return render_template('pistapage.html')
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
