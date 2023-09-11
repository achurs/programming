def count_pairs_with_difference_k(array, k):
  hash_table = {}
  count = 0

  for integer in array:
    hash_table[integer] = hash_table.get(integer, 0) + 1

  for integer in array:
    count += hash_table.get(integer - k, 0)
    count += hash_table.get(integer + k, 0)

  return count

list = [1, 2, 3, 4]
print(count_pairs_with_difference_k(list, 1))