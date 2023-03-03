
glass_size = int(input())
straw_pos = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
for h in range((2*glass_size + 2-straw_pos)//2 + 1):
# glass number is identified by the line above.
  for i in range(straw_pos):
    for j in range(0,i):
     print(" ",end="")
#this line working to assign increasing space character each row as straw continues.
    print("o")
# printed with for loop to show straw.
  for k in range(glass_size):
#this main loop is used for printing glass rows.
    for b in range(k):
        print(" ",end="")
    print("\\", end="")
    for l in range(2*(glass_size-k)):
# to determine depth of straw which located interior of the glass.
       if h-1<k:
            print('*',end="")
       else:
           if(l == straw_pos-1):
               print("o",end="")
           else:
               print(" ",end="")
    print("/")

  for t in range(glass_size):
#to print the last part of the glass containing spaces and horizontal line.
     print(" ",end="")
  print("--")
  for c in range(glass_size):
      for n in range(glass_size):
          #to finish the glasses for all domains in range which we assign.
         print(" ",end="")
      print("||")



#DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE