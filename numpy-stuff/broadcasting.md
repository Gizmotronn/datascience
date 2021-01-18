# [Broadcasting](https://www.notion.so/skinetics/Installing-Numpy-Guide-c593cd18554d428087352306c3bf2c1f#c361d05edce14df7961f5c9275ad9852)

Arrays can be broadcast around each other if their dimensions match or if one of the arrays has a size of 1

If the arrays size is equal, then elements will be operated on element-by-element:

```py
In [1]: a = [5.0, 6.0, 7.0]
In [2]: b = [5.0, 7.0, 3.0]
In [3]: a * b
Out [3]: [25, 42, 21] ```

If one of the arrays has size=1, then that array will be broadcast around the other array entirely:

In [1]: a = [5.0, 6.0, 7.0] In [2]: b = [2.0] In [3]: a * b Out[3]: [10.0, 12.0, 14.0] 

Another example:

Array a has the shape [4, 1, 8] and array b has the shape [1, 6, 8]

In [1]: a = ([ 1, 2, 3, 4, 	5, 	6, 7, 8, 9, 10, 11, 12, 13 
