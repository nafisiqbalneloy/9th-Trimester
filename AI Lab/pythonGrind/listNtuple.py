# student = ["karen",95.4,17,"dhaka"]
# print(student[0]) #list use korar benefits, can access value

# marks = [94.4,87.5,95.2,66.4,45.1] #list
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(len(marks))
# print(marks[1:4]) #can do slicing

# #method
# print(marks.sort(reverse=True)) #none
# print(marks) #sorted here ascending
# print(marks.reverse())
# print(marks)

# list = [2,1,3,1]
# list.pop(2) #index e jaiye delete kora
# print(list)
# list.remove(2) #2 delete kora
# print(list)

#TUPLE - immutable

# tup = (2,1,3,1)
# print(tup[0])
# print(tup[1])

# tup = (1,) #right way
# print(tup)
# print(type(tup))

#methods
# print(tup.index(2)) #2 element index 1 e ache


#WAP to ask the user to enter names of their 3 favourites
# movies and store them in a list
# movies = []
# mov1 = input("enter 1st movie: ")
# mov2 = input("enter 1st movie: ")
# mov3 = input("enter 1st movie: ")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)


#WAP to check if a list contains a palindrome of elements

list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list2):
    print("palindrome")
else:
    print("not palindrome")






