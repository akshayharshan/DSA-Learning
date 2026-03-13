# FastAPI Interview Prep – Day 1 Notes

## Goal of Day 1

Understand the **core FastAPI fundamentals** required for backend interviews.

Topics covered:

* Routers
* Dependency Injection
* Database session handling
* Pydantic schemas
* Error handling
* FastAPI request flow

---

# 1. FastAPI Request Flow

A request in FastAPI typically flows like this:

```
Client Request
      ↓
Router / Endpoint
      ↓
Dependency Injection
      ↓
Service Logic
      ↓
Repository / Database
```

Understanding this flow is important for backend interviews.

---

# 2. Router Structure

Routers help organize endpoints into modules.

### Example Router

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    return {"message": "ok"}
```

### Including Router in `main.py`

```python
from fastapi import FastAPI
from app.api.users import router

app = FastAPI()

app.include_router(router, prefix="/users")
```

Endpoint becomes:

```
GET /users
```

### Interview Answer

**Why use routers?**

Routers help modularize APIs by separating endpoints into different modules (users, orders, products).

---

# 3. Dependency Injection

FastAPI allows injecting dependencies into endpoints.

Example: database session.

```python
from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.database import get_db

@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return []
```

### Key Rule

```
Depends(get_db)   ✅
Depends(get_db()) ❌
```

`Depends(get_db())` incorrectly executes the function immediately.

### Interview Answer

Dependency injection allows reusable logic (database sessions, authentication, permissions) to be automatically provided to endpoints.

---

# 4. Database Session Dependency

Typical database dependency:

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### Why use `yield`?

Because FastAPI executes the code **after the request finishes**, ensuring the database session is closed.

Flow:

```
Request starts
↓
get_db() creates session
↓
Endpoint uses session
↓
Request finishes
↓
finally block closes session
```

### Problem if using `return`

If we wrote:

```python
def get_db():
    return SessionLocal()
```

The session might **not close properly**, which can exhaust database connections.

---

# 5. Pydantic Request Schema

FastAPI uses **Pydantic models** for request validation.

Example:

```python
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
```

Example request body:

```json
{
  "name": "Akshay",
  "email": "akshay@test.com",
  "password": "secret"
}
```

### Why use Pydantic?

* Data validation
* Automatic documentation
* Type safety
* Serialization

---

# 6. Error Handling

FastAPI provides `HTTPException` for structured errors.

Example:

```python
from fastapi import HTTPException

if not user:
    raise HTTPException(status_code=404, detail="User not found")
```

### Important Rule

```
raise HTTPException(...)   ✅
return HTTPException(...)  ❌
```

---

# 7. Minimal Imports to Remember

You only need to remember a few core imports:

### FastAPI

```python
from fastapi import APIRouter, Depends, HTTPException
```

### Pydantic

```python
from pydantic import BaseModel
```

### SQLAlchemy

```python
from sqlalchemy.orm import Session
```

---

# 8. Core FastAPI Patterns to Memorize

### Router Pattern

```python
router = APIRouter()

@router.get("/")
def home():
    return {"message": "ok"}
```

### DB Dependency Pattern

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### CRUD Pattern

```python
db.add(obj)
db.commit()
db.refresh(obj)
```

### Error Pattern

```python
raise HTTPException(status_code=404, detail="Not found")
```

---

# 9. Common Interview Questions (Day 1)

### What is Dependency Injection?

Dependency injection allows reusable logic (like DB sessions or authentication) to be injected into endpoints automatically.

---

### Why use Routers?

Routers help modularize large APIs by separating endpoints into domain-specific modules.

---

### Why use Pydantic?

Pydantic validates request data and ensures type safety.

---

### Why use `yield` in `get_db()`?

Using `yield` allows FastAPI to execute cleanup code after the request finishes, ensuring the database session closes properly.

---

# Day 1 Summary

Today we covered:

* FastAPI router structure
* Dependency injection
* DB session lifecycle
* Request validation using Pydantic
* Error handling with HTTPException

These topics form **the foundation of most FastAPI backend interviews**.

---

# Next Step (Day 2)

Focus on **SQLAlchemy interview topics**:

* Models
* `Mapped` and `mapped_column`
* Relationships
* Many-to-many tables
* `joinedload()` to avoid N+1 queries
* `flush` vs `commit`

These topics are **very common in Python backend interviews**.
