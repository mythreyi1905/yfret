
from flask import Flask, render_template
from flask import request
from flask_pymongo import PyMongo

app=Flask(__name__)

app.config['MONGO_URI'] = "mongodb://mythreyi:#Include1@ds233167.mlab.com:33167/bank"

mongo = PyMongo(app)

@app.route('/')
def home():
    return "This is the Homepage.Follow the README folder for obtaining output for the three different queries." 

@app.route('/query1',methods=['GET'])
def cellular():
    usercount = mongo.db.banker.find({"contact":{"$ne":"cellular"}}).count()
    users = mongo.db.banker.find({"contact":{"$ne":"cellular"}})
    return render_template('query1.html', users = users , usercount=usercount)

@app.route('/query2',methods =['GET'])
def dob():
    users = mongo.db.banker.find({ "$and":[ {"day" : { "$gt" : (15)}},{"month" : { "$in" : ["oct","nov","dec"]}}]})
    return render_template('query2.html', users = users )

@app.route('/query3/<int:start_age>/<int:end_age>/<string:marital>',methods =['GET'])
def customized(start_age,end_age,marital):
    users = mongo.db.banker.find({ "$and":[ {"age" : { "$gt" : (start_age)}},{"age" : { "$lt" : (end_age)}},{"marital" : marital }]})
    return render_template('query3.html',users = users, start_age=start_age, end_age=end_age,marital = marital )

if __name__ == '__main__': 
    app.run(debug=True,host= '0.0.0.0', port = 3000)
