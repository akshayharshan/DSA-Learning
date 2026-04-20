class User:
    base_level_access = "Guest" ## class attribute
    def __init__(self,name,age):
        self.name = name ## instance attribute
        self.age = age
    
    @classmethod
    def from_string(cls,data):
        name,age = data.split_str("-")
        return cls(name,age)
    
    @classmethod
    def set_default_access(cls,level):
        cls.base_level_access = level


    @staticmethod
    def is_adult(age):
        if age >= 18:
            return True


print(User.is_adult("25"))

new_user = User.from_string("ALICE-30")
print(f"Name: {new_user.name},Age:{new_user.age}")

User.set_default_access("Mmeber")


