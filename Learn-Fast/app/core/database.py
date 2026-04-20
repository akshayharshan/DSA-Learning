from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase

DATABASE_URL = 'postgres:///'

engine = create_engine(DATABASE_URL)
localSession = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass


def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()



from sqlalchemy import Integer,String,Foreign_key,Column
from sqlalchemy.orm import relationship

class User:
    __table__ = 'users'

    id  = Column(Integer,primary_key=True,index=True)
    name  = Column(String)
    email = Column(String)

    orders = relationship("Order",back_populate=("users"))

class Order:
    __table__ = 'orders'

    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,Foreign_key('users.users_id'),index=True)
    amount = Column(float)

    users = relationship("User", back_populates=("orders"))


from fastapi import FastAPI,Depends
from sqlalchemy.orm import session,Select
from app.core.database import get_db
from app.models import User



app = FastAPI()

@app.get('/users')
def get_users(db : session = Depends(get_db)):
    stmt = Select(User).all()
    result = db.execute(stmt)
    return result.scalar()



class Base(DeclarativeBase)
    pass


from sqlalchemy import Integer,Column,String,ForiegnKey,Float
from sqlalchemy import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    email = Column(String)

    orders = relationship("Order",back_populates="user")


class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer,primary_key=True,index=False)
    user_id = Column(ForiegnKey("users.id"))
    amount = Column(float)

    user = relationship("User",back_popualates='orders')


## just the query
# get all users

stmt = select(User)
result = db.execute(stmt)
return result.scalars().all()


## filter
stmt = select(User).where(User.id == 1)
result = db.execute(stmt)
return result.scalar_one_or_none()

 ## create
user = User(name="akshay",email="a@gmail.com")
db.add(user)
db.commt()

##update

user = db.get(User, 1)
user.name = "arun"
db.commit()

## delete

user = db.get(User, 1)
db.delete(user)
db.commit



user = db.get(user.id,1)
user.name = 'new'
db.commit()



stmt = select(User.name,Order.amount).join(Order)
resut = db.execute(stmt).all()


from sqlalchemy import func

stmt = select(User.name, fun.count(order.id)).group_by(User.id)
result = db.execute(stmt).all()


stmt = select(User).outerjoin(Orders).where(Order.id == None)


1# if we can update or change after the object creation is mutable and a immutable is where we cannot change the object after its creation
2# generator is a function that using yeild to return the value one by one rather thatloading everything to memeory once
3# global interpreter lock is actually used to avoid the pythonccode to run on multiple threads only execute one at a time
4# list is mutable but tuple is immutable but the tuple is fater than list
5# decorator is a function that extend other function without explicity write code inside the function
6# oop is called object oriented programing which help to reuse the code and make more structured coding
# which include major concepts like abstraction,encapsulation,polymorphism,inheritance
#7 static method doest need any arguments like cls it just standalone method used as utility methods and have no idea about the clas even it exist
# but class method take cls as argument it can be used to change the state of the class and know what class it belongs
FastAPI
#1 dependency injection is used to reuse the code without repeating every function
# 2depends() depends is actually used to inject the class in fast api we inject Depends(get_db) on every route to pass the db for db operation in each reauest
#3 engine = make_engine(DATABASE_URL)
#   sessionLocal = sessionmaker(bind=engine)   
    # def function get_db():
    #     db = sessionLocal()
    #     try:
    #         yeild db
    #     finally:
    #         db.close()

# 4) middleware is used to modify or have to do some modificatioperation before and after the request processed
# 5) sync is actually when is sent the thread have to wait for the response till that time it cant able to handle another request i/o task but when async intoduced the fast api AGI server can handle i/o bounded task so if a request took longer time to respond the allocate to another request to handle in mean time as the event loop handle it well the system willl much faster 



SQL

#1) SELECT  name salary FROM employees MAX(salary)
# where salary < (SELECT MAX(salary) FROM employees)

#2) left join, right join , inner join

#3) where is used for applying filter for rows before the aggregation but having is used to do filter after the aggregation

#4) SELECT users.name FROM users
# LEFT JOIN orders ON users.id = orders.user_id where orders.id IS NULL
# indexing is making the quering very fast but it increase the table size and slows writes

System / Real-world

1 # i will exmine the api and check what make it slow 

#  is there any unwanted loops are there or delaying things in the code and examine the query the database whetehr it is loading unwanted joins or data pulling from the database like created_at , upadated_at and try to add pagination if the data pulling is really big and think about caching to avoid the continues database query to database example like in a listing page we have to how basic information like title , description etc so then we can use elastic search and while click on one card it will call a query to database , quick searching can be move to there

2 # i will design the backend system based on the data and users the app is exposed to if the system is used by millions of people then scalability is a matter so i will think about microservices which service needed to move on to the microservice ? use laod balancers like trafiek to balance and route the requests and in code level i can use service repo pattern like bsiness logic will put in another file and repository will used for db query as sepertion is there it is easy for testing that th way i think

3#) first decide the what is the spec of the vps server i have to brought how much ram and core processer should neeed to runmy app optimal and but that and i have the docker use the docker images i buld the app including a nginx should be add as a service and might if it is a simple app the nginx will be configurede to listen to the post move the production file to there through git  





stmt = select(User.name,Order.name).join(Order)
resukt = db.execute(stmt).scalars().all()

user = User(id,1)
db.delete(user)
db.commit

user = User(id,1)
user.name = "new"
db.commit

user = User(name="akshay", email = "a@gmail.com")
db.add(user)
db.commit()














































