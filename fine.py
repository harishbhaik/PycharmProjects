d=int(input("enter number of days"))
fine=0
if(d<=5):
    fine=d*0.50
    print("fine less than 5 days):",float(fine))
elif(d>5 and d<=10):
    i=d-5
    fine=(i*1)+(5*0.50)
    print("fine(5 to 10 days)",float(fine))
elif(d>10 and d<=30):
    i=d-10
    fine=(i*5)+(5*0.50)+(5*1)
    print("fine(11 t0 30 days)",float(fine))
else:
    i=d-10
    fine = (i * 5) + (5 * 0.50) + (5 * 1)
print("your membership is cancelled")
print("fine (above 30 days)",float(fine))
