import numpy as np

# Step 1: Create a 5x3 array of random integers between 50 and 100
scores = np.random.randint(50, 101, size=(5, 3))

# Step 2: Calculate column-wise mean (mean of each subject)
mean_scores = scores.mean(axis=0)

# Step 3: Subtract the mean from original scores using broadcasting
centered_scores = scores - mean_scores

# Step 4: Print results
print("Original Scores (5 students x 3 subjects):")
print(scores)

print("\nMean Score of Each Subject:")
print(mean_scores)

print("\nCentered Scores (After Broadcasting):")
print(centered_scores)
