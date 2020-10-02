# Datafile.py is used for accessing random data from Test_data.yaml file
import random
import yaml
import pathlib


class test_data():
    my_path = pathlib.Path(__file__).resolve()              # resolve to get rid of any symlinks
    data_path = my_path.parent / 'Test_data.yaml'

    with data_path.open() as test:
        data = yaml.safe_load(test)                         #load data from yaml file

    def email(self):
        email_list = self.data['Email']
        self.email = random.choice(email_list)
        return self.email

    def address(self):
        add_list = self.data['Address']
        self.addresses = random.choice(add_list)
        return self.addresses

    def phone_number(self):
        number = self.data['Phone_Number']
        self.phone = random.choice(number)
        return self.phone

    def Names(self):
        name_list = self.data['Names']
        self.name = random.choice(name_list)
        return self.name