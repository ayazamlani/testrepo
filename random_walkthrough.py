import random
import logging
import sys

compass = {
  'N': 1,
  'S': -1,
  'E': 1,
  'W': -1
}


def stop_at_start(directions):
  # A function that takes in a list of directions and stops when back at original location

  x = 0
  y = 0

  for step in directions:
    if step in 'NS':
      x += compass[step]
    elif step in 'EW':
      y += compass[step]
    else:
      print('Invalid letter, use only N, S, E or W')
      sys.exit(1)

    print(f'Moved {step}')

    if x == 0 and y == 0:
      print('Hooray! Back at the start')
      break;


def next_step():
  nav = list(compass.keys())
  while True:
    step = random.choice(nav)
    yield step



directions = next_step()

stop_at_start(directions)
