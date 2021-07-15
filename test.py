# -*- coding: utf-8 -*-
print("hello world")
print("モテたい")

演算
print(1+1)
print(1-1)
print(1*1)
print(10/2)
print(5%3)

変数
unko = 'L_size'
unko_length = 2
unko_times = 5.5

# print (unko_length)

# 条件分岐
# if else elif
# ? == != < > >= <=
if unko_length > 6:
    print('ooi')
elif unko_length == 0:
    print('nai')
else:
    print('sukunai')

関数
def unko_funbaru(arg):
    unko_status = arg

    if(unko_status < 10):
        return 'mada daijobu'
    else:
        return 'yabai'

# print(unko_funbaru(10))

# list
unko_list = ['unko_small','unko_medium','unko_large']
# print(unko_list[1])

# for
# for index in range(11):
#     print(unko_funbaru(index))
for item in unko_list:
    print(item)

with
open()
with open('./unko.text','r') as file:
    print(file.read())

class
class Card:
    def __init__(self,date,user_name):
        self.date = date
        self.user_name =user_name
    def message(self):
        return 'この投稿は' + self.user_name + 'さんが' + self.date + '投稿しました'

date_a ='2020-01-01'
user_name_a = 'taro'
card_a = Card(date_a,user_name_a)

date_b ='2020-01-03'
user_name_b = 'kayoko'
card_b = Card(date_b,user_name_b)

print(card_b.message())

import文
import xxx