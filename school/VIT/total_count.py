def fraction_of_positive_negative_and_zero(numbers):
  positive_count = 0
  negative_count = 0
  zero_count = 0

  for number in numbers:
    if number > 0:
      positive_count += 1
    elif number < 0:
      negative_count += 1
    else:
      zero_count += 1

  total_count = positive_count + negative_count + zero_count

  positive_fraction = round(positive_count / total_count, 3)
  negative_fraction = round(negative_count / total_count, 3)
  zero_fraction = round(zero_count / total_count, 3)

  return [positive_fraction, negative_fraction, zero_fraction]


list = [1,2,3,4,-5,6,-8,-9,0,0]
val = fraction_of_positive_negative_and_zero(list)
print("the fraction of positive, negative and zero is:", val)