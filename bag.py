import datetime
from pathlib import Path

class Bag:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.fill()

    def fill(self):
        self.file = open(self.filename, 'r')
        self.users = {}

        for line in self.file:
            email, password, name, dataloc, created = line.strip().split(";")
            # load the data from it's file here
            # then you can place the data in the file here.
            self.users[email] = (password, name, dataloc, created)
            # self.users[email] = (password, name, dataloc, created, saved, data)
        self.file.close()


    def load_data(self, dataloc):
        pass
        # we need to open the data
        # add the data to the user
        # close the file. FOR SAFETY!

    def save_data(self, user):
        pass

    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return -1

    def rm_char(self, s, ss):
        if ss in s:
            blank = ''
            s = s.replace(ss, blank)
            print(s)
            return s
        else:
            return s

    def add_user(self, email, password, name):
        if email.strip() not in self.users:
            dataloc = email
            dataloc = self.rm_char(dataloc, '@')
            dataloc = self.rm_char(dataloc, '.')
            d = self.get_folder(dataloc)
            self.users[email.strip()] = (password.strip(),
            name.strip(), dataloc.strip(), Bag.get_date())
            self.save()
            return 1
        else:
            print("email in use")
            return -1

    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False

    def get_folder(self, f):
        current_location = Path.cwd()
        f = current_location / f
        found = False
        for x in current_location.iterdir():
            if x.is_dir():
                if x == f:
                    print('aha!')
                    return f
                else:
                    print("{} is not my folder".format(x))
            else:
                print('{} is not a folder'.format(x))
        print('prolly should make that up!!')
        f = self.make_new_folder(f)
        return f

    def make_new_folder(self, f):
        current_location = Path.cwd()
        f = current_location / f
        Path.mkdir(f)
        return f

    def save(self):
        d8 = datetime.datetime.strftime(datetime.datetime.now(),"%m/%d-%H:%M%S")

        for user in self.users:
            dl = str(users[user][3])
            p = Path.cwd()
            p = p / dl


    # should probably save the data first, then you can save where it is.
        with open(self.filename, 'w') as f:
            for user in self.users:
                f.write(user + ";" +
                    self.users[user][0] + ";" +
                    self.users[user][1] + ";" +
                    self.users[user][2] + ";" +
                    self.users[user][3] + "\n")

        # for user in self.users:
        #     locay =
        #     with open()

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]


if '__name__'== '__main__':
    fn = input("a name for your bag:")
