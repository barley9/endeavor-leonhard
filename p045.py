import utils.figurate

imax = 100_000
triangles = set(utils.figurate.triangle(i) for i in range(1, imax))
pentagons = set(utils.figurate.pentagon(i) for i in range(1, imax))
hexagons  = set(utils.figurate.hexagon(i)  for i in range(1, imax))

print("The next triangle number which is also pentagonal and hexagonal is {}.".format(sorted(triangles & pentagons & hexagons)[2]))