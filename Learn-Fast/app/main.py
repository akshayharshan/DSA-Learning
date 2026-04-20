from fastapi import FastAPI



app = FastAPI()



def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()
def generator(n):
    for i in range(n):
        yield i

print(generator(3))

    




from jose import jwt
from datetime import datetime, timedelta
SECRET_KEY = 'SECRET'
ALGORITHM = 'HS256'
def create_token(data:list):
    to_encode = data.copy()
    exp = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp":exp})
    token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token


from jose import jwt


def decode_token(token:str):
    payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
    return payload


import logging

logging.basicConfig(level=logging.INFO)
logging.info("user created")




from fastapi import Request
@app.middleware('http')
async def log_requests(request:Request,call_next):
    print("log before")
    response = await call_next(request)
    print("after request")
    return response



Rate limiting
Pagination (you already mentioned 👍)
Basic security (input validation)


We can also use HTTPS, secure storage like HttpOnly cookies, and token blacklisting for better security.”