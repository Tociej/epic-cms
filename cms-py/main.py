from tkinter import *
from functools import partial
# import requests
import json
import sqlite3

root = Tk()
root.title("Panel Sterowanya")
root.geometry("300x150")
root.resizable(False, False)

database = sqlite3.connect("database.sqlite")
cursor = database.cursor()


def dbSetup():
    cursor.execute("CREATE TABLE users (login TEXT, password TEXT, permissions INT)")
    cursor.execute("INSERT INTO users (login, password, permissions) VALUES ('admin', 'admin', 1)")
    cursor.execute("INSERT INTO users (login, password, permissions) VALUES ('user', 'user', 0)")

    header = {
        "color": "black",
        "bgcolor": "gray"}
    cursor.execute("CREATE TABLE menu (field TEXT)")
    cursor.execute("insert into menu (field) VALUES ('" + json.dumps(header) + "')")

    settings = {
        "fontsize": 24,
        "fontfamily": "Arial",
        "color": "black",
        "bgcolor": "white",
        "border": "gray",
        "order": ["slider", "news", "features"]
    }
    cursor.execute("CREATE TABLE settings (field TEXT)")
    cursor.execute("insert into settings (field) VALUES ('" + json.dumps(settings) + "')")

    slider = {
        "speed": 1000,
        "slides": [
            {"content": "first slide", "header": "ONE SLIDE",
             "bg": "https://wally.com.pl/galerie/t/tapeta-na-sciane-gory-032_55845.jpg", "fg": "white"},
            {"content": "2nd slide",
             "bg": "https://www.imperiumtapet.com/public/uploads/preview/krajobraz-20421535474510e55t5qdn5p.jpg",
             "fg": "yellow"},
            {"content": "3",
             "bg": "https://th.bing.com/th/id/R.c14ec6e89a110fa4756127ff14c0d658?rik=%2f%2bZfVI%2fTZqJN6Q&pid=ImgRaw&r=0",
             "fg": "black"},
        ]
    }
    cursor.execute("CREATE TABLE slider (field TEXT)")
    cursor.execute("insert into slider (field) VALUES ('" + json.dumps(slider) + "')")

    news = [
        {"content": "new products omg", "header": "head", "category": "balls", "article": "lorem ipsum",
         "comments": [{"user": "nick", "text": "dda"}]},
        {"content": "good news everyone!", "category": "balls", "article": "lorem ipsum", "comments": []},
        {"content": "poland mountain", "category": "balls", "article": "lorem ipsum", "comments": []},
        {"content": "new4", "article": "lorem ipsum", "category": "cawk", "comments": []},
        {"content": "new5", "article": "lorem ipsum", "category": "balls", "comments": []}
    ]
    cursor.execute("CREATE TABLE news (field TEXT)")
    cursor.execute("insert into news (field) VALUES ('" + json.dumps(news) + "')")

    features = [
        {"content": "This is first feature", "header": "great feature", "imgsrc": "https://i.imgur.com/WpE9bNBb.jpg"},
        {"content": "This is really nice feautere", "header": "great one really",
         "imgsrc": "https://i.imgur.com/WpE9bNBb.jpg"}
    ]
    cursor.execute("CREATE TABLE features (field TEXT)")
    cursor.execute("insert into features (field) VALUES ('" + json.dumps(features) + "')")
    database.commit()


try:
    cursor.execute("SELECT * fRoM users")
except:
    dbSetup()


# print(login.get())


def submit():
    global accesslevel
    print(f"{login.get()}, {password.get()}")

    # temporary adding ^-^

    # cursor.execute("SELECT * FROM users")
    # print(cursor.fetchall())

    # cursor.execute("SELECT * FROM users WHERE login='" + login.get() + "' AND password='" + password.get() + "' AND permissions > 0")
    # fetchone = cursor.fetchone()

    if (login.get() != "root" or password.get() != "root"):
        print("Access Denied")
        labelstate.config(text="Access Denied, please try again!", fg="red")
    else:
        print("Access Granted")
        labelstate.config(text="Access Granted", fg="green")

        # print(fetchone[2])
        # accesslevel = fetchone[2]

        openSettings()
        # open new window


labelstate = Label(root, text="Please log in!")
labelstate.pack()

labellogin = Label(root, text="Login:").pack()
login = Entry(root)
login.pack()
labelpassword = Label(root, text="Password:").pack()
password = Entry(root, show="*")
password.pack()

submit = Button(root, text="Submit", command=submit).pack()


def openSettings():
    global new
    global frame
    new = Toplevel()
    new.geometry("300x400")
    new.title("User center")
    new.resizable(False, False)
    label = Label(new, text=f"Welcome {login.get()}").grid(row=0, column=0)

    usersButton = Button(new, text="Users", command=usersTable).grid(row=1, column=0)
    menuButton = Button(new, text="Main Menu", command=menuTable).grid(row=1, column=1)
    settingsButton = Button(new, text="Settings", command=settingsTable).grid(row=1, column=2)
    sliderButton = Button(new, text="Slider", command=sliderTable).grid(row=1, column=3)

    frame = Frame(new)
    frame.grid(row=2, column=0, columnspan=5)
    usersTable()


def usersTable():
    for widgets in frame.winfo_children():
        widgets.destroy()
    cursor.execute("SELECT * FROM users")
    label = Label(frame, text="Username").grid(row=1, column=0)
    label = Label(frame, text="Password").grid(row=1, column=1)
    label = Label(frame, text="Accesslevel").grid(row=1, column=2)
    button = Button(frame, text="Add user", command=addUser).grid(row=1, column=3)
    # print("start making table: \n")

    iterator = 1
    for i in cursor.fetchall():
        iterator += 1
        for j in range(len(i)):
            label = Label(frame, text=i[j]).grid(row=iterator, column=j)
            userArgs = partial(deleteUser, i[0])
            editArgs = partial(editUser, i[0], i[1])
        button = Button(frame, text="Delete", command=userArgs).grid(row=iterator, column=3)
        button = Button(frame, text="Edit", command=editArgs).grid(row=iterator, column=4)
        # print("Nick", i[0])


def menuTable():
    for widget in frame.winfo_children():
        widget.destroy()

    cursor.execute("Select * from menu")
    data = json.loads(cursor.fetchone()[0])
    print(data)
    iterator = 0
    keys = []
    for key, value in data.items():
        label = Label(frame, text=key).grid(row=iterator, column=0)
        keys.append(key)
        entry = Entry(frame)
        entry.insert(0, value)
        entry.grid(row=iterator, column=1)
        iterator += 1

    button = Button(frame, text="Confirm", command=lambda: updateMenu(keys)).grid(row=iterator + 2, column=0,
                                                                                  columnspan=2)


def updateMenu(keys):
    values = []
    for element in frame.winfo_children():
        if (element.winfo_class() == "Entry"):
            values.append(element.get())

    cursor.execute("Delete from menu")
    input = {}
    for i in range(len(keys)):
        input[keys[i]] = values[i]
    print(input)
    cursor.execute("insert into menu (field) VALUES ('" + json.dumps(input) + "')")
    database.commit()
    # json.dumps(dict)


def settingsTable():
    for widget in frame.winfo_children():
        widget.destroy()

    cursor.execute("Select * from settings")
    data = json.loads(cursor.fetchone()[0])
    print(data)
    iterator = 0
    keys = []
    order = data["order"]
    for key, value in data.items():
        if(key == "order"):
            continue
        label = Label(frame, text=key).grid(row=iterator, column=0)
        keys.append(key)
        entry = Entry(frame)
        entry.insert(0, value)
        entry.grid(row=iterator, column=1)
        iterator += 1

    button = Button(frame, text="Confirm", command=lambda: updateSettings(keys, order)).grid(row=iterator + 2, column=0,
                                                                                      columnspan=2)


def updateMenu(keys):
    values = []
    for element in frame.winfo_children():
        if (element.winfo_class() == "Entry"):
            values.append(element.get())

    cursor.execute("Delete from menu")
    input = {}
    for i in range(len(keys)):
        input[keys[i]] = values[i]


    print(input)
    cursor.execute("insert into menu (field) VALUES ('" + json.dumps(input) + "')")
    database.commit()
    # json.dumps(dict)


def updateSettings(keys, order):
    values = []
    for element in frame.winfo_children():
        if (element.winfo_class() == "Entry"):
            values.append(element.get())

    cursor.execute("Delete from settings")
    input = {}
    for i in range(len(keys)):
        input[keys[i]] = values[i]

    input["order"] = order 
    print(input)
    cursor.execute("insert into settings (field) VALUES ('" + json.dumps(input) + "')")
    database.commit()


def sliderTable():
    for widget in frame.winfo_children():
        widget.destroy()

    cursor.execute("Select * from slider")
    data = json.loads(cursor.fetchone()[0])
    print(data)
    iterator = 0
    keys = []
    for key, value in data.items():

        if (type(value) == list):
            for i in value:
                for key2, value in i.items():
                    if key2 == "bg":
                        label = Label(frame, text=f"slider {numeration} {key2}").grid(column=0, row=iterator)
                        numeration += 1
                        entry = Entry(frame)
                        entry.insert(0, value)
                        entry.grid(column=1, row=iterator)
                        iterator += 1
                        # grid
        else:
            label = Label(frame, text=key).grid(row=iterator, column=0)
            keys.append(key)
            entry = Entry(frame)
            entry.insert(0, value)
            entry.grid(row=iterator, column=1)
            iterator += 1
            numeration = 0

    button = Button(frame, text="Confirm", command=lambda: updateSlider(keys, data)).grid(row=iterator + 2, column=0,
                                                                                          columnspan=2)


def updateSlider(keys, data):
    values = []
    for element in frame.winfo_children():
        if (element.winfo_class() == "Entry"):
            values.append(element.get())

    data["speed"] = values[0]
    iterator = 1
    for x in data["slides"]:
        data["slides"][iterator-1]["bg"] = values[iterator]
        iterator += 1
    cursor.execute("Delete from slider")

    cursor.execute("insert into slider (field) VALUES ('" + json.dumps(data) + "')")
    database.commit()


def deleteUser(username):
    print("Processed nick", username)
    cursor.execute("DELETE FROM users WHERE login='" + username + "'")
    database.commit()
    usersTable()


def editUser(prevusername, prevpassword):
    global edit
    global statusLabelEdit

    edit = Toplevel()
    edit.title("Edit User")
    edit.resizable(False, False)

    statusLabelEdit = Label(edit, text=f"Editing user: {prevusername}")
    statusLabelEdit.grid(row=0, column=0, columnspan=2)

    label = Label(edit, text="Nickname").grid(row=1, column=0)
    label = Label(edit, text="Password").grid(row=2, column=0)

    nickname = Entry(edit)
    nickname.grid(row=1, column=1)
    nickname.insert(0, prevusername)
    password = Entry(edit)
    password.grid(row=2, column=1)
    password.insert(0, prevpassword)

    v = StringVar(edit, "0")
    Radiobutton(edit, text="User", variable=v,
                value="0", indicator=0,
                background="light blue").grid(row=3, column=0)
    Radiobutton(edit, text="Admin", variable=v,
                value="1", indicator=0,
                background="light blue").grid(row=3, column=1)

    button = Button(edit, text="Add user",
                    command=lambda: commitEditUser(prevusername, prevpassword, nickname.get(), password.get(),
                                                   v.get())).grid(
        row=5, column=0, columnspan=2)


def commitAddUser(nickname, password, permissions):
    print("Adding user", nickname, password)

    cursor.execute("SELECT * FROM users WHERE (login = '" + nickname + "')")
    print(cursor.fetchall())
    if (cursor.fetchall() == []):
        cursor.execute(
            "INSERT INTO users (login, password, permissions) VALUES ('" + nickname + "', '" + password + "', '" + permissions + "')")
        database.commit()

        statusLabel.configure(text="Success")

        # dont destroy if you want to
        add.destroy()
        usersTable()

    else:
        statusLabel.configure(text="User Already In Database")


def addUser():
    # open add window
    global add
    global statusLabel
    add = Toplevel()
    add.title("Add User")

    statusLabel = Label(add, text="Please Add User")
    statusLabel.grid(row=0, column=0, columnspan=2)

    label = Label(add, text="Nickname").grid(row=1, column=0)
    label = Label(add, text="Password").grid(row=2, column=0)
    nickname = Entry(add)
    nickname.grid(row=1, column=1)
    password = Entry(add)
    password.grid(row=2, column=1)

    v = StringVar(add, "0")
    Radiobutton(add, text="User", variable=v,
                value="0", indicator=0,
                background="light blue").grid(row=3, column=0)
    Radiobutton(add, text="Admin", variable=v,
                value="1", indicator=0,
                background="light blue").grid(row=3, column=1)

    button = Button(add, text="Add user", command=lambda: commitAddUser(nickname.get(), password.get(), v.get())).grid(
        row=5, column=0, columnspan=2)


def commitAddUser(nickname, password, permissions):
    print("Adding user", nickname, password)

    cursor.execute("SELECT * FROM users WHERE (login = '" + nickname + "')")
    exists = cursor.fetchone()

    if exists is None:
        cursor.execute(
            "INSERT INTO users (login, password, permissions) VALUES ('" + nickname + "', '" + password + "', '" + permissions + "')")
        database.commit()

        statusLabel.configure(text="Success")

        # dont destroy if you want to
        add.destroy()
        usersTable()

    else:
        statusLabel.configure(text="User Already In Database")


def commitEditUser(prevnickname, prevpassword, newnickname, newpassword, permissions):
    print("Editing user", prevnickname, prevpassword)

    cursor.execute("SELECT * FROM users WHERE (login = '" + newnickname + "')")
    if (cursor.fetchone() is None or prevnickname == newnickname):
        # replace old data with new one
        cursor.execute("DELETE FROM users WHERE (login ='" + prevnickname + "')")
        cursor.execute(
            "INSERT INTO users (login, password, permissions) VALUES ('" + newnickname + "','" + newpassword + "','" + permissions + "')")
        database.commit()

        edit.destroy()
        usersTable()

    else:
        statusLabelEdit.configure(text="username already exists")


root.mainloop()