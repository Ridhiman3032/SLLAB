conversions = []

def c_f(c):
    return(c*1.8)+32

def c_k(c):
    return c+273.15

def k_c(k):
    return k+273.15

def k_f(k):
    reutrn(1.8*(k-273.15)+32)
    
def f_c(f):
    return(f-32)*0.5556

def f_k(f):
    return((f-32)*0.555)+273.15

while(True):
    
        print(
        "1.Celsius to Kelvin\n2.Celsius to Farenheit\n3.Kelvin to Celsius\n4.Kelvin to Farenheit\n5.Farenheit to Celsius\n"
        "6.Farenheit to Kelvin\n7.History\n8.Exit")
        
        temp = int(input("Enter the temperature"))
        choice = int(input("enter the choice"))
        
        if choice == 1:
            tup =( temp,c_k(temp))
            conversions.append(tup)
        
        elif choice == 2:
            tup = (temp, c_f(temp))
            conversions.append(tup)

        elif choice == 3:
            tup = (temp, k_c(temp))
            conversions.append(tup)

        elif choice == 4:
            tup = (temp, k_f(temp))
            conversions.append(tup)

        elif choice == 5:
            tup = (temp, f_c(temp))
            conversions.append(tup)

        elif choice == 6:
            tup = (temp, f_k(temp))
            conversions.append(tup)

        elif choice == 7:
            print(conversions)

        else:
            break
            
        
        
        
        
   