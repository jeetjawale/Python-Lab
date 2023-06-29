def uniquewordsfrequency(list_of_strings):
  words = set(list_of_strings)
  frequency_of_occurrence = {}
  for word in words:
    frequency_of_occurrence[word] = list_of_strings.count(word)
  return frequency_of_occurrence
if __name__ == "__main__":
  list_of_strings = ["Red", "Green", "Red", "Blue", "Red" , "Red", "Green"]
  frequency_of_occurrence = uniquewordsfrequency(list_of_strings)
  print(frequency_of_occurrence)
