# Problem
**PROBLEM ASKED BY DAILY INTERVIEW PRO**

This problem was recently asked by Google:

A chess board is an 8x8 grid. Given a knight at any position (x, y) and a number of moves k, we want to figure out after k random moves by a knight, the probability that the knight will still be on the chessboard. Once the knight leaves the board it cannot move again and will be considered off the board.

Here's some starter code:

```python
def is_knight_on_board(x, y, k, cache={}):
  # Fill this in.

print is_knight_on_board(0, 0, 1)
  # 0.25
```

# My Solution
I created an array that looped through all the possible positions the knight can make at
that move, keeping track of all the invalid positions (times it moved out of the box) append
valid positions (times it stayed in the box). I calculated the probability by dividing all the
invalid positions with the sum of the valid and invalid positions.
