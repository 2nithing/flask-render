from flask import Flask,render_template, request
import weight_predict

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def hello():
    if request.method == 'POST':
        height = request.form['height']
        weight = weight_predict.prediction([[float(height)]])
        return render_template('index.html',weight = round(weight[0],2), height=height)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run()
