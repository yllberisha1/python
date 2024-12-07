#create a list

names = ["Blerta","Erosi","Driloni","Brikena","Ylli"]

#Iteraye on the names list and print evry name

for name in names:
    print(name)


########################

sentence = "Hello World"

for character in sentence:
    if character.isalpha(): #Check if the charater is a letter
        print(character)


# Range Function

for number in range(1,6): #prints number from the number 1 to 5 or more intail n to n-1
    print(number)


###########################

numbers = [12,45,6,72,21,8,94,57]

#Initiaze a varbale "maximum" with the first value from the list "numbers"


maximum = numbers [0]

for num in numbers: # Begin a loop through each element in the list "numbers"
    if num > maximum: # heck if the current element "num" is greater then teh current maximum value
        maximum = num # if so, update the maximum value to be the current elemrnt in num
    print("The maximum value in the list is:", maximum)

##################################
#While loop

count = 1 # Initialize the loop control variable

while count <=  5:
    print("Iteration", count)
    count +=1 #Incorment the loop control variable

########################
#Do While loop

# infinite loop

while True:
    # prompt user to enter a postive number
    user_input = input("enter a positive number:")

    #check if input is numeric
    if user_input.isnumeric():
        number = int(user_input)

        if number > 0:
            break
         #Print the error message for invalid input
            print("invalid input please try again")
         #Print the valid positive number entered by the user
            print("you have enterd a valid positive number:", number)


#################################



   #numberList = [1,2,3,4,5,6,7]
   #target =4

   #for number in numberList:
       #print(number)
       #if number == target:
           #print("Target found")
           #break









