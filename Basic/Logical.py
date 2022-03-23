name='Rohel'
name_len=len(name)
if name_len<3:
    print('Name must be more than 3 digit and less than 50')
elif name_len>50:
    print('Name must be less than 50 digit')
else:
    print("Name looks good")
    
    
    # if name_len<3 or name_len>50: