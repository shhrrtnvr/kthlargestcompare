import heapq, random

def algorithm1(data, k):
    data.sort(reverse=True)
    return data[k-1]

def algorithm2(data, k):
    random.shuffle(data)
    shortlist = data[:k]
    heapq.heapify(shortlist)
    for i in range(k, len(data)):
        if data[i] > shortlist[0]:
            heapq.heappush(shortlist, data[i])
    return shortlist[0]

if __name__ == '__main__':
    import random
    sample = [random.randrange(1000) for _ in range(1000)]
    print(algorithm1(sample, 100))
    print(algorithm2(sample, 100))
