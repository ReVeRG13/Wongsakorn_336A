value = eval(input("Enter max value : "))
prime = input("Enter Y/N (OnlyPrime?) : ")
data_n = []
data_y = []
i = 0
for i in range(1) :
    for j in range(1, value+1):
        data_n.append(j)
    if prime == 'Y' :
        for num in range(1, value+1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    data_y.append(num)
        data_y.reverse()
        for i in range(0,len(data_y),1):
            print(f"{data_y[i]} is prime value")
    elif prime == 'N' :
            for num in range(1, value+1):
                    if num > 1:
                        for i in range(2, num):
                            if (num % i) == 0:
                                break
                        else:
                            data_y.append(num)
                            data_n.remove(num)
                    data_y.reverse()
                    data_n.reverse()
            for j in range(0,len(data_y),1):
                print(f"{data_y[j]} is prime value")
            for j in range(0,len(data_n),1):
                print(f"{data_n[j]} is not prime value")