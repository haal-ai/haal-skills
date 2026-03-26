# Python: Use snake_case for Functions and Variables

Use `snake_case` for functions, methods, variables, and module names. Use `PascalCase` for classes. Use `UPPER_SNAKE_CASE` for module-level constants.

## Why

These are PEP 8 conventions followed by the entire Python ecosystem. Inconsistent naming makes code harder to read and collaborate on.

## Bad

```python
def GetUser(userId):  # ❌ PascalCase function
    userRecord = db.find(userId)  # ❌ camelCase variable
    return userRecord

MAX_retries = 3  # ❌ mixed case constant
```

## Good

```python
def get_user(user_id: str) -> User:  # ✅ snake_case function + parameter
    user_record = db.find(user_id)  # ✅ snake_case variable
    return user_record

MAX_RETRIES = 3  # ✅ UPPER_SNAKE_CASE constant

class UserService:  # ✅ PascalCase class
    pass
```

## Languages

- Python
