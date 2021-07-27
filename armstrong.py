
def armstrong_validator(length):
    """This function will create a number from scratch in selected length and given integers 
    by user than check if produced number is an armstrong number or not."""
    count=0
    number=[] 
    while count<length:
        value=int(input("Dear user please write an integer between i>=0 and i<10 : "))
        number.append(value)
        count+=1
        
        continue
        if count==len:
            break
        count+=1
    test_number=0
    for i in range(count):
            count-=1
            test_number+=number[i]*10** count
            #print(number[i],count)

    total=0
    count=len(number)
    for i in range(count):
        total+=number[i]**count
    if(total==test_number):
        print(test_number, ' is an armstrong number!')
    else:
        print('sorry',test_number, 'is not an armstrong number!')
    
armstrong_validator(int(input('give a length please : ')))

        
        