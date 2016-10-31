import hashlib

class User:
    username=""
    password=""
    age=0
    email=""

    def update_pw(unhashed):
        mho=hashlib.sha1()
        mho.update(unhashed)
        self.pw=mho.hexdigest()

    def update():
