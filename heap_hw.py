import heapq


def min_cost_connection(cables):
    solution = []
    heapq.heapify(cables)
    while len(cables) > 1:
        elem1 = heapq.heappop(cables)
        elem2 = heapq.heappop(cables)
        eval = elem1 + elem2
        solution.append(eval)
        heapq.heappush(cables, eval)
    return sum(solution)


cables = [1, 2, 3, 4, 5]
print(min_cost_connection(cables))
