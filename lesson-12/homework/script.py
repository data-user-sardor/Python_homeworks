# Exercise 1: Threaded Prime Number Checker
import threading

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def check_primes(start, end, results):
    """Check primes in a range and store in results list."""
    primes = [n for n in range(start, end) if is_prime(n)]
    results.extend(primes)

if __name__ == "__main__":
    start_range = 1
    end_range = 100
    num_threads = 4
    threads = []
    results = []

    # Split range into chunks for threads
    chunk_size = (end_range - start_range) // num_threads
    for i in range(num_threads):
        start = start_range + i * chunk_size
        end = start + chunk_size if i < num_threads - 1 else end_range
        t = threading.Thread(target=check_primes, args=(start, end, results))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Sort results to keep order
    results.sort()
    print(f"Prime numbers between {start_range} and {end_range}:")
    print(results)

# Exercise 2: Threaded File Processing (Word Count)
import threading
from collections import Counter

def process_lines(lines, counter):
    """Count words in given lines and update counter."""
    local_counter = Counter()
    for line in lines:
        words = line.strip().split()
        local_counter.update(words)
    with threading.Lock():
        counter.update(local_counter)

if __name__ == "__main__":
    file_path = r"lesson-12\homework\large_text.txt" 
    num_threads = 4
    threads = []
    counter = Counter()

    # Read file
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Split lines into chunks for threads
    chunk_size = len(lines) // num_threads
    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i < num_threads - 1 else len(lines)
        t = threading.Thread(target=process_lines, args=(lines[start:end], counter))
        threads.append(t)
        t.start()

    # Wait for all threads
    for t in threads:
        t.join()

    # Display results
    print("Word occurrences:")
    for word, count in counter.most_common(10):  # Top 10 words
        print(f"{word}: {count}")
