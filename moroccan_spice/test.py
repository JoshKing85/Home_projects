import random
def generate_weights():
    """
    Generate a list of 10 random weights that sum to 750g with varied spread, a range of 10 to 150g, 
    and ensure all weights end in 0.
    """
    total_weight = 750
    min_weight = 10
    max_weight = 150
    weights = []

    for _ in range(9):
        remaining_weight = total_weight - sum(weights)
        max_possible = min(max_weight, remaining_weight - (9 - len(weights)) * min_weight)
        weight = random.randint(min_weight // 10, max_possible // 10) * 10  # Ensure the weight ends in 0
        weights.append(weight)

    weights.append((total_weight - sum(weights)) // 10 * 10)  # Ensure the last weight also ends in 0
    random.shuffle(weights)
    return weights

print(generate_weights())