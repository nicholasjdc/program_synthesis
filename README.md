In HW2 I implemented bottom up search in a recursive model
using "seenAnswers" variable as a way of eliminating equivalent solutions.
More specifically, during each iteration the result of the new function is 
checked to see if is in "seenAnswers". If so, that version of the function is 
skipped. If not, then that function is then added to seenAnswers, tested, and expanded.

Changes from HW1:
The original homework I submitted was an analytice solver. So first, I changed it
to be a brute force programming by example query. Then I added the ability to control the
depth of the function (# of operations that could be done on the input), and width("height"
of the allowed integers, e.g. height:5, valid numbers [1,2,3,4,5]). Then I added the seenAnswers
section to allow for additional efficiency. I read on some other people's repos that they
optimized their results so as to create the smallest solution possible. Due to my implementation
of the elimEquivalents function and DFS search for functions, my formulas are almost guaranteed to
be on the longer side, because some of the routes to the more succinct formulas are preceded by 
longer formulas that stumble on the same route and then cut off that route for anyone else. If
I wished to keep the current implementation of seenAnswers and implement a 'shortest algorithm' finder, I should use a BFS instead of DFS for traversing my bottom up tree. 

