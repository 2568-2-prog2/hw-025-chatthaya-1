import unittest
from dice import Dice

class TestDice(unittest.TestCase):
    def setUp(self):
        self.dice = Dice()

    def test_roll_count(self):
        probs = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]
        result = self.dice.roll(probs, 10)
        self.assertEqual(len(result), 10)

    def test_roll_values(self):
        probs = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]
        result = self.dice.roll(probs, 100)
        for val in result:
            self.assertTrue(1 <= val <= 6)
            
    def test_heavy_weight_bias(self):
        heavy_probs = [0.02, 0.02, 0.02, 0.02, 0.02, 0.90]
        num_rolls = 5000
        result = self.dice.roll(heavy_probs, num_rolls)
        
        count_6 = result.count(6)
        percentage_6 = (count_6 / num_rolls) * 100
        
        self.assertGreater(percentage_6, 85)
        self.assertGreater(count_6, result.count(1) * 10)
        
if __name__ == '__main__':
    unittest.main()