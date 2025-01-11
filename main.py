import numpy as np
import matplotlib.pyplot as plt

# Generate 10 random points in a 2D space
np.random.seed(0)  # For reproducibility
points = np.random.rand(10, 2)


# Calculate distance matrix
def calculate_distance_matrix(points):
    num_points = len(points)
    distance_matrix = np.zeros((num_points, num_points))

    for i in range(num_points):
        for j in range(i + 1, num_points):
            distance = np.linalg.norm(points[i] - points[j])
            distance_matrix[i, j] = distance
            distance_matrix[j, i] = distance  # Distance matrix is symmetric

    return distance_matrix


# Calculate average distance to nearest neighbors
def calculate_average_distance_to_nearest_neighbors(points):
    distance_matrix = calculate_distance_matrix(points)
    num_points = len(points)

    average_distances = []

    for i in range(num_points):
        # Remove distance to itself (zero)
        distances = np.delete(distance_matrix[i], i)

        # Find three nearest neighbors
        nearest_neighbors = np.argsort(distances)[:3]

        # Calculate average distance to nearest neighbors
        average_distance = np.mean([distance_matrix[i, neighbor] for neighbor in nearest_neighbors])

        average_distances.append(average_distance)

    return average_distances


# Calculate and print results
distance_matrix = calculate_distance_matrix(points)
average_distances = calculate_average_distance_to_nearest_neighbors(points)

print("Distance Matrix:")
print(distance_matrix)

print("\nAverage distance from each point to its three nearest neighbors:")
for i, avg_dist in enumerate(average_distances):
    print(f"Point {i + 1}: {avg_dist:.4f}")

# Plotting
plt.figure(figsize=(10, 5))

# Plot points
plt.subplot(1, 2, 1)
plt.scatter(points[:, 0], points[:, 1])
for i, point in enumerate(points):
    plt.annotate(f"{i + 1}", (point[0], point[1]))
plt.title("Points in 2D Space")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Plot average distance
plt.subplot(1, 2, 2)
plt.bar(range(1, len(points) + 1), average_distances)
plt.xlabel("Point Number")
plt.ylabel("Average Distance to Nearest Neighbors")
plt.title("Average Distance from Each Point")

plt.tight_layout()
plt.show()
