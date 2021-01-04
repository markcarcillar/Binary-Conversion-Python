# Binary Conversion - Python

[![My website](https://img.shields.io/badge/CLeDiscover-Clever%2C%20let's%20discover!-brightgreen?style=for-the-badge&logo=appveyor&logo=superuser)](https://clediscover.xyz)

[![GitHub stars](https://img.shields.io/github/stars/clediscover/Binary-Conversion-Python)](https://github.com/clediscover/Binary-Conversion-Python/stargazers)
[![GitHub license](https://img.shields.io/github/license/clediscover/Binary-Conversion-Python)](https://github.com/clediscover/Binary-Conversion-Python/blob/master/LICENSE.md)

### Description
  - A python module that has a conversion for binary to decimal and decimal to binary number.

### How to use
  - For more information check tests.py file.

  #### Steps for Binary to Decimal
  1. Import `BinaryToDecimal` class.
```python
from script import BinaryToDecimal
```
  2. Now use the `BinaryToDecimal` class. When using this make sure the value for its object is binary number. It accepts string or integer data type. Such as **101010** and **'101010'**.
```python
BinaryToDecimal(101010)
BinaryToDecimal('101010')
```
  3. Try using `BinaryToDecimal` class with not a binary number.
```
ValueError: This value is not binary. Make sure it only contains 0 or 1 and not start with 0.
```
  4. Get the decimal value of binary number.
```python
binary = BinaryToDecimal(101010)
print(binary.decimal) # Use the decimal property
```

  #### Steps for Decimal to Binary
  1. Import `DecimalToBinary` class.
```python
from script import DecimalToBinary
```
  2. Now use the `DecimalToBinary` class. When using this make sure the value for its object is decimal. It accepts string or integer data type. Such as **8672** and **'8672'**.
```python
DecimalToBinary(8672)
DecimalToBinary('8672')
```
  3. Try using `DecimalToBinary` class with not a decimal number.
```
ValueError: This value is not decimal. Make sure it only contains 0-9 and not start with 0.
```
  4. Get the binary value of decimal number.
```python
decimal = DecimalToBinary(101010)
print(decimal.binary) # Use the binary property
``` 

### Complete code example
  ```python
    from script import BinaryToDecimal, DecimalToBinary

    # Create an instance of BinaryToDecimal and DecimalToBinary class
    # BinaryToDecimal
    two_bits_binary = BinaryToDecimal('10')
    four_bits_binary = BinaryToDecimal(1110)
    eight_bits_binary = BinaryToDecimal(11101110)
    sixteen_bits_binary = BinaryToDecimal(1110111011101110)
    # DecimalToBinary
    two_digits_decimal = DecimalToBinary('15')
    four_digits_decimal = DecimalToBinary(2_304)
    eight_digits_decimal = DecimalToBinary(1_0089_109)
    sixteen_digits_decimal = DecimalToBinary(1_008_910_910_089_109)

    # Check if the decimal and binary value is correct
    # Assertion for BinaryToDecimal
    assert two_bits_binary.decimal == 2
    assert four_bits_binary.decimal == 14
    assert eight_bits_binary.decimal == 238
    assert sixteen_bits_binary.decimal == 61166
    # Assertion for DecimalToBinary
    assert two_digits_decimal.binary == 1111
    assert four_digits_decimal.binary == 100100000000
    assert eight_digits_decimal.binary == 100110011111001010010101
    assert sixteen_digits_decimal.binary == 11100101011001100101100000011001111110011110010101
  ```
