#discount finder program
print('Welcome, in discount finder program')
price=float(input('enter the price '))
discount=int(input('enter the percentage of discount '))
final=price - (price/100*discount)
print('the final amount is '+ str(float(final)))
