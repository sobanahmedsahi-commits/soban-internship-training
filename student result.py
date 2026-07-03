def calculate_stats(students):
    averages = []

    for data in students.values():
        avg = sum(data["grades"].values()) / len(data["grades"])
        averages.append(avg)

    print("Maximum average:", max(averages))
    print("Minimum average:", min(averages))
    print("Overall average:", sum(averages) / len(averages))

calculate_stats(students)