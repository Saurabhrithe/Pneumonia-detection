
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# main driver function
if __name__ == '__main__':
	app.run()
