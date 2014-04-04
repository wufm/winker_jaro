# Winkler Jaro

An implementation of the Winkler Jaro compare function which computes the distance difference between two strings.

The distance is measured between 0.0 and 1.0 with 1.0 being an exact match
You get to decide what your threshold is for how much equality you need.

Check out test.py for examples

# Test Output
from test.py

````
Testing various string distance with Winkler Jaro

josh vs josh = 1.0
josh vs Joshua = 0.75
josh vs Joshalot = 0.708333333333
josh vs Peter = 0.0
````

# Marriage Hero
This implementation was created and adapted for Marriage Hero, Washington United for Marriage / Approve74

http://www.friendvote.washingtonunitedformarriage.org/

http://washingtonunitedformarriage.org



