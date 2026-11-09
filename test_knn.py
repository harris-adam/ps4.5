# test_knn.py
# David Kopec
# MIT License
import unittest
from knn import Fish, read_fish_CSV, nearest, classify, predict
from pathlib import Path


class KNNTestCase(unittest.TestCase):
    def test_nearest(self):
        k: int = 3
        p = Path(__file__).with_name('Fish.csv')
        all_fish = read_fish_CSV(p.absolute())
        test_fish: Fish = Fish("", 0.0, 30.0, 32.5, 38.0, 12.0, 5.0)
        nearest_fish: list[Fish] = nearest(k, test_fish, all_fish)
        self.assertEqual(len(nearest_fish), k)
        expected_fish = [Fish(species='Bream', weight=340.0, length1=29.5, length2=32.0, length3=37.3, height=13.9129, width=5.0728), Fish(species='Bream', weight=500.0, length1=29.1, length2=31.5, length3=36.4, height=13.7592, width=4.368), Fish(species='Bream', weight=700.0, length1=30.4, length2=33.0, length3=38.3, height=14.8604, width=5.2854)]
        self.assertEqual(nearest_fish, expected_fish)

    def test_classify(self):
        k: int = 5
        p = Path(__file__).with_name('Fish.csv')
        all_fish = read_fish_CSV(p.absolute())
        test_fish: Fish = Fish("", 0.0, 20.0, 23.5, 24.0, 10.0, 4.0)
        classify_fish: str = classify(k, test_fish, all_fish)
        self.assertEqual(classify_fish, "Parkki")

    def test_predict(self):
        k: int = 5
        p = Path(__file__).with_name('Fish.csv')
        all_fish = read_fish_CSV(p.absolute())
        test_fish: Fish = Fish("", 0.0, 20.0, 23.5, 24.0, 10.0, 4.0)
        predict_fish: float = predict(k, test_fish, all_fish)
        self.assertEqual(predict_fish, 165.0)


if __name__ == '__main__':
    unittest.main()


