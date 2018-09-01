from vpython import *
k = 1.0
g = vector(0.0, -9.8, 0.0)
m = 1.0
scene.autoscale = 0
n_steps = 1000
dt = (10.0 - 0) / n_steps
s = sphere(pos=vector(0.0, 0.0, 0.0))
s.vel = vector(0.0, 0.0, 0.0)
for i in range(n_steps):
    rate(1.0/dt)
    s.alpha = -k * s.pos + m * g
    s.pos += s.vel * dt
    s.vel += s.alpha * dt