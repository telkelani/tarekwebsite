from flask import Flask, render_template, url_for

app = Flask(__name__)

about_page = 'about'
home = 'home'

@app.route("/")
@app.route("/index")
def index():
	return render_template('index.html', home=home)

@app.route("/about")
def about():
	return render_template('about.html', about_page=about_page)


if __name__ == '__main__':
	app.run(debug=True) #So I don't have to keep setting the env variables every time i shut down terminal
