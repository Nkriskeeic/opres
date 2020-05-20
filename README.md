# Opres

## What's this.

This module enables you to use Option and Result types in your Python project.

## How to use.

1. install this module

```shell script
pip install git+https://github.com/Nkriskeeic/opres
``` 

2. import `opres` in your script

```python
from opres import Option, Some, Nothing, Result, Ok, Err

some_var = Some([100, 200])
sum_of_some_var = some_var.map(sum).unwrap()  # your editor will interpret `sum_of_some_var` as an integer

res_var = Ok("text")
length_of_text = res_var.map_or(len, 0)  # 4

res_var = Err("not found")
length_of_text = res_var.map_or(len, 0)  # 0
```

## examples

Please see `examples` or `tests`.


## Support

### Option[T]

- `unwrap() -> T`
- `unwrap_or(default: T) -> T`
- `unwrap_or_else(default_func: Callable[[], T]) -> T`
- `is_nothing() -> bool`
- `is_some() -> bool`
- `expect(message: str) -> T`
- `map(f: Callable[[T], S]) -> Option[S]`
- `map_or(f: Callable[[T], S], default: S) -> Option[S]`
- `map_or_else(f: Callable[[T], S], default_func: Callable[[], S]) -> Option[S]`
- `ok_or(err: E) -> Result[T, E]`
- `ok_or_else(err_func: Callable[[], E]) -> Result[T, E]`

### Result[T, E]

- `unwrap(self) -> T`
- `unwrap_err(self) -> E`
- `unwrap_or(self, default: T) -> T`
- `unwrap_or_else(self, default_func: Callable[[], T]) -> T`
- `is_ok(self) -> bool`
- `is_err(self) -> bool`
- `expect(self, message: str) -> T`
- `map(self, f: Callable[[T], S]) -> Result[S, E]`
- `map_or(self, f: Callable[[T], S], default: S) -> Result[S, E]`
- `map_or_else(self, f: Callable[[T], S], default_func: Callable[[], S]) -> Result[S, E]`
- `ok(self) -> Option[T]`
- `err(self) -> Option[E]`

## License
MIT
