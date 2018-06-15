import os
os.system("cls")

import time
from time import sleep
i = 0
bag =  ['axe', 'knife', 'mashroom']
exet = 0
from time import*
from random import*
from colorama import Fore, Back,Style,init
init()
seed(clock())
hp0 = 100
hp1 = 100
damage = randrange(15) + 1
def fight():
	global hp1
	global hp0
	global exet
	while hp1 >= 0 or hp0 >= 0:
		print('bad guy HP: ' , hp0 , 'your HP: ' , hp1)
		damage = randrange(15) + 1
		hp0 = hp0 - damage
		if hp1 < 0 :
			hp1 = 0
			sleep(1)
			print('bad guy HP: ' , hp0 , 'your HP: ' , hp1)
			break
		elif hp0< 0 :
			hp0 = 0
			sleep(1)
			print('bad guy HP: ' , hp0 , 'your HP: ' , hp1)
			break
		print('bad guy HP: ' , hp0 , 'your HP: ' , hp1)
		damage = randrange(15) + 1
		hp1 = hp1 - damage
		
		if hp1 < 0 :
			hp1 = 0
			sleep(1)
			print('bad guy HP: ' , hp0 , 'your HP: ' , hp1)
			break
		elif hp0 < 0 :
			hp0 = 0
			sleep(1)
			print('bad guy HP: ' , hp0 , 'your HP: ' , hp1)
			break
		print('bad guy HP: ' , hp0 , 'your HP: ' , hp1)
		if hp1 == 0:
			#print('Game over')
			exet = 1
			
		elif hp0 == 0:
			#print('you win \n your xp: ' + xp1)
			exet = 0
	
		
def shop():
	while 1 :
		c = int(input('Buy bandages or go away\nbuy - 1 go away - 0 show inventori| - 2 '))
		if c == 1:
			print('Buy sucsses')
			bag.append('bandage')
		elif c == 0:
			print('go away')
			break
		elif c == 2:
			for i in bag:
				print(i)




while 1 :
	
	a = randrange(4)
	if a == 1 :
		print('Обнаружен противник')
		#	if b == 0 :
		#		print('Поздравляю вы убежали ')
		#	elif b == 1 :
		#		print('Поздравляю вы победили противника ')
		fight()
		if exet == 1:
			print('Game over')
			break
			
			
		elif exet == 0:
			print('you win \n your hp: ' , hp1)




	
	elif a == 2 :
		#c = int(input('Вы встретили торговца\n купить гриб - 1 прогнать - 0 '))
		#if c == 1 :
		#		print('Поздравляю вы купили гриб ')
		#elif c == 0 :
		#		print('Вы лошара вы не купили гриб ')
		shop()
		os.system("cls")
	elif a == 0 : 
		d = int(input('Покинуть игру\n да - 1 нет - 0| '))
		if d == 1 :
			break
		os.system("cls")
	elif a == 3:
		r=str(input('Do you to save y/n'))
		if r=='y':
			f=open('save.txt','w')
			f.write(str(hp1) + '|' + str(hp0) + '|' + str(bag) + '|' + str(a) + '|')
			#l = f.read()
			f.close()
			print('save sucsses')
			break
		
