from vector import Vector

#Tests des constructeurs
try:
    print("\n-------------> INT CONSTRUCTEUR")
    vector1 = Vector(3)
    print(vector1.values)
    print(vector1.shape)

    print("\n-------------> RANGE CONSTRUCTEUR")
    vector2 = Vector((10,15))
    print(vector2.values)
    print(vector2.shape)

    print("\n-------------> LIST OF FLOATS CONSTRUCTEUR")
    vector3 = Vector([0.0, 1.0, 2.0, 3.0])
    print(vector3.values)
    print(vector3.shape)
    ex3 = vector3 * 5
    print(ex3.values)
    ex33 = ex3 - vector3
    print(ex33.values)
    ex333 = sum([vector3, ex3, ex33])
    print(ex33.values)

    print("\n-------------> LIST OF LIST OF FLOATS CONSTRUCTEUR")
    vector4 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print(vector4.values)
    print(vector4.shape)
    ex4 = vector4 * 5
    print(ex4.values)
    ex44 = ex4 + vector4
    print(ex44.values)
    ex444 = ex44 / 2
    print(ex444.values)
    ex4444 = ex444.T()
    print(ex4444.values)
    ex44444 = ex4444.dot(ex33)
    print(ex44444.values)

except ValueError as err:
    print(err.args)
