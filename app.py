from flask import Flask, render_template, url_for
import random

app = Flask(__name__)

@app.route('/') 
def index():
    images = [
        url_for('static', filename='gifs/cat1.gif'),
        url_for('static', filename='gifs/cat2.gif'),
        url_for('static', filename='gifs/cat3.gif'),
        url_for('static', filename='gifs/cat4.gif'),
        url_for('static', filename='gifs/cat5.gif'),
        url_for('static', filename='gifs/cat6.gif')
    ]
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
