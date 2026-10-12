def classify(value):
    if value < 498:
        return "Below range"
    elif value <= 502:
        return "In range"
    else:
        return "Above range"

def calculate_average(total, count):
    average_snapshot = total / count
    return average_snapshot

number_bags = int(input("Enter the number of rice bags: "))
total = 0
count_below_r = 0
count_in_r = 0
count_above_r = 0

for number_bag in range(number_bags):
    weight_bags = int(input("Enter the rice bag weight: "))
    result = classify(weight_bags)
    print(result)
    total = total + weight_bags
    if result == "Below range":
        count_below_r = count_below_r + 1
    elif result == "In range":
        count_in_r = count_in_r + 1
    else:
        count_above_r = count_above_r + 1


average_snapshot = calculate_average(total, number_bags)

print(f"Total weight: {total} g")
print(f"Average weight: {average_snapshot} g")
print(f"Below range: {count_below_r}")
print(f"In range: {count_in_r}")
print(f"Above range: {count_above_r}")