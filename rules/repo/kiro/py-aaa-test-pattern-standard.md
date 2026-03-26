---
inclusion: manual
---

# Python: Structure Tests with Arrange-Act-Assert

Structure all test functions with a clear Arrange / Act / Assert flow. Do not mix setup and assertions.

## Why

AAA structure makes tests readable and maintainable. A single `act` step and a single `assert` step make failures easy to diagnose.

## Bad

```python
def test_user_creation():
    assert UserService().create("alice", "alice@example.com").name == "alice"  # ❌ all in one line
```

## Good

```python
def test_user_creation():
    service = UserService()                          # Arrange

    user = service.create("alice", "alice@x.com")   # Act

    assert user.name == "alice"                     # Assert
```

## Languages

- Python

