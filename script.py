import re

class BinaryToDecimal:
  def __init__(self, binary):
    if not self.is_binary(binary):
      raise ValueError('This value is not binary. Make sure it only contains 0 or 1 and not start with 0.')
    self.binary = binary
  
  @property
  def decimal(self):
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
    base = 2**(bits-1)
    return base

  def is_binary(self, binary):
    binary = str(binary)
    if re.search(r'[a-zA-Z2-9\W\s]', binary):
      return False
    if len(binary) > 1:
      if binary.startswith('0'):
        return False
    return True