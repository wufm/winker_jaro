# Winkler Jaro

An implementation of the Winkler Jaro compare function which computes the distance difference between two strings.

The distance is measured between 0.0 and 1.0 with 1.0 being an exact match
You get to decide what your threshold is for how much equality you need.

In our app, we used 0.95 as the minimum score to even consider

Check out test.py for examples

# Test Output
from test.py

````
Testing various string distance with Winkler Jaro

Josh Cohen vs Josh Cohen = 1.0
Josh Cohen vs Joshua Cohen = 0.966666666667
Josh Cohen vs Joshalot Cohen = 0.912857142857
Josh Cohen vs Peter Smith = 0.460606060606
````

# Marriage Hero
This implementation was created and adapted for Marriage Hero, Washington United for Marriage / Approve74

http://www.friendvote.washingtonunitedformarriage.org/

http://washingtonunitedformarriage.org



