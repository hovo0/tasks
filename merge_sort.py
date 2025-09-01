data_example = [1,5,10,78,96,88,6,2,4]
def mergesort(data):
    """
      Sort a list of numbers using the merge sort algorithm.

      Time Complexity:
          O(n * log n) for best, average, and worst cases.
      Args:
          data (list): A list of numbers to sort.

      Returns:
          list: A new sorted list.
    """
    def sort(data1, data2):

        result = []
        i,j = 0,0
        while i<len(data1) and j<len(data2):
            if data1[i]<data2[j]:
                result.append(data1[i])
                i+=1
            else:
                result.append(data2[j])
                j+=1
        while i<len(data1):
            result.append(data1[i])
            i+=1
        while j<len(data2):
            result.append(data2[j])
            j+=1
        return result

    def divide(data):
        if len(data) < 2:
            return data
        else:
            middle = len(data)//2
            data1 = divide(data[:middle])
            data2 = divide(data[middle:])
            return sort(data1,data2)
    return divide(data)

print(mergesort(data_example))