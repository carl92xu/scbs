bin_num = list(input("Binary Number: "))
try:
    bin_num.remove(".")
except:
    pass
print(bin_num)

dec_num = 0

for i in range(len(bin_num)):
    dec_num += int(bin_num[i]) * (2 ** (7-i))

print(dec_num)
