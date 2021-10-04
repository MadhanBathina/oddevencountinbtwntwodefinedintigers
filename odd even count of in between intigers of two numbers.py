Start=int(input('Starting intiger :'))
End=int(input('Ending intiger :'))

oddcount=0
evencount=0
for i in range (Start, End+1) :
    
    if i % 2 == 0 :
        evencount += 1
        
    else :
        oddcount += 1
        

print ('evencount={0}'.format(evencount))
print ('oddcount={0}'.format(oddcount))

