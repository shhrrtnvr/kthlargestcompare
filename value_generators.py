import random
def generate_random(n, lim = 1000):
    return [random.randrange(lim) for _ in range(n)]

def generate_sorted(n):
    return list(range(1, n+1))

def generate_reverse(n):
    return list(range(n, 0, -1))

if __name__ == '__main__':
    print(generate_random(10))
    print(generate_sorted(10))
    print(generate_reverse(10))
    
