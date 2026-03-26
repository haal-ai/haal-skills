---
inclusion: manual
---

# Python: Use Type Hints on All Functions

Add type hints to all function parameters and return types.

## Why

Type hints enable static analysis (mypy, pyright), improve IDE autocompletion, and serve as documentation. They catch type errors before runtime.

## Bad

```python
def get_user(user_id):  # ❌ no type hints
    return db.find(user_id)

def process(items, max_count):  # ❌
    return items[:max_count]
```

## Good

```python
from typing import Optional

def get_user(user_id: str) -> Optional[User]:  # ✅
    return db.find(user_id)

def process(items: list[str], max_count: int) -> list[str]:  # ✅
    return items[:max_count]
```

## Languages

- Python

