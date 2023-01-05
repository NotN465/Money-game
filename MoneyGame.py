import time
import random
import requests
import math
Question = input('Do you want to\n Withdraw - 1\n Deposit - 2\n Balance - 3\n Beg - 4\n Job - 5\n Work - 6\n Search - 7\n Crypto')

if Question == '2':
      deposit = int(input('how much would you like to deposit?'))
      Deposit = open("Dzep.txt", 'r')
      Money_in_pocket = int(Deposit.read())
      if deposit <= Money_in_pocket:
          minus_balance = Money_in_pocket - deposit
          Deposit = open("Dzep.txt", 'w')
          Deposit.write(f'{minus_balance}')
          Deposit = open("Dzep.txt", 'r')
          Reading_deposit = Deposit.read()
          print(f'You have ${Reading_deposit} in your pocket')
          Bankomat = open("Banka.txt", 'r')
          Stanje_Bankomata = Bankomat.read()
          Bankomat = open("Banka.txt", 'w')
          Total_Money = int(Stanje_Bankomata) + deposit
          Bankomat.write(f"{Total_Money}")
          Bankomat = open("Banka.txt", 'r')
          Reading_Bankomat = Bankomat.read()
          print(f'You have ${Reading_Bankomat} in your bank')


      else:
          print('You dont have enough money')
if Question == '1':
    withdraw = int(input('much would you like to withdraw'))
    Withdraw = open('Banka.txt', 'r')
    Withdraw3 = int(Withdraw.read())
    if Withdraw3 >= withdraw:
        Taking_money = Withdraw3 - withdraw
        Withdraw = open('Banka.txt', 'w')
        Withdraw.write(f'{Taking_money}')
        Withdraw = open('Banka.txt', 'r')
        Reading_Withdraw = Withdraw.read()
        print(f'You have ${Reading_Withdraw} in your bank')
        Withdraw2 = open('Dzep.txt', 'r')
        Stanje__dzepu = Withdraw2.read()
        Withdraw2 = open('Dzep.txt', 'w')
        Stanje__dzepu_i_withdraw = int(Stanje__dzepu) + withdraw
        Withdraw2.write(f'{Stanje__dzepu_i_withdraw}')
        Withdraw2 = open('Dzep.txt', 'r')
        Reading_Withdraw2 = Withdraw2.read()
        print(f'You have ${Reading_Withdraw2} in your pocket')
    else:
        print('ako ovo neradi previse cu vremena potrosit na skriptu koju sam vec napravio.')
if Question == '3':
    Banka = open('Banka.txt','r')
    Dzep = open('Dzep.txt','r')
    Pare_u_banci = Banka.read()
    Pare_u_dzepu = Dzep.read()
    print(f'You have ${Pare_u_banci} in your bank and ${Pare_u_dzepu} in your pocket ')
if Question == '4':
    Dzep1 = open('Dzep.txt','r')
    Reading_Dzep1 = Dzep1.read()
    print('You are begging for money...')
    time.sleep(3)
    random_beg_money = random.randint(1,10)
    print(f'Someone gave you ${random_beg_money}')
    Dzep = open('Dzep.txt','w')
    Adding_Dzep_and_beg = int(Reading_Dzep1) + random_beg_money
    Dzep.write(f'{Adding_Dzep_and_beg}')
if Question == '5':
    Job = open('Job.txt','w')
    input2 = str(input('Do you wish to change or set a job? Type Yes to confirm:'))
#If you want a job
    if input2  == 'Yes':
        #Job picking
        input3 = int(input('Do you wish to work as\n Mechanical Enginner - 1\n Doctor - 2\n Construction worker - 3'))
        if input3 == 1:
            Job = open('Job.txt', 'w')
            Job.write('Mechanical Enginner')
            print('You now work as a Mechanical Enginner')
        if input3 == 2:
            Job = open('Job.txt', 'w')
            Job.write('Doctor')
            print('You now work as a Doctor')
        if input3 == 3:
            Job = open('Job.txt', 'w')
            Job.write('Construction worker')
            print('You now work as a Construction worker')
#If you already have a job
if Question == '6':
        #Job paying
        Job = open('Job.txt', 'r')
        Reading_Job = Job.read()
        if Reading_Job == 'Mechanical Enginner':
            print('Working...')
            time.sleep(60)
            ME_paycheck = 1000
            print(f'Your paycheck is ${ME_paycheck}')
            Banka = open('Banka.txt','r')
            Pare_u_banci = Banka.read()
            Banka = open('Banka.txt','w')
            Placa = int(Pare_u_banci) + ME_paycheck
            Banka.write(f'{Placa}')
            Banka = open('Banka.txt','r')
            print(f'You now have ${Banka.read()}')
        if Reading_Job == 'Doctor':
            print('Working...')
            time.sleep(60)
            ME_paycheck = 2000
            print(f'Your paycheck is ${ME_paycheck}')
            Banka = open('Banka.txt','r')
            Pare_u_banci = Banka.read()
            Banka = open('Banka.txt','w')
            Placa = int(Pare_u_banci) + ME_paycheck
            Banka.write(f'{Placa}')
            Banka = open('Banka.txt','r')
            print(f'You now have ${Banka.read()}')
        if Reading_Job == 'Construction worker':
            print('Working...')
            time.sleep(60)
            ME_paycheck = 800
            print(f'Your paycheck is ${ME_paycheck}')
            Banka = open('Banka.txt','r')
            Pare_u_banci = Banka.read()
            Banka = open('Banka.txt','w')
            Placa = int(Pare_u_banci) + ME_paycheck
            Banka.write(f'{Placa}')
            Banka = open('Banka.txt','r')
            print(f'You now have ${Banka.read()}')

if Question == '7':
    random_choice_for_search = random.randint(1,2)
    if random_choice_for_search == 1:
        print('Unfortunately you found nothing')
    if random_choice_for_search == 2:
        random_money_choice = random.randint(1,5)
        print(f'Congrats! You found ${random_money_choice}')
        Dzep = open('Dzep.txt','r')
        Dzepread = Dzep.read()
        dzepread_and_random_money_choice = int(Dzepread) + random_money_choice
        Dzep = open('Dzep.txt','w')
        Dzep.write(f'{dzepread_and_random_money_choice}')
if Question == '8':
    base_url = "https://api.binance.com/api/v3"
    symbols = ["BTC"]
    prices = {}
    time.sleep(1)
    for symbol in symbols:
        url = base_url + f"/avgPrice?symbol={symbol}USDT"
        r = requests.get(url)
        prices[symbol] = r.json()["price"]
        price = prices['BTC']
        print('Crypto prices:\n''$'+price)
        Crypto =open('Crypto.txt','r')
        Reading_Crypto = Crypto.read()
        print(f'Your Crypto balance:\n{float(Reading_Crypto)*float(price)}')
        input4 = str(input('Do you wan to Buy or Sell or use Laverage?'))
        if input4 == 'Buy':
            input5 = int(input('How much do you wish to buy in dollars?'))
            Banka = open('Banka.txt','r')
            Reading_Bank = Banka.read()
            if input5 <= int(Reading_Bank):
              Input5_Reading_Bank = int(Reading_Bank) - input5
              Banka = open('Banka.txt','w')
              Banka.write(f'{Input5_Reading_Bank}')
              Crypto = open('Crypto.txt','r')
              Crypto_reading = Crypto.read()
              Crypto_reading_Input5 = float(Crypto_reading)*float(price) + float(input5)
              Crypto = open('Crypto.txt','w')
              Crypto.write(f'{float(Crypto_reading_Input5)/float(price)}')
            if input5 >= int(Reading_Bank):
                print('You dont have enough money on your bank account')
        if input4 == 'Sell':
            input6 = int(input('How much do you want to sell in dollars'))
            Crypto = open('Crypto.txt','r')
            Reading_Crypto = Crypto.read()
            if input6 <= float(Reading_Crypto) * float(price):
                Reading_Crypto_price = float(Reading_Crypto) * float(price)
                Reading_Crypto_input6 = float(Reading_Crypto_price) - float(input6)
                Crypto = open('Crypto.txt','w')
                Crypto.write(f'{float(Reading_Crypto_input6)/float(price)}')
                Banka = open('Banka.txt','r')
                Reading_Bank = Banka.read()
                Reading_Bank_input6 = int(Reading_Bank) + input6
                Banka = open('Banka.txt','w')
                Banka.write(f'{Reading_Bank_input6}')
            if input6 >= float(Reading_Crypto) * float(price):
                print('You dont have enough money on your Crypto account')
