https://www.notion.so/skinetics/Installing-Numpy-Guide-c593cd18554d428087352306c3bf2c1f#63d4632d64a64769bf2a75f6a1dfd595

# Optimising Storage: Data Types

> In NumPy, though, there’s a little more detail that needs to be covered. NumPy uses C code under the hood to optimize performance, and it can’t do that unless all the items in an array are of the same type. That doesn’t just mean the same Python type. They have to be the same underlying C type, with the same shape and size in bits!

## Numerical types

[Numerical Types](https://www.notion.so/5ba6a618db6c4753b0d1bcee4dd02bae)

> [These are just the types that map to existing Python types. NumPy also has types for the smaller-sized versions of each, like 8-, 16-, and 32-bit integers, 32-bit single-precision floating-point numbers, and 64-bit single-precision complex numbers.](https://numpy.org/devdocs/user/basics.types.html)

Specify type when creating an array using the `dtype` argument:

```python
import numpy as np
a = np.array([1, 3, 5.5, 7.7, 9.2], dtype=np.single)
a
>>> array([1. , 3. , 5.5, 7.7, 9.2], dtype=float32)

b = np.array([1, 3, 5.5, 7.7, 9.2], dtype=np.uint8)
b
>>> array([1, 3, 5, 7, 9], dtype=np.uint8)
```

> NumPy automatically converts your platform-independent type `np.single` to whatever fixed-size type your platform supports for that size. In this case, it uses `np.float32`. If your provided values don’t match the shape of the dtype you provided, then NumPy will either fix it for you or raise an error.