import math
from collections import Counter

data = [
    ((160, 2),"apple"),
    ((170, 6),"banana"),
    ((180, 8),"apple"),
    ((260, 8),"banana"),
    ((160, 7),"apple"),
    ((120, 6),"banana"),
    ((140, 3),"apple"),
    ((130, 7),"banana"),
    ((110, 6),"apple"),
]

def eulidean_distance(point1, point2):
    return math.sqrt(sum((a-b)**2 for a, b in zip(point1, point2)))
def knn(new_point, k):
    distances = []
    for features, point in data:
        distance = eulidean_distance(features,new_point)
        distances.append((distance, point))
    distances.sort()
    neighbors = [label for _, label in distances[:k]]
    vote = Counter(neighbors)
    most_common = vote.most_common(1)[0][0]
    print(f"The most common label the {k} nearest neighbors is {most_common}")
    return most_common
new_point = (190, 8)
k=3
neighbors = knn(new_point, k)