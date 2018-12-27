import json

class Person:

    def __init__(self, first_name, last_name,
                 email, gender, ip_address):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.ip_address = ip_address

    def make_printout(self):
        txt = ''
        txt = txt + '\nFirst name: {0}'.format(self.first_name)
        txt = txt + '\nLast name: {0}'.format(self.last_name)
        txt = txt + '\nEmail: {0}'.format(self.email)
        txt = txt + '\nIP Address: {0}'.format(self.ip_address)
        print(txt)


with open('MOCK_DATA.json') as f:
    data = json.load(f)

#for first in data:
#    print(first['first_name'])

for line in data:
    person = Person(line['first_name'], line['last_name'], line['email'], line['gender'], line['ip_address'])
    person.make_printout()
