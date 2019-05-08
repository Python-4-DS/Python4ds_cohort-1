def sum_of_lists(N):
    total = 0
    for i in range(5):
        l = [j^(j>>i)for j in range(N)]
        total += sum(l)
        del l #remove reference to l
    return total
