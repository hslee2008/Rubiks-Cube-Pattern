import magiccube
from tqdm import tqdm
import statistics

cube = magiccube.Cube(3,"YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")

# input length of notation
n = int(input())

# set all the cube notation list
cube_notation = [
  "U","U'",
  "R","R'",
  "L","L'",
  "F","F'",
  "B","B'",
  "D","D'",
]

# given n, print all the possible notation combination with length of n
def print_all_notation(n):
  if n == 0:
    return [[]]
  else:
    result = []
    for notation in cube_notation:
      for notation_list in print_all_notation(n-1):
        result.append([notation] + notation_list)
    return result
  
allPossibleNotation = print_all_notation(n)

print(len(allPossibleNotation))

# cube repeat every notation till the cube is solved and average the turns it took
def cube_repeat(notation):
  count = 0
  
  while True:
    cube.rotate(notation)
    count += 1
    if cube.is_done():
      break
  
  return count

list = []

for notation_list in tqdm(allPossibleNotation):
  list.append(cube_repeat(' '.join(notation_list)))

print("평균", statistics.mean(list))
print("중앙값", statistics.median(list))
print("최빈값", statistics.mode(list))  