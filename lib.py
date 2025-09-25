def count_identities(*lists):
    count_intersections = set(lists[0])

    for lst in lists[1:]:
        count_intersections &= set(lst)

    return len(count_intersections)
