import sys
sys.path.append('f:\Reverse\NewStar week 5\lock\check.pyd')
import check


print('''
                                                                    
 /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ 
|______/|______/|______/|______/|______/|______/|______/
                                                                  
 /$$$$         /$$$$$$             /$$$$$$         /$$$$                  
| $$_/        /$$$_  $$           /$$__  $$       |_  $$                  
| $$         | $$$$\\ $$ /$$   /$$| $$  \\ $$         | $$                  
| $$         | $$ $$ $$|  $$ /$$/| $$$$$$$$         | $$                  
| $$         | $$\\ $$$$ \\  $$$$/ | $$__  $$         | $$                  
| $$         | $$ \\ $$$  >$$  $$ | $$  | $$         | $$                  
| $$$$       |  $$$$$$/ /$$/\\  $$| $$  | $$        /$$$$                  
|____/        \\______/ |__/  \\__/|__/  |__/       |____/                                                                                                                                                     
 /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$
|______/|______/|______/|______/|______/|______/|______/
                                                                                                                                                                    
''')
print('''The secret is locked.
You must enter the correct password to unlock it.
Hint: The password is 20 characters long and only contains letters and numbers from 0 to f.
      
''')


while True:
    password = input('\npassword>')
    ret = check.check(password)
    
    if ret == 20:
        print('\nCongratulation!\nFlag is flag{your_input.lower()}')
        break

    if ret == 114:
        print('Error input: only 0-f allowed. Lower case needed.')
        continue

    if ret == 514:
        print('Error length.')
        continue

    print(f'[{ret}] Good [{20-ret}] Bad , try again.')
