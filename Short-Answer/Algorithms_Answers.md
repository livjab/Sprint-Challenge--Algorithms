#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This is an example of O(log n). As n gets larger, the number of operations increases, but not by much. The output for 'a' will quickly equal that of the input of the while loop.


b) This is linear time complexity. The nested loop originally led me to believe that it would be O(n^2), but upon closer examination, it seems that the first loop is a constant, leaving only the second loop to consider, which is O(n).


c) This is exponential time complexity -- O(c^n). The algorithm increases the number of operations it performs as an exponential function of 'n'

## Exercise II

1. Choose random floor and drop egg.

- if egg breaks, go down one floor and try again.
  - continue moving one floor down until egg does not break

- if egg does not break, go up one floor and try again.
  - continue moving one floor up until egg does break

This problem reminds me of how we solved quick sort, which is O(n^2).
