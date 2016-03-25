import random


def weighted_random_values(tower_dicts_with_values, n_elements=2):
    """
    Espera [({(0, 1): TorreBlah(), (0, 2): TorreFoo(), ...}, valor), ...]
    """
    only_values = [value[1] for value in tower_dicts_with_values]
    max_value = max(only_values)
    min_value = min(only_values)

    distance = max_value - min_value
    absolute_size = max_value + min_value
    if absolute_size == 0:
        absolute_size = 1
    weight = int(abs(distance / absolute_size))
    if weight <= 0:
        weight = 1

    tower_dicts_with_values = sorted(tower_dicts_with_values,
                                     key=lambda value: value[1], reverse=True)

    possible_results = []
    for towers, value in tower_dicts_with_values:
        for _ in range(weight):
            possible_results.append((towers, value))
        weight -= int(abs(value/len(tower_dicts_with_values)))
        if weight <= 0:
            weight = 1

    print(possible_results)

    results = []
    for _ in range(n_elements):
        choice = random.choice(possible_results)
        results.append(choice)

    return results


if __name__ == '__main__':
    towers = ['a', 'b', 'c', 'd', 'e', 'f']
    print(weighted_random_values(towers))
