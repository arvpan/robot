from flask import Flask, url_for
from flask import g, session, request, render_template, flash
from aiml import Kernel
from os import listdir

files = listdir('standard')

#CONFIGURATION
DEBUG = True



#APP
app = Flask(__name__)
app.config.from_object(__name__)



bot = Kernel()
for file in files:
	bot.learn('standard/'+file)

respon = ' '

@app.before_request
def before_request():
	g.respon = 'Hello , Hugo The Robot. Some people call me the Mad Robot. Good to see you.'

@app.route('/',methods=['GET','POST'])
def index():
	if request.method == 'POST':
		reply = bot.respond(request.form['question'])
		return render_template('index.html',respon=reply)
	return render_template('index.html',respon=g.respon)
	
#running the app
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
