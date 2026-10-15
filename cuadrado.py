import matplotlib.pyplot as plt

A = (3, 1, 0)
B = (5, 2, 0)
C = (5, 4, 0)
D = (3, 5, 0)
E = (1, 4, 0)
F = (1, 2, 0)

vertices = [A, B, C, D, E, F]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for nombre, v in zip(["A", "B", "C", "D", "E", "F"], vertices):
    ax.scatter(*v)
    ax.text(*v, nombre)

aristas = [
    (A, B), (B, C), (C, D),
    (D, E), (E, F), (F, A)
]

for p, q in aristas:
    ax.plot([p[0], q[0]], [p[1], q[1]],
            [p[2], q[2]])

ax.set_title("Hexágono 3D")
plt.show()