

# for i in range(1, 11):
  
    # sentence = 'The value is {:02}'.format(i)   

'''Let's try with fStrings'''    

    # sentence = f'The value is {i:.2f}'
    # it worked

    # print(sentence)


# pi = 3.14159265

# sentence = 'Pi is equal to {:.2f}'.format(pi)

sentence = '1 MB is equal to {:,} bytes'.format(1000**2)

print(sentence)