from flask import Flask, request
from datetime import date, datetime
from calcs import f_calculation
import json

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

# @app.route('/test/<givennumber>',methods = ['POST', 'GET'])
# def testplayername(givennumber):
#     if request.method == 'POST':
#         print("Method = Post")
#         data = request.get_json()
#         quoteword = data['quote_word']
#         print(quoteword)
#         print(data)
#     else:
#         print("Method = Get")
#     print(givennumber)
#     response = f_calculation(int(givennumber))
#     return f'name of player = {response} '

@app.route('/daysbetween',methods = ['POST'])
def daycalculator():
    data = request.get_json()
    day1 = date.fromisoformat(data['day1'])
    day2 = date.fromisoformat(data['day2'])
    response = abs((day2 - day1).days)
    return f'days between {day1} and {day2} = {response} '

@app.route('/secondsbetween',methods = ['POST'])
def secondcalculator():
    data = request.get_json()
    day1 = date.fromisoformat(data['day1'])
    day2 = date.fromisoformat(data['day2'])
    response = abs(((((day2 - day1).days)*24)*60)*60)
    return f'seconds between {day1} and {day2} = {response} '

@app.route('/hoursbetween',methods = ['POST'])
def hourcalculator():
    data = request.get_json()
    day1 = date.fromisoformat(data['day1'])
    day2 = date.fromisoformat(data['day2'])
    response = abs(((day2 - day1).days)*24)
    return f'hours between {day1} and {day2} = {response} '

@app.route('/dayssince',methods = ['POST'])
def daysince():
    data = request.get_json()
    day1 = datetime.fromisoformat(data['day1'])
    response = ((abs(day1 - datetime.now())).days)
    return f'days since {day1.date()} = {response} '

@app.route('/currenttime',methods = ['POST'])
def getcurrenttime():
    return f'Current time = {datetime.now()}'

@app.route('/test',methods = ['POST'])
def test():
    return json.dumps({'key': 'value'})



