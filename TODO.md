Hooray, this can now generate 4x4 grids. However, it is GROSSLY slow on anything larger.

Small performance wins:
+ pre-generate the Trie of all vocabulary and cache it on disk
+ better validation -- there's some redundancy in `Board.validate

Maybe bigger performance saves:
+ better heuristic for deciding which row/col to tackle next. Right now we fill
row 1, and then fill row 2 -- options for row 2 are totally unconstrained, we 
try everything in our dictionary and and for each, validate it against the existing
board. Smarter would be to fill row 1, then col 1, row 2, then col 2...

??? / general TODOs:
+ randomize which option we pick, instead of using the first returned
  + will probs want to be able to pass a seed to this if we want a specific result...?