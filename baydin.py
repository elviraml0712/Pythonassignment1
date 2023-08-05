zero = "you are lucky in this year"
one = "you are normal this year"
two = "you are unlucky this year"
year = eval(input('Birth Year : '))
month = eval(input('Birth Month : '))
day = eval(input('Birthday : '))
sum = year + month + day
mod = sum % 3
print("lucky star baydin")
if mod == 0:
    print(zero)
elif mod == 1:
    print(one)
elif mod == 2:
    print(two)