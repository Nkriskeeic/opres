# Opres

## What's this.

This module enables you to use Option and Result types in your Python project.

## How to use.

1. install this module

```shell script
pip install git+{URL}
``` 

2. import `opres` in your script

```python
from opres import Option, Some, Nothing, Result, Ok, Err
from typing import List

some_var = Some([100, 200])
sum_of_some_var = some_var.map(sum).unwrap()  # your editor will interpret `sum_of_some_var` as an integer

res_var = Ok("text")
length_of_text = res_var.map_or(len, 0)  # 4

res_var = Err("not found")
length_of_text = res_var.map_or(len, 0)  # 0
```

## License
MIT
