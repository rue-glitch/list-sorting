def listSort(numList: list)-> list:
  "Returns a sorted list"
  sortedList = []
  length = len(numList)

  for i in range(1, length):
    sortedList.append(numList[i])

  for i in range(1, length):  
    for j in range(i+1, length):
      if sortedList[i]> sortedList[j]:
        temp = sortedList[i]
        sortedList[i] = sortedList[j]
        sortedList[j] = temp

  return sortedList

