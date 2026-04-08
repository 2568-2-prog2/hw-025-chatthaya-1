import random
class Dice:
    def roll(self, probabilities, num_rolls):
        faces = [1,2,3,4,5,6]
        results = random.choices(faces, weights=probabilities, k=num_rolls)
        return results