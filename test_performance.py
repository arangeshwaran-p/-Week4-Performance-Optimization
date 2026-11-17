import unittest
from original import count_unique_items as original_count
from optimized import count_unique_items as optimized_count
class TestUniqueCounter(unittest.TestCase):
    def test_repeated_values(self):
        data=[1,2,2,3,3,3]; self.assertEqual(original_count(data),3); self.assertEqual(optimized_count(data),3)
    def test_empty_list(self):
        self.assertEqual(original_count([]),0); self.assertEqual(optimized_count([]),0)
    def test_all_unique(self):
        data=[1,2,3,4]; self.assertEqual(original_count(data),4); self.assertEqual(optimized_count(data),4)
    def test_large_dataset(self):
        data=[i%1500 for i in range(12000)]; self.assertEqual(original_count(data),optimized_count(data)); self.assertEqual(optimized_count(data),1500)
if __name__=="__main__": unittest.main()
