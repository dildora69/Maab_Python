
# ex-1

#
# import threading
#
#
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
#
# def check_prime_range(start, end, primes):
#     for num in range(start, end):
#         if is_prime(num):
#             primes.append(num)
#
#
# def main():
#     range_start = 10
#     range_end = 100
#     num_threads = 4
#     step = (range_end - range_start) // num_threads
#     primes = []
#     threads = []
#
#     for i in range(num_threads):
#         start = range_start + i * step
#         end = start + step if i < num_threads - 1 else range_end
#         thread = threading.Thread(target=check_prime_range, args=(start, end, primes))
#         threads.append(thread)
#         thread.start()
#
#     for thread in threads:
#         thread.join()
#
#     print("Prime numbers:", sorted(primes))
#
#
# if __name__ == "__main__":
#     main()




# ex-2



# import threading
# from collections import Counter
#
# def count_words_in_chunk(file_chunk, word_count):
#     words = file_chunk.split()
#     word_count.update(words)
#
# def main():
#     file_path = 'large_text.txt'  # Ensure you have a large text file
#     num_threads = 4
#     word_count = Counter()
#
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#
#     chunk_size = len(lines) // num_threads
#     threads = []
#
#     for i in range(num_threads):
#         start = i * chunk_size
#         end = start + chunk_size if i < num_threads - 1 else len(lines)
#         thread = threading.Thread(target=count_words_in_chunk, args=(' '.join(lines[start:end]), word_count))
#         threads.append(thread)
#         thread.start()
#
#     for thread in threads:
#         thread.join()
#
#     print("Word count summary:", word_count)
#
# if __name__ == "__main__":
#     main()

