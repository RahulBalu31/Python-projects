per=int(input('Enter the Percentage :'))
if(per > 95):
    print("Grade: A")
elif(per > 80 and per <= 95):
    print("Grade: B")
elif(per >= 50 and per <= 80):
    print("Grade: C")
elif(per < 50):
    print("Grade: D")
