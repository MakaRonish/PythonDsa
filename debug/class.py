def makeChange(change):
    result={}
    round=change%5
    value=None
    if round<=2:
        value=change-round
    else:
        value=change-round+5
    number_of_quater=value//25
    if number_of_quater>0:
        result["quater"]=number_of_quater
    remaining=value-(25*number_of_quater)
    if remaining>0:
        number_of_dime=remaining//10
        if number_of_dime>0:
            result["dime"]=number_of_dime
        remaining=remaining-(10*number_of_dime)
        if remaining>0:
            number_of_nickel=remaining//5
            if number_of_nickel>0:
                result["nickel"]=number_of_nickel
            remaining=remaining-(5*number_of_nickel)

    else:
        pass
    return result


print(makeChange(54))

    
    
    
                        


        



    
