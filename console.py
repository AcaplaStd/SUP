
from sup import *
import datetime


while True:
    s = input('>>> ').split()
    c = s[0]
    l = len(s)
    if c == 'register':
        if l >= 4 and s[-2] == s[-1]:
            register(s[1], s[2])
        else:
            print('Register syntax is:\nregister <username> <password> <confirm pw>')
    elif c == 'save':
        save()
    elif c == 'load':
        load()
    elif c == 'addperson':
        i = -1
        if l == 2:
            i = add_person(s[1])
        elif l >= 3:
            i = add_person(s[1], s[2])
        else:
            print('AddPerson syntax is:\naddperson <name> [surname]')
        print('ID of %s is %d' % (s[1], i) if i >= 0 else '')
    elif c == 'addevent':
        if l < 3:
            print('AddEvent syntax is:\naddevent <person_id> <title> [text] [DD.MM.YYYY]')
            continue
        i = s[1]
        if l == 3:
            r = people[i].add_event(s[2])
        elif l == 4:
            r = people[i].add_event(s[2], s[3])
        else:
            d = datetime.date(list(map(int, s[4].split('.')))[::-1])
            r = people[i].add_event(s[2], s[3], d)
        print('ID of %s is %d' % (s[2], r))
    elif c == 'editevent':
        if l < 3:
            print('EditEvent syntax is:\neditevent <id> <title> [text] [DD.MM.YYYY]')
            continue
        i = int(s[1])
        if l == 3:
            events[i].edit(s[2])
        elif l == 4:
            events[i].edit(s[2], s[3])
        else:
            d = datetime.date(map(int, s[4].split('.'))[::-1])
            events[i].edit(s[2], s[3], s[4])
    elif c == 'person':
        if l < 2:
            print('Person syntax is:\nperson <id>')
            continue
        i = int(s[1])
        p = people[i]
        print('name:', p.name)
        print('surname:', p.surname)
        print('events:', ', '.join(map(str, p.events)))
    elif c == 'event':
        if l < 2:
            print('Event syntax is:\nevent <id>')
            continue
        i = int(s[1])
        e = events[i]
        print('title:', e.title)
        print('text:', e.text)
        print('date:', e.date)
    elif c == 'exit':
        break
    else:
        print("Unknown command '%s'" % c)
