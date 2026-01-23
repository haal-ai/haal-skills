# Anti-patterns to Avoid

## Avoid Windows-style Paths

Always use forward slashes in file paths, even on Windows:

- ✓ Good: `scripts/helper.py`, `reference/guide.md`
- ✗ Avoid: `scripts\helper.py`, `reference\guide.md`

Unix-style paths work across all platforms, while Windows-style paths cause errors on Unix systems.

## Avoid Offering Too Many Options

Don't present multiple approaches unless necessary:

**Bad example: Too many choices** (confusing):
```
"You can use the Strategy pattern, or the Factory pattern, or the Builder pattern, or the Abstract Factory, or..."
```

**Good example: Provide a default** (with an alternative when needed):
```
"Use the Strategy pattern for swappable behaviors:
```python
class PaymentStrategy(ABC):
    @abstractmethod
    def process(self, amount): pass
```

For object creation with many optional parameters, use the Builder pattern instead."
```
