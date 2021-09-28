from sys import argv

universal_length = 0
num_subsets = 0


with open(argv[1]) as f:
    lines = f.readlines()
    

for i in range(len(lines)):
    lines[i] = list(map(int, lines[i].split()))
            

lines = iter(lines)
universal_length = next(lines)[0]
num_subsets = next(lines)[0]

weights = []
subsets = []

for count in range(num_subsets):
    subsets.append(next(lines))
    weights.append(next(lines)[0])


best_sets = 0
best_weight = float('inf')

for i in range(2 ** num_subsets):
    u = [False] * universal_length
    weight = 0
    for j in range(num_subsets):
        if (i >> j) & 1:
            weight += weights[j]
            for num in subsets[j]:
                u[num-1] = True
    
    if weight < best_weight and all(u):
        best_sets = i
        best_weight = weight

print(best_weight)
for i in range(num_subsets):
    if (best_sets >> i) & 1:
        print(i+1, end=" ")
print()