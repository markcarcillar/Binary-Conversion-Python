import re

class BinaryToDecimal:
  def __init__(self, binary):
    ''' Check if the value is binary first before it save as instance of BinaryToDecimal class and have a decimal value '''
    if not self.is_binary(str(binary)):
      raise ValueError('This value is not binary. Make sure it only contains 0 or 1 and not start with 0.')
    self.binary = binary
  
  @property
  def decimal(self):
    ''' Returns the decimal value of binary number as integer data type '''
    decimal = 0
    bits = 1
    binary_as_list = ','.join(str(self.binary)).split(',')
    for count in range(len(binary_as_list)-1, -1, -1):
      if binary_as_list[count] == '1':
        decimal += self.base_of(bits)
      bits += 1
    return int(decimal)

  @staticmethod
  def base_of(bits):
    ''' 
      Returns base of bits.
      For instance, base of 8 bits is 128.
    '''
    base = 2**(bits-1)
    return base

  @staticmethod
  def is_binary(binary):
    '''
      Returns true if value only contains 0 or 1 and not start with 0, otherwise, false. 
      It accepts string or integer data type.
    '''
    if re.search(r'[^01]', binary):
      return False
    if len(binary) > 1:
      if binary.startswith('0'):
        return False
    return True