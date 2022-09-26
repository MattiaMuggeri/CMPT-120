
def main():

    #that's not right... how can we make sure it also includes equals 5?
    temp = 5
    if temp >= 5:
        print("temp is greater than or equal to 5")
        
    
    #enter your name here
    name = "Mattia"
    '''in this if/elif/else, add 4 mispellings of your name for if/elif comparisons, and then have your last elif be elif name = "your properly spelled name" '''
    if name == "Matia":
        print("That's not right!")
    elif name == "Matteo":
        print("That's not right!")
    elif name == "Matto":
        print("That's not right!")
    elif name == "Mattia":
        print("That's right!")
    else :
        print("That's not right!")
    #etc etc, the else can be whatever you want
    
    
    #we're gonna check if a user input number is even
    #pick any number
    even = input(int("Enter a number to find out if its even or odd"))
    even = int(even)
    #what do we replace the question marks with?
    if even % 2 == 0:
        #what would be appropriate in these print statements?
        print("It is even")
    else:
        print("It is odd")
  
  
    #i'm trying to do math with the numbers 2 and 4, but it's getting 3 and 5... why?
    #Because index starts at 0 hence you are using the subsequent element, I changed all 2's to 1's and all 4's to 3's
    numbers = [1,2,3,4,5]
    print(numbers[1])
    print(numbers[3])
    print(numbers[3] / numbers[1])
    print(numbers[3] * numbers[1])
    
    #again, why is it getting 7 and 20, I wanted 3 and 29!
    #same as before
    numbers2 = [465,3,30,7,29,20,82,13,5]
    print(numbers2[2])
    print(numbers2[4])
    
    #Here's a fun one: This is a list of everyone's name. Find where yours is and print the index of your name
    students = ["Achorn, Cameron", "Brown, Evan", "Catalano, Alexander", "Cianfoni, Alexander", "Delorey, Tyler","Edmonds, Jonah","Elliott, Dustin","Faix, Joseph","Fleischman, Connor","Fuerte, Caroline","Gidos, Hannah","Lavitt, Samuel","Lichstein, Harris","Longo, Nicholas","Martinez, David","Muggeri, Mattia","Munger, Ryan","Nealon, Ryan","Paulus, Natalie","Penn, Riley","Potenza, Amanda","Prochet, Carlisl","Putkaradze, Saba","Quayson, Eugene","Rietti, Cristina","Seeley, Shane","Sweeney, Quinn","Tata, Mathew","Taylor, Julia","Tuozzo, Michael"]
    N = len(students)
    Found = False
    L = N - 1
    #The following line has a syntax error and IDK what is wrong please help
    loop X from 0 to L:
        if (students[X] == "Mattia):
            print ("Found at index", X )
            Found = True
    end loop
    
    if Found == False
            print("Not found")
            
        
        
    
    
main()
    
    

    
