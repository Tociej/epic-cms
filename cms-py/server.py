import sqlite3, json
from flask import *
from flask_cors import CORS
import requests

ඞ = Flask(__name__, static_url_path='')
CORS(ඞ)




@ඞ.route("/getData", methods=['POST', 'GET'])
def getData():
    conn = sqlite3.connect("database.sqlite") 
    cursor = conn.cursor()
    header = cursor.execute("sElECt * fRoM menu").fetchone()[0]
    s̸̡̧̢̜̖̰̣̖̼̙̖͎͈̞̏̎͠ļ̸̛̝͎̝̱̥͙͕̖̯̭̀̄̀̀͠i̷͇̜̱͕͖̜̫̭̦̦̹̠͙̔ḑ̵̡͍̩̅̿̕͠ę̸̦̩̱̗̬̘̘͙̜̈́̊͐̄̀̔̌̑̑͂́̕͜ͅr̴̰̮̪̜͓̼̱̳̳͓̹̞̲͛̾̂́́̅̂̉ = cursor.execute("sElECt * fRoM slider").fetchone()[0]
    settings = cursor.execute("sElECt * fRoM settings").fetchone()[0]
    news = cursor.execute("seLecT * fRom news").fetchone()[0]
    features = cursor.execute("seLECt * FROm features").fetchone()[0]
    data = {
        "header": json.loads(header),
        "slider": json.loads(s̸̡̧̢̜̖̰̣̖̼̙̖͎͈̞̏̎͠ļ̸̛̝͎̝̱̥͙͕̖̯̭̀̄̀̀͠i̷͇̜̱͕͖̜̫̭̦̦̹̠͙̔ḑ̵̡͍̩̅̿̕͠ę̸̦̩̱̗̬̘̘͙̜̈́̊͐̄̀̔̌̑̑͂́̕͜ͅr̴̰̮̪̜͓̼̱̳̳͓̹̞̲͛̾̂́́̅̂̉),
        "settings": json.loads(settings),
        "news":json.loads(news),
        "features": json.loads(features)
    }
    conn.close()
    response = ඞ.response_class(response=json.dumps(data), mimetype="application/json", status=200 )
    return response

#kocham svelte rel
#ඞඞඞඞඞඞඞඞඞඞඞ

@ඞ.route("/setData", methods=['POST', "GET"])
def setData():
    data = request.get_json()
    slider = data.get("slider")
    news = data.get("news")
    features = data.get("features")
    settings = data.get("settings")
    header = data.get("header")

    conn = sqlite3.connect("database.sqlite")
    cursor = conn.cursor()
    cursor.execute("delete from menu")
    cursor.execute("insert into menu (field) VALUES ('" + json.dumps(header) +  "')")
    cursor.execute("delete from settings")
    cursor.execute("insert into settings (field) VALUES ('" + json.dumps(settings) +  "')")
    cursor.execute("delete from slider")
    cursor.execute("insert into slider (field) VALUES ('" + json.dumps(slider) +  "')")   
    cursor.execute("delete from features")
    cursor.execute("insert into features (field) VALUES ('" + json.dumps(features) +  "')")
    cursor.execute("delete from news")
    cursor.execute("insert into news (field) VALUES ('" + json.dumps(news) +  "')")
    conn.commit()
    conn.close()

    response = ඞ.response_class(response=json.dumps({"res":"work"}), mimetype="application/json", status=200 )
    return response
    
    # send to db 

@ඞ.route("/login", methods=['POST', "GET"])
def login():
    data  = request.get_json()
    user = data.get("user")
    passw = data.get("password")

    conn = sqlite3.connect("database.sqlite")

    cursor = conn.cursor()

    cursor.execute(f"sEleCT * from users WHERE (login = '{user}' AND password = '{passw}')")
    gamer = cursor.fetchone()
    if(gamer is None):
        print("rip bozo")
        response = ඞ.response_class(response=json.dumps({"res": "bad"}), mimetype="application/json", status=200 )
        return response
    else:
        print(gamer[2])
        response = ඞ.response_class(response=json.dumps({"res":"pog", "perms": gamer[2], "user": user}), mimetype="application/json", status=200 )
        return response

@ඞ.route("/deleteComment", methods=["POST", "GET"])
def deleteComment():
    data = request.get_json()
    article_id = data.get("articleid")
    id = data.get("id")

    conn = sqlite3.connect("database.sqlite")
    cursor = conn.cursor()
    cursor.execute("selEcT * fRoM news")
    newse = cursor.fetchone()[0]
    news = json.loads(newse)
    news[article_id]["comments"].pop(id)

    cursor.execute("Delete from news")
    cursor.execute("insert into news (field) VALUES ('" + json.dumps(news) + "')")
    conn.commit()

    return ඞ.response_class(response=json.dumps(news[article_id]["comments"]), mimetype="application/json", status=200 )

@ඞ.route("/postComment", methods=["POST", "GET"])
def postComment():
    data = request.get_json()
    article_id = data.get("articleid")
    user = data.get("user")
    comment = data.get("comment")

    conn = sqlite3.connect("database.sqlite")
    cursor = conn.cursor()
    cursor.execute("selEcT * fRoM news")
    newse = cursor.fetchone()[0]
    news = json.loads(newse)
    news[article_id]["comments"].append({"user": user, "text": comment})

    cursor.execute("Delete from news")
    cursor.execute("insert into news (field) VALUES ('" + json.dumps(news) + "')")
    conn.commit()

    return ඞ.response_class(response=json.dumps(news[article_id]["comments"]), mimetype="application/json", status=200 )


@ඞ.route("/register", methods=['POST', "GET"])
def register():
    data  = request.get_json()
    user = data.get("user")
    passw = data.get("password")

    conn = sqlite3.connect("database.sqlite")

    cursor = conn.cursor()
    gamer = cursor.fetchone()
    if(gamer is None):
        print("rip bozo")
        cursor.execute("INSERT INTO users (login, password, permissions) VALUES ('"+ user + "', '"+ passw + "', 0)")
        conn.commit()
        response = ඞ.response_class(response=json.dumps({"res":"pog", "perms": 0, "user": user}), mimetype="application/json", status=200 )
        return response
    else:
        print(gamer[2])
        response = ඞ.response_class(response=json.dumps({"res":"bad"}), mimetype="application/json", status=200 )
        return response
    
    pass


if __name__ == "__main__":
    ඞ.run(debug=True)


