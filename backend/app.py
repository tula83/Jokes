from flask import Flask, request,jsonify
from flask_cors import CORS
from models.users import User
from models.jokes import Jokes
from routes.joke_routes import get_joke,get_joke_rapid
import openai

import sys
import os
## required while importing  modules

sys.path.append(os.path.abspath(os.path.dirname(__file__)))



# Initialize Flask app
app = Flask(__name__)
CORS(app)



@app.route("/user/insert",methods=['POST'])
def insert_user():
    user=request.get_json()
    email=user.get('email')
    username=user.get("username")

    if email == None or username == None or len(email) == 0 or len(username) == 0 :
        return "Please provide credentials",400

    user=User(email=email,username=username)

    result=user.save_user_data()

    return result


@app.route("/user/get",methods=['GET'])
def get_user():
    user=User()
    result=user.get_user_data()
    return result




### insert data
@app.route("/jokes/insert",methods=["POST"])
def joke_insert():
    data=request.get_json()
    cat=data.get("category")
    mssg=data.get("message")

    if mssg== None or  len(mssg) == 0:
        return "message is required",400

    ###
    joke=Jokes(category=cat,message=mssg)
    result=joke.save_joke()

    return {"message":result},201


@app.route("/jokes/get",methods=['GET'])
def get_joke():
    jokes=Jokes()
    data=jokes.get_joke()
    return jsonify({'data':data}),200







if __name__ == "__main__":
    app.run(debug=True)
