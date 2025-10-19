def getSecondOrderElements(n: int,  a: [int]) -> [int]:
   largest,smallest = a[0],a[0]
   for i in a :
      largest = max(largest,i)
      smallest = min(smallest,i)
   second_smallest = float("inf")
   second_largest = float("-inf")
   for i in a :
      if i == largest or i == smallest :
         continue
      else :
         second_smallest = min(second_smallest,i)
         second_largest  = max(second_largest,i)
   return [second_largest,second_smallest]

print(getSecondOrderElements(7,[1,2,3,4,5,6,7]))