# Ans for Q1 and Q2

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def get_details(self):
        return self.name , self.salary


obj1 = Employee('akshay',20000)
print(obj1.get_details())
obj2 = Employee('aravind',40000)
print(obj2.get_details())

# Q3) Encapsulation


class Employee:
    def __init__(self,name,salary = 0):
        self.name = name
        self._salary = salary
    def get_details(self):
        return self.name , self.salary
    def update_salary(self,amount):
        self.__salary = amount



obj = Employee('akshay',20000)
obj.get_details()
obj.update_salary(30000)



# Q4) Encapsulation

class Manager(Employee):

    def __init__(self,department):
        self.department = department

    def get_details(self):
        return self.department
# polymorphism
class Dog:
    def speak(self):
        return "boww"

class Cat:
    def speak(self):
        return "meow"

dog = Dog()
dog.speak()
cat = Cat()
cat.speak()

# static method
class User:
    count = 0
    @classmethod
    def __init__(cls):
        cls.count+=1
    def is_valid_email(email):
        return str(email)
user = User()


# generator 
def generator(n):
    for i in range(1,n):
        yield i
for value in generator(3):
    print(value)



# Remove duplicates from list


def remove_duplicate(nums):
    seen = set()
    res = []

    for num in nums:
        if num not in seen:
            res.append(num)
            seen.add(num)
    return res

# Count frequency of characters in string

def count_freq(string):
    hashmap = {}
    for char in string:
        hashmap[char] = hashmap.get(char,0) + 1
    return hashmap



class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
    def withdraw(self,amount):
        if self.__balance() > 0:
            self.__balance -= amount
            return self.__balance
        else:
            return 0
    def get_balance(self):
        return self.__balance



account = BankAccount(1000)
account.deposit(1000)
account.withdraw(200)


def reverse(string):
    l = 0
    r = len(string) - 1
    string = list(string)
    while l < r:
        string[l],string[r] = string[r],string[l]
        l +=1
        r -= 1
    return "".join(string)

def first_non_reeat(string):

    hashmap = {}

    for char in string:
        hashmap[char] = hashmap.get(char,0)  + 1
    for char in string:
        if hashmap[char] == 1:
            return char




def reverse(string):
    l = 0
    r = len(string) - 1
    reverse = list(string)
    while l < r:
        reverse[l],reverse[r] = reverse[r],reverse[l]
        l +=1
        r -= 1
    reverse_str = "".join(reverse)
    if 

def merge_sorted_array(arr1,arr2):
    res = []
    l = 0
    r = 0
    while l < len(arr1) and r < len(arr2):
        if arr1[l] <= arr2[r]:
            res.append(arr1[l])
            l+=1
        else:
            res.append(arr2[r])
            r+=1
    if l < r:
        res.extend(arr2[r:])
    else:
        res.extend(arr1[l:])
    return res


list1 = [1, 3, 5, 7]
list2 = [2, 4]
print(merge_sorted_array(list1,list2)


def duplicates(nums):

    seen = set()
    for num in nums:
        if num in seen:
            return num
        else:
            seen.add(num)
    return None




print(duplicates([1, 3, 4, 2, 2]))


def two_sum(nums,target):
    hashmap = {}
    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in hashmap:
            return [i,hashmap[compliment]]
        hashmap[nums[i]] = i
    

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums,target))


def outer(func):
    def inner():
        print ("start")
        result = func()
        print(result)
        print("end")
    return inner




@outer
def test():
    return "hello"

test()




from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class credit(Payment):
    def pay(self,amount):
        return f"paid {amount} using credit card"




from fastapi import FastAPI ,Depends,create_engine
from sqlalchemy.orm import Session,Sessionmaker

app = FastAPI()

DATABASE_URL = "connection to db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=false,bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users")
def get_users(db: Session = Depends(get_db))
    return db.query(User).all()

@app.post("/users")
def create_user(name:str, db: Session = Depends(get_db))
    user = User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


try:
    result = some_function()
except Exception as e:
    print(str(e))


@app.post("/item")
def create_item(db : Session = Depends(get_db)):
    try:
        item = Item(name = "test")
        db.add(item)
        db.commit()
        return item
    except Exception as e:
        db.rollback()
        raise HttpException(status_code=500,detail=str(e))


from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

async def get_users(db:AsyncSession)
    stmt = select(User)
    result = await db.execute(stmt)
    return result.scalars(),all()


async def create_user(db:AsyncSession):
    user = User(name="akshay")
    db.add(user)

    await db.flush()

    print(user.id)
    await db.commit()
    return user