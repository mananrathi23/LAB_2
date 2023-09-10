t=int(input("enter duration in months:")) 
 p=int(input("enter amount:")) 
 n=int(input("enter monthly installment:")) 
 r=7.1 
 if t<=6 or n<=500 : 
     print("invalid") 
 else: 
     print("final amount is ",(p(1+r/n))**nt) 
