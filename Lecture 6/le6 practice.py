#que 1
# cities=["haripur","Islamabad","Peshawear","Swat"]
# fruits=["apple","banana","peach","mango"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(fruits)

#que 2
# cities=["haripur","Islamabad","Peshawear","Swat"]
# fruits=["apple","banana","peach","mango"]

# def print_len(list):
#     print(len(list))

# def print_list(list):
#     for item in list:
#         print(item, end="")
# print_list(fruits)

# #que 3
# n=5
# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     print(fact)

# factorial(7)
#que 4
# def converter(usd_val):
#     inr_val = usd_val * 38
#     print(usd_val, "USD is equal to", inr_val, "INR" )
# converter(1)
#que 5
# def cal_sum(n):
#     if (n==0):
#         return 0
#     return cal_sum(n-1)+n

# sum= cal_sum(6)
# print(sum)


#que 6

def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits=["banana","mango","apple","orange","litchi"]

print_list(fruits)