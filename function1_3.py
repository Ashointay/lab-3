def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) // 2 
    chickens = numheads - rabbits 
    return rabbits, chickens 
numheads = 35 
numlegs = 94 
print(solve(numheads, numlegs))