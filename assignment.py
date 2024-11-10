# print( "    *" )
# print( "   **" )
# print("  ***")
# print(" ****")

# item = 5
# for i in range(item):
#     print(" " *(item-i-1) + "* "*(i+1))

n = 5
for i in range(n):
    for j in range(n-i-1):
        if j < n-i-1:
            print("* ", end=" ")
    for k in range(i + 1):
        if k <=i:
            print("", end="")
    print()

print("WELDONE")

