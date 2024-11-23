import numpy as np

def count_crossings(t):
    x = 0
    crossings = 0
    for i in range(t):
        move = 1 if np.random.rand() < 0.5 else -1
        x += move
        if x == 0:
            crossings += 1
    return crossings

def average_crossings(num_runs, t):
    crossings_list = [count_crossings(t) for _ in range(num_runs)]
    return np.mean(crossings_list)

# Running for t = 4 * 10^4, 9 * 10^4, and 16 * 10^4
for t in [4 * 10**4, 9 * 10**4, 16 * 10**4]:
    avg_crossings = average_crossings(50, t)
    print(f"Average crossings for t = {t}: {avg_crossings}")