"""Optimized: use a set for average O(1) membership/insertion."""
def count_unique_items(data):
    return len(set(data))

if __name__ == "__main__":
    sample_data = [i % 1500 for i in range(12000)]
    print("Unique items:", count_unique_items(sample_data))
