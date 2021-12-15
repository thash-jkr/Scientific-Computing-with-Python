import copy
import random


class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for k, v in kwargs.items():
      for i in range(v):
        self.contents.append(k)

  def draw(self, num):
    if num >= len(self.contents):
      balls = self.contents
    else:
      balls = []
      for i in range(num):
        b = random.choice(self.contents)
        balls.append(b)
        self.contents.remove(b)

    return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  N = num_experiments
  M = 0
  for i in range(N):
    expected_copy = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)
    colours = hat_copy.draw(num_balls_drawn)

    for colour in colours:
      if colour in expected_copy:
        expected_copy[colour] -= 1

    if all(x <= 0 for x in expected_copy.values()):
      M += 1

  return M / N
