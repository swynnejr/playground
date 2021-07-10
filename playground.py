from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def index():
    return render_template("index.html",color = "blue", times=5)

#adding int: to <int:times> is the same as line 12
@app.route('/play/<int:times>')
def repeat_blocks(times):
    # times = int(times)
    return render_template("index.html", color = "green",times = times)

@app.route('/play/<int:times>/<color>')
def change_color(times, color):
    # times = int(times)
    return render_template("index.html", times = times, color = color)

if __name__=="__main__":
    app.run(debug=True)
