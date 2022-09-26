def main():
  
  #set this to any double
  doubleValue = 1.2
  
  #set this to any int
  intValue = 3
  
  #print out addition, subtraction, multiplication, and division of these two values
  
  print(doubleValue + intValue)
  print(doubleValue - intValue)
  print(doubleValue * intValue)
  print(doubleValue / intValue) 
  
  
  #populate this list
  myFriends = ["Me","myself","I","Mattia"]
  
  #print out your friends at index 2 and index 3
  print(myFriends[2])
  print(myFriends[3])
  
  #populate this list with five numbers
  fiveNumbers = [1,4,9,16,25]
  
  #do each of the four equations with different numbers each time.
  
  print(fiveNumbers[2] + fiveNumbers[0])
  print(fiveNumbers[1] - fiveNumbers[3])
  print(fiveNumbers[2] * fiveNumbers[4])
  print(fiveNumbers[1] / fiveNumbers[1])
  
  #now replace two of the numbers in the list with a different number (using name of list[x] = ?, not rewriting the fiveNumber list)
  fiveNumbers[0] = 36
  fiveNumbers[1] = 49
  #print out the list
  print(fiveNumbers)
  
main()
