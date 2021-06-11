#get as many input from users on the number of numbers
list_of_nums = []
num_of_nums = input("How many numbers do you want to average?:")
while not num_of_nums.isnumeric():
    num_of_nums = input("How many numbers do you want to average?:")
num_of_nums = int(num_of_nums)

#get as many input as indicated by the number of numbers

for i in range(num_of_nums):
  print(f"Please key a number {i+1}:")
  num = input("Key in number here:")
  while not num.isnumeric():
    print(f"Please key a number {i+1}:")
    num = input("Key in number here:")
  list_of_nums.append(int(num))

#calculate the average of these amount of numbers
sum_of_nums = 0
for num in list_of_nums:
  sum_of_nums += num
print(f"The average of these numbers are {sum_of_nums/len(list_of_nums)}.")
