from flask import Flask, request
from chatgpt import talk_gpt


app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/citytheme/<giventheme>')
def citymaker(giventheme):
    prompt = f"Generate a city name with the theme: {giventheme}, respond with only that name. If theme doesnt exist, reply with: Theme doesnt exist"
    return talk_gpt(prompt)

@app.route('/usergenerator/<giventheme>')
def usergenerator(giventheme):
    prompt = f"Generate a roblox username with this theme: {giventheme}, respond with only that name. If theme doesnt exist, reply with: Theme doesnt exist"
    return talk_gpt(prompt)

@app.route('/challangegenerator/<givenlanguage>/<givendifficulty>')
def challangegenerator(givenlanguage,givendifficulty):
    prompt = f"Generate a random programming challange, in this language: {givenlanguage} and this difficulty: {givendifficulty}"
    return talk_gpt(prompt)