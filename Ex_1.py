star = eval(input("Enter Diamond star : "))
def Diamond(star) :

   for i in range(star) :
        print(*" "*(star - i),*"*"*(i*2+1))
   for i in range(star -2,-1,-1) : 
        print(*" "*(star -  i),*"*"*(i*2+1))

Diamond(star)