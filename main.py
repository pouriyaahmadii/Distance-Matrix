import numpy as np
import matplotlib.pyplot as plt

# ایجاد 10 نقطه تصادفی در فضای 2 بعدی
np.random.seed(0)  # برای تکرارپذیری
points = np.random.rand(10, 2)


# محاسبه ماتریس فاصله
def calculate_distance_matrix(points):
    num_points = len(points)
    distance_matrix = np.zeros((num_points, num_points))

    for i in range(num_points):
        for j in range(i + 1, num_points):
            distance = np.linalg.norm(points[i] - points[j])
            distance_matrix[i, j] = distance
            distance_matrix[j, i] = distance  # ماتریس فاصله متقارن است

    return distance_matrix


# محاسبه میانگین فاصله هر نقطه تا سه همسایه نزدیک
def calculate_average_distance_to_nearest_neighbors(points):
    distance_matrix = calculate_distance_matrix(points)
    num_points = len(points)

    average_distances = []

    for i in range(num_points):
        # حذف فاصله نقطه تا خودش (صفر)
        distances = np.delete(distance_matrix[i], i)

        # یافتن سه همسایه نزدیک
        nearest_neighbors = np.argsort(distances)[:3]

        # محاسبه میانگین فاصله تا سه همسایه نزدیک
        average_distance = np.mean([distance_matrix[i, neighbor] for neighbor in nearest_neighbors])

        average_distances.append(average_distance)

    return average_distances


# محاسبه و چاپ نتایج
average_distances = calculate_average_distance_to_nearest_neighbors(points)
print("میانگین فاصله هر نقطه تا سه همسایه نزدیک:")
for i, avg_dist in enumerate(average_distances):
    print(f"نقطه {i + 1}: {avg_dist:.4f}")

# رسم گرافیکی
plt.figure(figsize=(10, 5))

# رسم نقاط
plt.subplot(1, 2, 1)
plt.scatter(points[:, 0], points[:, 1])
for i, point in enumerate(points):
    plt.annotate(f"{i + 1}", (point[0], point[1]))
plt.title("نقاط در فضای 2 بعدی")

# رسم میانگین فاصله
plt.subplot(1, 2, 2)
plt.bar(range(1, len(points) + 1), average_distances)
plt.xlabel("شماره نقطه")
plt.ylabel("میانگین فاصله تا سه همسایه نزدیک")
plt.title("میانگین فاصله هر نقطه")

plt.tight_layout()
plt.show()
