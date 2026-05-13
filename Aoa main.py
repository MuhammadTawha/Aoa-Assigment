import time

# 1. Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 2. Bubble Sort (With optimization flag)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# 3. Quick Sort (Using middle element as pivot for better performance)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 4. Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# --- Testing Harness ---
def run_experiment(algo, data):
    times = []
    for _ in range(3):
        data_copy = data.copy()
        start = time.time()
        algo(data_copy)
        end = time.time()
        times.append(end - start)
    return sum(times) / 3

# Data Cases
cases = {
    "Size 5 Sorted": list(range(1, 6)),
    "Size 5 Reverse": list(range(5, 0, -1)),
    "Size 100 Sorted": list(range(1, 101)),
    "Size 100 Reverse": list(range(100, 0, -1))
}

algos = [
    ("Selection Sort", selection_sort),
    ("Bubble Sort", bubble_sort),
    ("Quick Sort", quick_sort),
    ("Merge Sort", merge_sort)
]

print(f"{'Algorithm':<20} | {'Case':<20} | {'Avg Time (s)':<15}")
print("-" * 60)
for algo_name, algo_func in algos:
    for case_name, data in cases.items():
        avg_time = run_experiment(algo_func, data)
        print(f"{algo_name:<20} | {case_name:<20} | {avg_time:.8f}")