#random - generate numbers,choices
import random
print("Number from 10 to 50 is : ", random.randint(10,50))

#random.random(dynamically used)
print("Number from 0 to 1 is : ", random.random())

#for floating random number (uniorm)

print("Random number from 1.5 to 5.5 " , random .uniform(1.5,5.5))

#choice 
l=['sai','ganapathi','kousik','14']
print("Random choice from list : " , random.choice(l))
print("Random choices from list : " , random.choices(l))

list = [1, 2, 3, 4, 5]
random.shuffle(list)
print("Shuffled list : " ,list)

#Fixed number
random.seed(10)
print(random.randint(1,100))
