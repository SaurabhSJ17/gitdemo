n = int(input("enter the value for n = "))
m =int(input("enter the value for m = "))
print( "1=addition \n", "2=sub \n", "3=multi \n", "4=division \n", "5=modulus \n","6=floor division \n","7=power munti \n")
k=int(input("select the your calclative method = "))

if k==1:
    ans1 = n+m
    print("Addition of",n,"and",m,"is", ans1)

elif k==2:
    ans2 = n-m
    print("Subtraction of",n,"and",m,"is", ans2)

elif k==3:
    ans3 = n*m
    print("Multiplication of",n,"and",m,"is", ans3)

elif k==4:
    ans4 = n/m
    print("Division of",n,"and",m,"is", ans4)

elif k==5:
    ans5 = n%m
    print("Modulus of",n,"and",m,"is", ans5)

elif k==6:
    ans6 = n//m
    print("Floor Division of",n,"and",m,"is", ans6)

elif k==7:
    ans7 = n**m
    print("exponetial of",n,"and",m,"is",ans7)

else:
    print("select valide method from 1 to 7")