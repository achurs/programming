def watson_number(array):
  n = len(array)
  sum_array = [0] * (n + 1)
  for i in range(1, n + 1):
    sum_array[i] = sum_array[i - 1] + array[i - 1]

  for i in range(n):
    left_sum = sum_array[i]
    right_sum = sum_array[n] - sum_array[i + 1]
    if left_sum == right_sum:
      return array[i]

  return -1


list = [1,2,3,4,5,6,7,8]
if watson_number(list) == -1:
  print("No Number")
else:
  print("The Number: ", watson_number(list))
