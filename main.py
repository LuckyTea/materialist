import os
import json
from datetime import datetime

content = {}
json_content = {}
host = os.listdir()
db = 'data.dat'
indent = 15
header = {'base': 'alpha 001', 'last update': str(datetime.now())}
graph = ['Name', 'Location', 'Date buy', 'Date exchange', 'Cost', 'Cost exchange', 'Tags']


def init():
    if(db not in host):
        init_header()
    else:
        with open(db, 'r') as file:
            try:
                content = json.load(file)
                if('header' not in content):
                    init_header()
            except ValueError:
                init_header()
    main()


def init_header():
    with open(db, 'w') as file:
        content['header'] = header
        json.dump(content, file, indent=4)


def main():
    while True:
        com = input('Command: ').lower()
        if(com == 'add' or com == 'a'):
            add()
        elif(com == 'show' or com == 's'):
            show()
        elif(com == 'remove base' or com == 'rm'):
            remove_base()
        elif(com == 'exit' or com == 'ex'):
            break
        else:
            print('List of commands: \n',
                  'add(a) - Add new element to itemsbase.\n',
                  'show(s) - show all added items\n',
                  'remove base(rm) - clean database\n',
                  'exit(ex) - close programm')


def add():
    add_content = []
    for i in range(len(graph)):
        while True:
            if(i == 6):
                in_content = str(input('{:{}}'.format(graph[i]+':', indent)))
                in_content = in_content.split(', ')
                break
            else:
                in_content = str(input('{:{}}'.format(graph[i]+':', indent)))
                if(len(in_content) > 100):
                    print('100 characters maximum')
                else:
                    break
        add_content.append(in_content)
        json_content[graph[i]] = add_content[i]
    json_content['Date add'] = str(datetime.now())
    with open(db, 'r') as file:
        content = json.load(file)
    with open(db, 'w') as file:
        content['header']['last update'] = str(datetime.now())
        content[str(len(content)+1)] = json_content
        json.dump(content, file, indent=4, sort_keys=True)
    backup()


def sort_list(content):
    true_list = sorted(content)
    true_list.remove('header')
    another_true_list = []
    for i in true_list:
        another_true_list.append(int(i))
        another_true_list = sorted(another_true_list)
    return(another_true_list)


def show():
    with open(db, 'r') as file:
        content = json.load(file)
    if(len(content) <= 1):
        print('Add something first.')
    else:
        print('Last update at {}\n{}'.format(content['header']['last update'], '-'*80))
        for i in sort_list(content):
            i = str(i)
            print('#{} {} {}'.format(i.zfill(3), graph[0]+':', content[i][graph[0]]))
        show_control()


def show_control():
    while True:
        com = input('Show Command: ').lower()
        com = com.split(' ')
        if(com[0] == 'all'):
            show_all()
        elif(com[0] == 'show'):
            com.remove('show')
            if(len(com) >= 1):
                item_show(com)
            else:
                print('!!! This command should have atlesat one argument !!!')
        elif(com[0] == 'tag'):
            com.remove('tag')
            if(len(com) >= 1):
                search_tag(com)
            else:
                print('!!! This command should have atlesat one argument !!!')
        elif(com[0] == 'edit'):
            com.remove('edit')
            if(len(com) >= 1):
                print('!!! This command can have only one argument !!!')
            else:
                item_edit(com)
        elif(com[0] == 'delete'):
            com.remove('delete')
            if(len(com) > 1 and len(com) < 0):
                print('This command can have only one argument')
            else:
                item_delete(com)
        elif(com[0] == 'back'):
            break
        else:
            print('List of commands: \n',
                  'all - Show full infotmation for all elements.\n',
                  'show # - Show full infotmation for # elements.\n',
                  'edit # = Edit # element.\n',
                  'delete # - Delete # element\n',
                  'back - Back to main menu.')


def show_all():
    with open(db, 'r') as file:
        content = json.load(file)
        ii = 0
        for i in sort_list(content):
            if(ii == 5):
                input('Next...')
                ii = 0
            else:
                i = str(i)
                print('{dash}\n{i1:{i}} {i2}\n{n1:{i}} {n2}\n{l1:{i}} {l2}\n{d1:{i}} {d2}\n{d3:{i}} {d4}\n\
{c1:{i}} {c2:{i}}\n{c3:{i}} {c4}\n{t1:{i}} {t2}'.format(
                    i1='id:',        i2=i.zfill(3),            # ID
                    n1=graph[0]+':', n2=content[i][graph[0]],  # Name
                    l1=graph[1]+':', l2=content[i][graph[1]],  # Location
                    d1=graph[2]+':', d2=content[i][graph[2]],  # Date buy
                    d3=graph[3]+':', d4=content[i][graph[3]],  # Date exchange
                    c1=graph[4]+':', c2=content[i][graph[4]],  # Cost
                    c3=graph[5]+':', c4=content[i][graph[5]],  # Cost exchange
                    t1=graph[6]+':', t2=', '.join(content[i][graph[6]]),  # Tags
                    dash='-'*80, i=indent))
                ii += 1


def item_show(element):
    with open(db, 'r') as file:
        content = json.load(file)
        try:
            for i in element:
                print('{dash}\n{i1:{i}} {i2}\n{n1:{i}} {n2}\n{l1:{i}} {l2}\n{d1:{i}} {d2}\n{d3:{i}} {d4}\n\
{c1:{i}} {c2:{i}}\n{c3:{i}} {c4}\n{t1:{i}} {t2}\n{dash}'.format(
                    i1='id:',        i2=i.zfill(3),            # ID
                    n1=graph[0]+':', n2=content[i][graph[0]],  # Name
                    l1=graph[1]+':', l2=content[i][graph[1]],  # Location
                    d1=graph[2]+':', d2=content[i][graph[2]],  # Date buy
                    d3=graph[3]+':', d4=content[i][graph[3]],  # Date exchange
                    c1=graph[4]+':', c2=content[i][graph[4]],  # Cost
                    c3=graph[5]+':', c4=content[i][graph[5]],  # Cost exchange
                    t1=graph[6]+':', t2=', '.join(content[i][graph[6]]),  # Tags
                    dash='-'*80, i=indent))
        except KeyError:
            print('There is no items with id #{}'.format(''.join(element)))


def item_edit(element):
    with open(db, 'r') as file:
        content = json.load(file)
        for i in element:
                print('{dash}\n{n1:{i}} {n2}\n{l1:{i}} {l2}\n{d1:{i}} {d2}\n{d3:{i}} {d4}\n\
{c1:{i}} {c2:{i}}\n{c3:{i}} {c4}\n{t1:{i}} {t2}\n{dash}'.format(
                    n1=graph[0]+':', n2=content[i][graph[0]],  # Name
                    l1=graph[1]+':', l2=content[i][graph[1]],  # Location
                    d1=graph[2]+':', d2=content[i][graph[2]],  # Date buy
                    d3=graph[3]+':', d4=content[i][graph[3]],  # Date exchange
                    c1=graph[4]+':', c2=content[i][graph[4]],  # Cost
                    c3=graph[5]+':', c4=content[i][graph[5]],  # Cost exchange
                    t1=graph[6]+':', t2=', '.join(content[i][graph[6]]),  # Tags
                    dash='-'*80, i=indent))
    add_content = []
    for i in range(len(graph)):
        while True:
            if(i == 6):
                in_content = str(input('{:{}}'.format(graph[i]+':', indent)))
                in_content = in_content.split(', ')
                break
            else:
                in_content = str(input('{:{}}'.format(graph[i]+':', indent)))
                if(len(in_content) > 100):
                    print('100 characters maximum')
                else:
                    break
        add_content.append(in_content)
        json_content[graph[i]] = add_content[i]
    json_content['Date add'] = str(datetime.now())
    with open(db, 'r') as file:
        content = json.load(file)
    with open(db, 'w') as file:
        content['header']['last update'] = str(datetime.now())
        content[''.join(element)] = json_content
        json.dump(content, file, indent=4, sort_keys=True)
    backup()


def item_delete(element):
    with open(db, 'r') as file:
        content = json.load(file)
        content.pop(''.join(element))
    with open(db, 'w') as file:
        content['header']['last update'] = str(datetime.now())
        json.dump(content, file, indent=4, sort_keys=True)
    backup()


def search_tag(tag_list):
    result_list = []
    with open(db, 'r') as file:
        content = json.load(file)
    for i in sort_list(content):
        result = list(set(tag_list) & set(content[str(i)][graph[6]].split(', ')))
        if(len(result) == len(tag_list)):
            i = str(i)
            result_list.append(content[i][graph[0]])
    if(len(result_list) > 0):
        for i in result_list:
            print(i)
    else:
        print('Nothing find')


def remove_base():
    with open(db, 'r') as file:
        content = json.load(file)
    with open(db, 'w') as file:
        content.clear()
        content['header'] = header
        json.dump(content, file, indent=4, sort_keys=True)


def backup():
    with open(db, 'r') as file:
        content = json.load(file)
        last_update = content['header']['last update']
    try:
        backup = os.listdir('backups')
    except FileNotFoundError:
        os.mkdir('backups')
        backup = os.listdir('backups')
    if(last_update[:10]+'.data' in backup):
        with open('backups/'+str(datetime.now())[:10]+'.dat', 'w') as file:
            json.dump(content, file, indent=4)
    else:
        with open('backups/'+str(datetime.now())[:10]+'.dat', 'w') as file:
            json.dump(content, file, indent=4)
        if(len(backup) >= 5):
            os.remove('backups/'+backup[0])
        else:
            pass


if __name__ == '__main__':
    init()
