#!/usr/bin/env python
# coding: utf-8

# In[1]:


h=int(input('Hours worked: $'))
r=int(input('Wage: $'))

pay=round(h*r,2)   

choice=input('Would you like to calculate overtime?')
if choice=='yes':
    overtime=int(input('Overtime hours:'))
    overtimerate=r*1.5
    overtimepay=overtime*overtimerate
    totalpay=round(overtimepay+pay,2)


annual=totalpay*52 
bipay=totalpay*2

union=bipay*.01
retire=(annual*.045)/26
state=bipay*.06

if annual>=10276 and annual<=41775:
    fedtax=(annual*.12)/26
    if annual>=41776 and annual<=89075:
        fedtax=(annual*.22)/26
        if annual>=89076 and annual<=170050:
            fedtax=(annual*.24)/26
            if annual>=170051 and annual<=215950:
                fedtax=(annual*.32)/26
x=147000
if annual <=147000:
    sstax=(annual*.062)/26
if annual>147000:
    sstax=(x*.062)/26

y=147000
if annual <=147000:
    medicaid=(annual*.062)/26
if annual>147000:
    medicaid=(y*.062)/26
                
netpay=bipay-union-retire-state-fedtax-sstax-medicaid
deductions=union+retire+state+fedtax+sstax+medicaid

a=input('Enter first name:')
b=input('Enter last name:')

import random
random_digits=random.randint(100000,999999)

print("\nEmployee ID:"+a[0].title()+b[0].title()+str((random_digits)))
print('Name:',a.title(),b.title())
print('\nBiweekly total: $',round(bipay,2))
print('Regular time: $',round(pay,2))
print('Over time: $', round(overtimepay,2))
print('\nDeductions: $', round(deductions,2))
print('Union fees: $',round(union,2))
print('Retirement fund: $', round(retire,2))
print('State taxes: $', round(state,2))
print('Federal taxes: $', round(fedtax,2))
print('Social security: $', round(sstax,2))
print('Medicaid: $', round(medicaid,2))

print('\nNet pay: $', round(netpay,2))


# In[ ]:





# In[ ]:




