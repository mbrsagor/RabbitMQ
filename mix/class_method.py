class User(object):

    @classmethod
    def get_full_name(cls, first_name, last_name):
        print(f"Full Name is: {first_name} {last_name}")

    @staticmethod
    def get_name(name):
        print(f"Hello {name}")


if __name__ == '__main__':
    User.get_full_name('mbr', 'sagor')
    User.get_name('sagor')
