from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
	{
		'author': 'Surbhi Agarwal',
		'title': 'Blog Post 1',
		'context': 'First post content',
		'date_posted': '04/09/2018'
	},	
	{
		'author': 'Pranshu Mishra',
		'title': 'Blog Post 2',
		'context': 'Second post content',
		'date_posted': '05/09/2018'
	}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
	app.run(debug=True)