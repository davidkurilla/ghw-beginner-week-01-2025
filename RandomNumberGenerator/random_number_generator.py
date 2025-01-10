import time

class MyRNG:
    def __init__(self, seed=None):
        self.m = 2**31 - 1
        self.a = 1103515245
        self.c = 12345

        if seed is None:
            seed = int(time.time() * 1000) % self.m
        self.n = seed

    def next(self):
        self.state = (self.a * self.n + self.c) % self.m
        return self.n

    def rand_int(self, min_value, max_value):
        return min_value + self.next() % (max_value - min_value + 1)
    
rng = MyRNG()

rand_int_01 = rng.rand_int(1, 5)
rand_int_02 = rng.rand_int(1, 10)
rand_int_03 = rng.rand_int(1, 100)

print(f'Rand Int 1: {rand_int_01}')
print(f'Rand Int 2: {rand_int_02}')
print(f'Rand Int 3: {rand_int_03}')