import numpy as np

# Define the parameters
vote_probabilities = [0.35, 0.40, 0.25]  # probabilities for +1, -1, 0
vote_types = [1, -1, 0]

# Simulation function
def simulate_majority_negative(vote_probs, sample_size, num_simulations=200):
    majority_negative_count = 0
    for _ in range(num_simulations):
        # Randomly sample votes according to the given probabilities
        votes = np.random.choice(vote_types, size=sample_size, p=vote_probs)
        
        # Count number of -1 votes
        num_negative = np.sum(votes == -1)
        
        # Check if there is a majority of -1 votes
        if num_negative > sample_size / 2:
            majority_negative_count += 1
    
    # Return the proportion of simulations where -1 was the majority
    return majority_negative_count / num_simulations

# Sample sizes for experiments
sample_sizes = [10, 120, 250]

# Run simulations for each sample size
probabilities = {size: simulate_majority_negative(vote_probabilities, size) for size in sample_sizes}

# Output the probabilities for each sample size
for size, prob in probabilities.items():
    print(f"Sample Size: {size}, Probability of Majority -1: {prob:.4f}")

# To find the sample size needed for 0.9 probability
def find_sample_size_for_probability(vote_probs, target_prob, max_sample_size=1000, num_simulations=200):
    for sample_size in range(10, max_sample_size + 1):
        prob = simulate_majority_negative(vote_probs, sample_size, num_simulations)
        if prob >= target_prob:
            return sample_size, prob
    return None, None  # In case we don't reach the target within max_sample_size

# Find the sample size for a 0.9 probability
target_probability = 0.9
sample_size_for_90_prob, achieved_prob = find_sample_size_for_probability(vote_probabilities, target_probability)

if sample_size_for_90_prob is not None and achieved_prob is not None:
    print(f"\nSample size needed for a probability of 0.9 for majority -1: {sample_size_for_90_prob}, Achieved probability: {achieved_prob:.4f}")
