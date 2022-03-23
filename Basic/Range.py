lower=int(input('Enter lower number of range: '))
upper=int(input('Enter highest number of range: '))
x=range(lower,upper)
print(f'Even numbers from {lower} to {upper}: ')
for a in x:
    if a%2==0:
        print(a)
        