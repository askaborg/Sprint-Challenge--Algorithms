#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  O(log n)

    At the beginning of the while loop, the upper limit n^3 becomes static.
    The number of loops depends on the variable, a; this grows in a Fibonacci
    pattern, also a Logarithmic Spiral.  Since the while loop exits when
    (a < n^3), statements within the loop is executed O(log n) times.


b)  O(n log n)

    Statements within the for loop executes O(n) times because of range(n).
    Statements within the while loop executes O(log n) times becuase j
    increases exponentially and the while loop exits when (j < n). The while
    loop is nested within the for loop; multiplying n and log n,
    we get O(n log n).

c)  O(n)

    This recursive function acts like a reverse for loop where the function
    calls itself O(n) times.

## Exercise II

When the number of floors is 1, return 1; base case

Test to see if an egg gets broken when thrown from the n//2 story.

    if the egg breaks

        test again from the (n//2)//2 story.

    otherwise

        test again from the (n//2) + (n//2)//2 story.

Use recursion and keep track of f.

Since the number of recursive calls is halved each time with respect to n, the time complexity is O(log n).
