# Hydra-game

A hydra is a set of sets that represents a tree. The goal of the game is to chop off all of hydra's heads while every time the head is chopped, the hydra grows. 
In my version, hydra is represented by parenthesis like this: 
() is an empty hydra 
(()) is a hydra with one head
(()()) is a hydra with two heads and so on. 

To chop a head off, you find the first head [()] starting from the left, remove it and replicate the set it was immediately contained in n times unless it is the outermost set (base case) 
For example: 
(()), n = 2 ----> () (base case)

(()()), n = 2----> (()) (also base case)

((()())()), n = 2 ----> ((())(())()) 

To run the game, I start with n = 1 and increase it every time I call Hydra function. For small initial hydras, the game terminates quickly: 
```
input: (()(((()))))
output:
((((()))))
(((())))
((()()))
((())(())(()))
(()()()()(())(()))
(()()()(())(()))
(()()(())(()))
(()(())(()))
((())(()))
(()()()()()()()()()(()))
(()()()()()()()()(()))
(()()()()()()()(()))
(()()()()()()(()))
(()()()()()(()))
(()()()()(()))
(()()()(()))
(()()(()))
(()(()))
((()))
(()()()()()()()()()()()()()()()()()()())
(()()()()()()()()()()()()()()()()()())
(()()()()()()()()()()()()()()()()())
(()()()()()()()()()()()()()()()())
(()()()()()()()()()()()()()()())
(()()()()()()()()()()()()()())
(()()()()()()()()()()()()())
(()()()()()()()()()()()())
(()()()()()()()()()()())
(()()()()()()()()()())
(()()()()()()()()())
(()()()()()()()())
(()()()()()()())
(()()()()()())
(()()()()())
(()()()())
(()()())
(()())
(())
()
dead
```

For larger or more complicated hydras, it is difficult to prove if the hydra will terminate and it requires advanced techniques (like ordinals). 
