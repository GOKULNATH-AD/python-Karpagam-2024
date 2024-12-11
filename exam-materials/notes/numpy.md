# NUMPY

    numpy is a package
    numpy.ndarray is a class

    We can use np.array() function to create
        an array in numpy.
  
    attributes: 
       - size
       - shape
       - ndim
    operator overloading possible:
       + ( add )
       == ( equal to )
       * ( multiple ) ( 2 ways )
       ** ( pow )
    methods:
       - sum
       - min
       - max
       - mean

```python
>>> import numpy as np
>>> arr1 = np.array([ 34, 21, 11])
>>> arr1.ndim
1
>>> arr1.size
3
>>> arr1.shape
(3,)

>>> arr1
array([34, 21, 11])
>>> arr1 * 10
array([340, 210, 110])

>>> arr1 = np.array([1,2,3])
>>> arr1
array([1, 2, 3])
>>> arr1 = arr1 * 10
>>> arr1
array([10, 20, 30])
>>> arr1.sum()
np.int64(60)
>>> int(arr1.sum())
60

>>> arr1
array([10, 20, 30])
>>> arr1.max()
np.int64(30)
>>> arr1.min()
np.int64(10)
>>> arr1.mean()
np.float64(20.0)
```
