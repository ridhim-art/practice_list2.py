cir = lambda r: 2 * r * 3.14

data = [3,85,515,85,25,45,2,558,55,25,5,5,255,52]

results =[]

#normal
for radius in data:
    out = cir(radius)
    results.append(out)
print(results)

#comprehension

results = [cir(radius) for radius in data ]
print(results)

# map function

results = list(map(cir,data)) 
print(results)