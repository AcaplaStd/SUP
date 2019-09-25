# Sistjema Uznavanija Podrobnostjej
# (C) Acapla Studios 2019


import pickle
import datetime as dt

people = []
users = []
events = []


def encrypt(s: str):
    return s


class User:
    def __init__(self, name: str, pw: str = ''):
        self.name = name
        self.pw = encrypt(pw)


class Event:
    def __init__(self, title: str = '', text: str = '', date: dt.date = dt.date(1900, 1, 1)):
        global events
        self.title = title
        self.text = text
        self.date = date
        self.id = len(events)
        events.append(self)

    def edit(self, title: str = '', text: str = '', date: dt.date = dt.date(1900, 1, 1)):
        if title != '':
            self.title = title
        if text != '':
            self.text = text
        if text != dt.date(1900, 1, 1):
            self.date = date


class Person:
    def __init__(self, name: str, surname: str = ''):
        self.id = len(people)
        self.name = name
        self.surname = surname
        self.events = []

    def add_event(self, title: str = '', text: str = '', date: dt.date = dt.date(1900, 1, 1)):
        i = Event(title, text, date).id
        self.events.append(i)
        return i


def save(peoplefile: str = 'people.pickle', eventfile: str = 'events.pickle', userfile: str = 'users.pickle'):
    with open(peoplefile, 'wb') as file:
        pickle.dump(people, file)
    with open(eventfile, 'wb') as file:
        pickle.dump(events, file)
    with open(userfile, 'wb') as file:
        pickle.dump(users, file)


def load(peoplefile: str = 'people.pickle', eventfile: str = 'events.pickle', userfile: str = 'users.pickle'):
    global people, events, users
    with open(peoplefile, 'rb') as file:
        people = pickle.load(file)
    with open(eventfile, 'rb') as file:
        events = pickle.load(file)
    with open(userfile, 'rb') as file:
        users = pickle.load(file)


def register(name: str, pw: str):
    users.append(User(name, pw))


def add_person(name: str, surname: str = ''):
    p = Person(name, surname)
    people.append(p)
    return p.id
