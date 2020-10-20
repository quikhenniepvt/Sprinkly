from passlib.apps import custom_app_context as pwd_context


class User:
    username = "quikhennie"
    password_hash = ""

    def __init__(self):
        print("checking user credentials!")
        password = "yUf@734Vk8(g9>:u";
        self.hash_password(password)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)
        print("hello"+self.password_hash)

    def verify_password(self, password):
        print("Checking pw " + password + " against " + self.password_hash)
        return pwd_context.verify(password, self.password_hash)
