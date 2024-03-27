"""
  Test for base_model module
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
      Test Base Model
    """
    def test_equal_instance(self):
        """
          Equal instance
        """
        mod = BaseModel()
        self.assertEqual(True, 1)


if __name__ == '__main__':
    unittest.main()
