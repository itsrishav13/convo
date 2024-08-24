from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/saved")
def saved():
    return render_template('saved.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/posted_threads")
def posted_threads():
    return render_template('posted_threads.html')


if __name__ == '__main__':
    app.run(debug=True)
