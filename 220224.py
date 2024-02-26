# thelist = ["apple", "banana", "Cherry", "pieapple", "Cherry"]
# print(len(thelist))

# mylist = ["apple", "banana", "cherry"]
# print(mylist[-2])

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)
# for x in thislist:
#     print(x)

# print("result")
# response = int(input())
thislist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nxt =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# thislist[2:5]
for x in thislist:
    for y in thislist:
        print(f"{x}{y}")
        # scores = x - y
        # while response == scores:
        #     print("You win")
        #     break
        # else:
        #     print("You loose!!")