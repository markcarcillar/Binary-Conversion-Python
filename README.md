# Binary To Decimal

### Description
  - This is made in python. It converts binary number to decimal number. It accepts either string or integer data type. It has `BinaryToDecimal` class and it is the one that you will use to convert binary number into decimal number.

### How to use
  1. First make sure that script.py is in your same directory with your project, then in your file import `BinaryToDecimal` class.
```python
from script import BinaryToDecimal
```
  2. Now use the `BinaryToDecimal` class. When using this make sure the value for its object is binary number. Such as **101010**.
```python
BinaryToDecimal(101010)
```
  3. Try using `BinaryToDecimal` class with not a binary number.
```
ValueError: This value is not binary. Make sure it only contains 0 or 1 and not start with 0.
```
  4. Get the decimal value of binary number
```python
binary = BinaryToDecimal(101010)
print(binary.decimal) # Use the decimal property
```

### Complete code example
  ```python
    from script import BinaryToDecimal

    # Create instance of BinaryToDecimal class
    two_bits_binary = BinaryToDecimal(10)
    four_bits_binary = BinaryToDecimal(1110)
    eight_bits_binary = BinaryToDecimal(11101110)
    sixteen_bits_binary = BinaryToDecimal(1110111011101110)

    # Check if the decimal value is correct
    assert two_bits_binary.decimal == 2
    assert four_bits_binary.decimal == 14
    assert eight_bits_binary.decimal == 238
    assert sixteen_bits_binary.decimal == 61166
  ```
