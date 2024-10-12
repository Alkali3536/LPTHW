types_of_people = 10
#This line above defines a variable and assigns value `10`. 

x = f"There are {types_of_people} type of people."
#we use f-string (formatted string) to add the value 
# of the variable `types_of_people` into the string. 

binary = "binary"
do_not = "don't"
#We assigns value "binary" to binary and "don't"  to do_not

y = f"Those who know {binary} and those who {do_not}."
#we use f-string (formatted string) to add the value 
# of the variable `binary` and "don't" into the string. 


print (x)
print (y)

#print the values of `x` and `y` to the console. 

print (f"I said: {x}")
print (f"I also said: '{y}'")
#These lines use **f-strings** to print the previously defined 
# `x` and `y` values with additional text. The output will be:

hilarious = False
#This line defines the variable `hilarious` and assigns it the 
# Boolean value `False`.

joke_evaluation = "Isn't that joke so funny?! {}"
#we defines a string `joke_evaluation` with a placeholder `{}` 

print (joke_evaluation.format(hilarious))
#uses the **`.format()` method** to replace the placeholder `{}` 
# in the `joke_evaluation`

w = "This is the left side of ..."
e = "a string with a right side."
#we define two variable and assing string
print (w + e)