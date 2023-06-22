def calculate_score(rent, distance, amenities, budget,prox):
    amenity_points = 10
    proximity_range = prox #2,5,7,10,15

    amenity_weight = amenities * amenity_points
    proximity_weight = ((proximity_range - distance) / proximity_range) * 100
    score = amenity_weight + proximity_weight + (budget - rent)

    return score

def knapsack_problem(accommodations, budget,amenities,prox):
    n = len(accommodations)

    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            name, distance, rent, amenities = accommodations[i - 1]  # Update the order of unpacking
            if rent <= j:
                included_score = calculate_score(rent, distance, amenities, budget,prox) + dp[i - 1][j - rent]
                dp[i][j] = max(included_score, dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    best_accommodation = None
    max_score = 0
    for accommodation in accommodations:
        name, distance, rent, amenities = accommodation  # Update the order of unpacking
        score = calculate_score(rent, distance, amenities, budget,prox)
        if rent <= budget and score > max_score:
            max_score = score
            best_accommodation = accommodation

    return max_score, [best_accommodation] if best_accommodation else []


def main(acc,budget,amenities,prox):#from maps get_data
    
    #budget = 3000

    score, best_accommodations = knapsack_problem(acc, budget,amenities,prox)
    
    accommodation = best_accommodations[0] #add exception
    d={accommodation[0]:(accommodation[2],accommodation[1],accommodation[3])}
    return d


