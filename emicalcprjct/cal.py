from flask import Flask,render_template,redirect,url_for,request,session
from flask_pymongo import PyMongo

app=Flask(__name__)
app.config['SECRET_KEY']='1b33ac8c097cae90298bf30d17e47804b7118b1420c5b94a'
app.config['MONGO_DBNAME']='Calculator'
app.config['MONGO_URI']='mongodb+srv://SheetalK01:SVKME2015@sheetalkcluster-xtvj5.mongodb.net/Calculator?retryWrites=true&w=majority'
mongo=PyMongo(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/calculator',methods=['GET','POST'])
def cal():
	if request.method == 'POST':
		calc = mongo.db.Calculator
		current=calc.find_one({'pa':request.form['principal_amount']})

		if current is None:
			#hashpass=bcrypt.hashpw(request.form['pass'].encode('utf-8'),bcrypt.gensalt())
			princ=request.form['principal_amount']
			rt=request.form['rate']

			session['ri'] = rt
			print "Session of rate:",session['ri']
			rt=float(rt)/(12*100)

			print("Calcualted rate for one month period:",rt)
			trm=request.form['term']
			session['tenureterm'] = trm
			print "Session of term:",session['tenureterm']
			trm=int(trm)*12
			print "Calculated term for one month interest:",trm
			result=(int(princ)*float(rt)*(int(1+rt)**trm)/(((1+rt)**trm)-1))
			print result
			calc.insert({'pa':princ,'ri':rt,'tenureterm':trm,'emi':result})
			session['pa'] = princ
			print "Session of pa: ",session['pa']
			
			session['emi'] = result
			return redirect(url_for('cal'))
		else:
			return redirect(url_for('index'))
	return render_template('index.html')