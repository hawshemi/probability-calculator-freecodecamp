import copy
import random

# Define a class called Hat
class Hat:

  # Initialize the Hat object with a dictionary of colors and their counts
  def __init__(self, **kwargs):
    # Initialize an empty list to store the contents of the hat
    self.contents = []
    # Iterate through the key-value pairs in the input dictionary
    for key, value in kwargs.items():
      # Extend the contents list with 'value' number of 'key' elements
      self.contents.extend([key] * value)

  # Define a method to draw a specified number of balls from the hat
  def draw(self, number):
    # If the number requested is greater than or equal to the total number of balls, return a copy of all the balls
    if number >= len(self.contents):
      return self.contents.copy()
    balls = []
    # Iterate 'number' times to draw that many balls
    for _ in range(number):
      # Generate a random index to select a ball from the contents list
      choice = random.randrange(len(self.contents))
      # Append the selected ball to the balls list and remove it from the contents
      balls.append(self.contents.pop(choice))
    return balls

# Define a function called experiment to perform experiments with the hat
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  # Create a list of expected ball counts based on the expected_balls dictionary
  expected_counts = [expected_balls[key] for key in expected_balls]
  successes = 0

  # Repeat the experiment 'num_experiments' times
  for _ in range(num_experiments):
    # Create a deep copy of the original hat to avoid modifying it
    new_hat = copy.deepcopy(hat)
    # Draw 'num_balls_drawn' balls from the new hat
    balls = new_hat.draw(num_balls_drawn)

    # Count the occurrences of each expected ball in the drawn balls
    ball_counts = [balls.count(key) for key in expected_balls]

    # Check if all the actual counts are greater than or equal to the expected counts
    if all(
        ball_count >= expected_count
        for ball_count, expected_count in zip(ball_counts, expected_counts)):
      successes += 1

  # Calculate the probability of success and return it
  return successes / num_experiments
