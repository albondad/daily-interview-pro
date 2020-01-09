def two_sum(list, k):
  result = False

  for i in range(len(list)):
    for j in range(len(list)):
        if i != j:
            if (list[i] + list[j]) == k:
                result = True

  print result
  raw_input()


print two_sum([4,7,1,-3,2], 5)
