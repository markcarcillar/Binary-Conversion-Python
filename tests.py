from unittest import TestCase

from script import BinaryToDecimal

class BinaryToDecimalTests(TestCase):
  def setUp(self):
    self.two_bits_binary = BinaryToDecimal(10)
    self.four_bits_binary = BinaryToDecimal(1110)
    self.eight_bits_binary = BinaryToDecimal(11101110)
    self.sixteen_bits_binary = BinaryToDecimal(1110111011101110)
    
  def test_not_valid_when_value_contains_metacharacter__letter__or_starts_with_0(self):
    self.assertRaises(ValueError, BinaryToDecimal, '0101^$()*+') # metacharacters
    self.assertRaises(ValueError, BinaryToDecimal, 'Hello01world') # letters
    self.assertRaises(ValueError, BinaryToDecimal, '01110') # starts with 0 even its binary
  
  def test_base_of_method(self):
    self.assertEqual(BinaryToDecimal.base_of(2), 2)
    self.assertEqual(BinaryToDecimal.base_of(4), 8)
    self.assertEqual(BinaryToDecimal.base_of(8), 128)
    self.assertEqual(BinaryToDecimal.base_of(16), 32768)
  
  def test_decimal_property(self):
    self.assertEqual(self.two_bits_binary.decimal, 2)
    self.assertEqual(self.four_bits_binary.decimal, 14)
    self.assertEqual(self.eight_bits_binary.decimal, 238)
    self.assertEqual(self.sixteen_bits_binary.decimal, 61166)
    
    # More
    self.assertEqual(BinaryToDecimal(0).decimal, 0)
    self.assertEqual(BinaryToDecimal(1).decimal, 1)
    self.assertEqual(BinaryToDecimal(1011).decimal, 11)
    self.assertEqual(BinaryToDecimal(1111).decimal, 15)
    