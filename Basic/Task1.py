weight=float(input('Enter your weight: '))
measure=input('(L)bs or (K)g:')
if measure == 'l' or measure == 'L':
    weight=weight*0.4535
    print(f"Your weight in Kg: {weight}")
elif measure == 'k' or measure == 'K':
    weight=weight*2.204
    print(f"Your weight in Pounds: {weight}")
else:
    print('Wrong choice !!')

# if measure.upper()=='L':