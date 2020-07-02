Pass = 0 
Fail = 0 
Count = 0 
while (!eof()) :
    TotalMarks=0
    read(Marks)
    if (Marks >= 40)
        Pass = Pass + 1
    if (Marks < 40)
        Fail = Fail + 1
    Count = Count + 1
    TotalMarks = TotalMarks+Marks 
print("Out of %d, %d passed and %d failed\n",Count,Pass,Fail) 
average = TotalMarks/Count;
/* This is the point of interest */
print("The average was %d\n",average) 
PassRate = Pass/Count*100 ;
print("This is a pass1 rate of %d\n",PassRate) 