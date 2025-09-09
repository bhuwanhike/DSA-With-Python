

dimension = int(input("Enter the dimension: "))

# Pattern - 1
'''

*****
*****
*****
*****
*****

'''

# for i in range(0, dimension):
#     for j in range(0, dimension):       # Time complexity - O(n^2)
#         print("*", end="")

#     print("\n")


# Using single loop

# for i in range(0, dimension):
#     print("*"*dimension, end="")        # Time complexity - O(n)
#     print("\n")

# ---------------*---------------*--------------------


# Pattern - 2
'''

*
**
***
****
*****

'''

# for i in range(0, dimension):
#     for j in range(0, i+1):
#         print("*", end="")              # Time complexity - O(n^2)

#     print("\n")


# Using single loop

# for i in range(0, dimension):
#     print("*"*(i+1), end="")            # Time complexity - O(n)
#     print("\n")


# ---------------*---------------*--------------------


# Pattern - 3
'''

1
12
123
1234
12345

'''

# for i in range(0, dimension):
#     for j in range(0, i+1):
#         print(j+1, end="")             # Time complexity - O(n^2)

#     print("\n")

# Using single loop

# pattern = ""

# for i in range(1, dimension+1):           # Time complexity - O(n)
#     pattern += str(i)
#     print(pattern, end="")
#     print("\n")

# ---------------*---------------*--------------------


# Pattern - 4
'''

1
22
333
4444
55555

'''

# for i in range(1, dimension+1):
#     for j in range(1, i+1):              # Time complexity - O(n^2)
#         print(i, end="")

#     print("\n")


# Using single loop


# for i in range(1, dimension+1):
#     print(f'{i}'*i, end="")                  # Time complexity - O(n)
#     print("\n")


# ---------------*---------------*--------------------

# Pattern - 5
'''

*****
****
***
**
*

'''

# for i in range(0, dimension):
#     for j in range(dimension-i, 0, -1):     # Time complexity - O(n^2)
#         print("*", end="")

#     print("\n")


#  Using single loop

# for i in range(dimension, 0, -1):

#     print("*"*i, end="")                      # Time complexity - O(n)

#     print("\n")


# ---------------*---------------*--------------------

# Pattern - 6
'''

12345
1234
123
12
1

'''

# for i in range(dimension, 0, -1):
#     for j in range(1, i+1):               # Time complexity - O(n^2)
#         print(j, end="")
#     print("\n")


# Using single loop

# patt = "".join(str(i) for i in range(1,dimension+1))

# for i in range(dimension,0, -1):
#     print(patt[:i], end="")
#     print("\n")                             # Time complexity - O(n)


# ---------------*---------------*--------------------

# Pattern - 7
'''

    *
   ***
  *****
 *******
*********

'''

# for i in range(dimension, 0, -1):
#     print(" "*i, end="")
#     print("*"*(2*(dimension-i+1)-1))         # Time complexity - O(n)
#     print("\n")


# ---------------*---------------*--------------------

# Pattern - 8
'''

*********
 *******
  *****
   ***
    *

'''

# for i in range(dimension, 0, -1):
#     print("*"*((2*i)-1))                   # Time complexity - O(n)
#     print(" "*(dimension-i+1), end="")


# ---------------*---------------*--------------------

# Pattern - 9
'''

    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *

'''

# for i in range(dimension, 0, -1):
#     print(" "*(i-1), end="")
#     print("*"*(2*(dimension-i+1)-1))

# for i in range(dimension, 0, -1):
#     print("*"*((2*i)-1))                   # Time complexity - O(2n)
#     print(" "*(dimension-i+1), end="")


# ---------------*---------------*--------------------


# Pattern - 10
'''

*
**
***
****
*****
****
***
**
*

'''

# for i in range(1, dimension+1):
#     print("*"*i)

# for i in range(dimension-1, 0, -1):      # Time complexity - O(2n)
#     print("*"*i)


# ---------------*---------------*--------------------


# Pattern - 11
'''

1 
0 1
1 0 1
0 1 0 1
1 0 1 0 1

'''

# for i in range(0, dimension):
#     for j in range(0, i+1):
#         if ((i+j) % 2 == 0):          # Time complexity - O(n^2)
#             print(1, end=' ')
#         else:
#             print(0, end=' ')

#     print("\n")


# ---------------*---------------*--------------------


# Pattern - 12
'''

1      1
12    21
123  321
12344321

'''

# for i in range(1, dimension+1):
#     for j in range(1, i+1):
#         print(j, end="")

#     print(" " * 2*(dimension-i), end="")       # Time complexity - O(2(n^2))
#     for l in range(i, 0, -1):
#         print(l, end="")

#     print("\n")


# ---------------*---------------*--------------------


# Pattern - 13
'''

1 
2 3
4 5 6
7 8 9 10
11 12 13 14 15

'''

# num = 1
# for i in range(0, dimension):
#     for j in range(0, i+1):
#         print(num, end=" ")            # Time complexity - O(n^2)
#         num+=1                         # Space complexity - O(dimension^2)
#     print("\n")


# ---------------*---------------*--------------------


# Pattern - 14
'''

A
AB
ABC
ABCD
ABCDE

'''

# for i in range(0, dimension):
#     for j in range(ord('A'), i+65+1):
#         print(chr(j), end="")                   # Time complexity - O(n^2)

#     print("\n")


# ---------------*---------------*--------------------


# Pattern - 15
'''

ABCDE
ABCD
ABC
AB
A

'''

# for i in range(dimension, 0, -1):
#     for j in range(ord('A'), i+65):
#         print(chr(j), end="")                   # Time complexity - O(n^2)

#     print("\n")


# ---------------*---------------*--------------------


# Pattern - 16
'''

A
BB
CCC
DDDD
EEEEE

'''

# char = "A"
# for i in range(0, dimension):
#     print(char*(i+1))
#     char = chr(ord(char)+1)           # Time complexity - O(n)
# Space complexity - O(dimension+2)


# ---------------*---------------*--------------------


# Pattern - 17
'''

    A
   ABA
  ABCBA
 ABCDCBA

'''

# for i in range(0, dimension):
#     char = 'A'
#     print(" "*(dimension-i-1), end="")             # Time complexity - O(n^2)
#     for j in range(0, (2*i)+1):
#         print(char, end="")
#         if(j<i):
#             char = chr(ord(char)+1)
#         else:
#             char = chr(ord(char)-1)


#     print("\n")


# ---------------*---------------*--------------------

# Pattern - 18
'''

E
D E
C D E
B C D E
A B C D E

'''

# char = chr(64+dimension)
# for i in range(0, dimension):
#     for j in range(0, i+1):
#         print(char, end=' ')                    # Time complexity - O(n^2)
#         if(j<i):
#             char = chr(ord(char)+1)
#     char = chr(ord(char)-i-1)
#     print("\n")


# ---------------*---------------*--------------------

# Pattern - 19
'''

**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********

'''

# for i in range(0, dimension):
#     print("*"*(dimension - i), end="")              # Time complexity - O(2n)
#     print(" "*2*i, end="")
#     print("*"*(dimension-i))

# for i in range(0, dimension):
#     print("*"*(i+1), end="")
#     print(" "*2*(dimension-i-1), end="")
#     print("*"*(i+1))


# ---------------*---------------*--------------------

# Pattern - 20
'''

*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

'''

# for i in range(0, dimension):
#     print("*"*(i+1), end="")
#     print(" "*2*(dimension-i-1), end="")
#     print("*"*(i+1))

# for i in range(1, dimension):
#     print("*"*(dimension - i), end="")              # Time complexity - O(2n)
#     print(" "*2*i, end="")
#     print("*"*(dimension-i))


# ---------------*---------------*--------------------

# Pattern - 21
'''

****

*  *

*  *

****

'''

# for i in range(0, dimension):
#     for j in range(0, dimension):
#         if(i == 0 or i == (dimension-1) or j ==0 or j==(dimension-1)):
#             print("*", end="")               # Time complexity - O(n^2)
#         else:
#             print(" ", end="")
#     print("\n")

# for i in range(0, dimension):
#     if(i == 0 or i == (dimension-1)):
#         print("*"*dimension)                             # Time complexity - O(n)
#     else:
#         print("*"+(" "*(dimension-3)),"*")


# ---------------*---------------*--------------------

# Pattern - 22
'''

4 4 4 4 4 4 4 
4 3 3 3 3 3 4
4 3 2 2 2 3 4 
4 3 2 1 2 3 4
4 3 2 2 2 3 4 
4 3 3 3 3 3 4
4 4 4 4 4 4 4 

'''

# new_dim = (2*dimension)-1

# for i in range(0, new_dim):
#     for j in range(0, new_dim):
#         value = min(i,j, new_dim-i-1, new_dim-j-1)          # Time complexity - O(n^2)
#         print(dimension-value, end=' ')
#     print("",end='\n')