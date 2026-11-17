"""Baseline: count distinct values using repeated list membership checks."""
def count_unique_items(data):
    unique_items = []
    for item in data:
        if item not in unique_items:
            unique_items.append(item)
    return len(unique_items)

if __name__ == "__main__":
    sample_data = [i % 1500 for i in range(12000)]
    print("Unique items:", count_unique_items(sample_data))
