string="qwdyubsdyfvb12387@#$%^&*(jdhbfuASDFGHJKLRTYU)"
cap_count=0
low_count=0
num_count=0
for chr in string:
    if ord(chr)>=65 and ord(chr)<=90:
        cap_count+=1
    elif ord(chr)>=97 and ord(chr)<=122:
        low_count+=1
    elif ord(chr)>=48 and ord(chr)<=57:
        num_count+=1

print(f"lower case={low_count}")
print(f"capital case={cap_count}")
print(f"number ={num_count}")

cap_count=0
low_count=0
num_count=0
for chr in string:
    if "a"<=chr<="z":
        low_count+=1
    elif "A"<=chr<="Z":
        cap_count+=1
    elif "0"<=chr<="9":
        num_count+=1

print(f"lower case={low_count}")
print(f"capital case={cap_count}")
print(f"number ={num_count}")