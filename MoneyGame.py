import time
import random
import requests
import math
import json
Question = input('Do you want to\n Withdraw - 1\n Deposit - 2\n Balance - 3\n Beg - 4\n Job - 5\n Work - 6\n Search - 7\n Crypto - 8\n Trader - 9\n Taxi - 10')

items_for_search = ['stick','old phone','book']


if Question == '2':
    Place = open('Place.txt','r')
    Reading_place = Place.read()
    if Reading_place == 'Bank':
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
    else:
        print(f'You are not at the bank you are at {Reading_place}')
if Question == '1':
 Place = open('Place.txt','r')
 Reading_place = Place.read()
 if Reading_place == 'Bank':
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
 else:
     print(f'You are not at the bank you are at {Reading_place}')
if Question == '3':
 Place = open('Place.txt','r')
 Reading_place = Place.read()
 if Reading_place == 'Bank':
    Banka = open('Banka.txt','r')
    Dzep = open('Dzep.txt','r')
    Pare_u_banci = Banka.read()
    Pare_u_dzepu = Dzep.read()
    print(f'You have ${Pare_u_banci} in your bank and ${Pare_u_dzepu} in your pocket ')
 else:
     print(f'You are not at the bank you are at {Reading_place}')
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
    Place = open('Place.txt', 'r')
    Reading_place = Place.read()
    if Reading_place == 'Job':
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
    else:
        print(f'You are not at your job you are at {Reading_place}')

if Question == '7':
    random_choice_for_search = random.randint(1,3)
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
    if random_choice_for_search == 3:
        random_item_choice = random.choice(items_for_search)
        if random_item_choice == "stick":
            with open('inventory.json','r+') as f:
                data = json.load(f)
                data2 = data['data'][0]['stick_count']
                random_sticks_choice = random.randint(1,3)
                sticks = data2 + random_sticks_choice
                data2 = data['data'][0]['stick_count'] = sticks
                with open('inventory.json','w') as f:
                    json.dump(data,f)
                print(f'You found {random_sticks_choice} sticks')
                print(f'You now have {sticks} sticks')
        if random_item_choice == "old phone":
            with open('inventory.json','r+') as f:
                data = json.load(f)
                data2 = data['data'][1]['old_phone_count']
                random_old_phone_choice = random.randint(0,1)
                if random_old_phone_choice == 0:
                    print('Unfortunately you found 0 old phones')
                else:
                    old_phones = data2 + random_old_phone_choice
                    data2 = data['data'][1]['old_phone_count'] = old_phones
                    with open('inventory.json','w') as f:
                        json.dump(data,f)
                    print(f'You found {random_old_phone_choice} old phone')
                    print(f'You now have {old_phones} old phones')
        if random_item_choice == 'book':
            with open('inventory.json','r+') as f:
                data = json.load(f)
                data2 = data['data'][2]['book_count']
                random_book_choice = random.randint(0,1)
                if random_book_choice == 0:
                    print('Unfortunately you found 0 books')
                else:
                    book = data2 + random_book_choice
                    data2 = data['data'][2]['book_count'] = book
                    with open('inventory.json','w') as f:
                        json.dump(data,f)
                    print(f'You found {random_book_choice} book')
                    print(f'You now have {book} books')






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
        input4 = str(input('Do you want to Buy or Sell?'))
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
if Question == '9':
 Place = open('Place.txt','r')
 Reading_place = Place.read()
 if Reading_place == 'Trader':
    print('Hello i am the trader, do you wish to buy or sell some items?')
    input10 = str(input('Buy or Sell? :'))
    if input10 == 'Sell':
        opening_json = open('inventory.json')
        data1 = json.load(opening_json)
        data2 = data1['data']
        print('Your inventory')
        for i in data2:
            print(i)

        input11 = str(input('What do you wish to sell? :'))
        if input11 == 'stick':
            input12 = int(input('How much sticks do you wish to sell? :'))
            with open('inventory.json','r+') as f:
                data = json.load(f)
                data2 = data['data'][0]['stick_count']
            if data2 >= input12:
                with open('inventory.json', 'r+') as f:
                    data = json.load(f)
                    data2 = data['data'][0]['stick_count']
                    sticks = data2 - input12
                    data2 = data['data'][0]['stick_count'] = sticks
                    with open('inventory.json', 'w') as f:
                        json.dump(data, f)
                    print(f'You now have {sticks} sticks')
                with open('Dzep.txt','r') as d:
                    Dzep = d.read()
                with open('Dzep.txt','w') as d:
                    multiply_input12 = input12 * 1
                    Dzep_stick = int(Dzep) + multiply_input12
                    d.write(f'{Dzep_stick}')
                    print(f'You sold {input12} sticks for {multiply_input12}$')
                    print(f'You now have {Dzep_stick}$ in your pocket')
            else:
                print('You dont have that much sticks')
        if input11 == 'old phone':
            input12 = int(input('How much old phones do you wish to sell? :'))
            with open('inventory.json','r+') as f:
                data = json.load(f)
                data2 = data['data'][1]['old_phone_count']
            if data2 >= input12:
                with open('inventory.json', 'r+') as f:
                    data = json.load(f)
                    data2 = data['data'][1]['old_phone_count']
                    old_phones = data2 - input12
                    data2 = data['data'][1]['old_phone_count'] = old_phones
                    with open('inventory.json', 'w') as f:
                        json.dump(data, f)
                    print(f'You now have {old_phones} old phones')
                with open('Dzep.txt','r') as d:
                    Dzep = d.read()
                with open('Dzep.txt','w') as d:
                    random_phone_money_choice = random.randint(50,100)
                    multiply_input12 = input12 * random_phone_money_choice
                    Dzep_old_phone = int(Dzep) + multiply_input12
                    d.write(f'{Dzep_old_phone}')
                    print(f'You sold {input12} old phones for {multiply_input12}$')
                    print(f'You now have {Dzep_old_phone}$ in your pocket')
            else:
                print('You dont have that much old phones')
        if input11 == 'book':
            input12 = int(input('How much books do you wish to sell? :'))
            with open('inventory.json','r+') as f:
                data = json.load(f)
                data2 = data['data'][2]['book_count']
            if data2 >= input12:
                with open('inventory.json', 'r+') as f:
                    data = json.load(f)
                    data2 = data['data'][2]['book_count']
                    books = data2 - input12
                    data2 = data['data'][2]['book_count'] = books
                    with open('inventory.json', 'w') as f:
                        json.dump(data, f)
                    print(f'You now have {books} books')
                with open('Dzep.txt','r') as d:
                    Dzep = d.read()
                with open('Dzep.txt','w') as d:
                    random_book_money_choice = random.randint(10,30)
                    multiply_input12 = input12 * random_book_money_choice
                    Dzep_book = int(Dzep) + multiply_input12
                    d.write(f'{Dzep_book}')
                    print(f'You sold {input12} books for {multiply_input12}$')
                    print(f'You now have {Dzep_book}$ in your pocket')
            else:
                print('You dont have that much books')
    if input10 == 'Buy':
        input13 = str(input('Welcome, what do you wish to buy?\n Stick - 2$\n Old Phone - 120$\n Phone - 500$\n Book - 20$'))
        if input13 == 'Stick':
            input14 = int(input('How much sticks do you wish to buy? :'))
            with open('inventory.json','r') as f:
                data = json.load(f)
                data2 = data['data'][0]['stick_count']
                data3 = data2 + input14
                data2 = data['data'][0]['stick_count'] = data3
                with open('inventory.json','w') as f:
                    json.dump(data,f)
                print(f'You now have {data3} sticks')
                Dzep = open('Dzep.txt','r')
                Reading_Dzep = Dzep.read()
                Reading_Dzep_input14 = input14 * 2
                Reading_Dzep_Reading_Dzep_input14 = int(Reading_Dzep) - Reading_Dzep_input14
                if Reading_Dzep_Reading_Dzep_input14 > 0:
                    Dzep = open('Dzep.txt','w')
                    Dzep.write(f'{Reading_Dzep_Reading_Dzep_input14}')
                else:
                    with open('inventory.json', 'r') as f:
                        data = json.load(f)
                        data2 = data['data'][0]['stick_count']
                        data3 = data2 - input14
                        data2 = data['data'][0]['stick_count'] = data3
                        with open('inventory.json', 'w') as f:
                            json.dump(data, f)
                        print(f'Unfortuneatly you dont have enough money to buy {input14} sticks')
        if input13 == 'Old Phone':
            input14 = int(input('How much old phones do you wish to buy? :'))
            with open('inventory.json','r') as f:
                data = json.load(f)
                data2 = data['data'][1]['old_phone_count']
                data3 = data2 + input14
                data2 = data['data'][1]['old_phone_count'] = data3
                with open('inventory.json','w') as f:
                    json.dump(data,f)
                print(f'You now have {data3} old phones')
                Dzep = open('Dzep.txt','r')
                Reading_Dzep = Dzep.read()
                Reading_Dzep_input14 = input14 * 120
                Reading_Dzep_Reading_Dzep_input14 = int(Reading_Dzep) - Reading_Dzep_input14
                if Reading_Dzep_Reading_Dzep_input14 > 0:
                    Dzep = open('Dzep.txt','w')
                    Dzep.write(f'{Reading_Dzep_Reading_Dzep_input14}')
                else:
                    with open('inventory.json', 'r') as f:
                        data = json.load(f)
                        data2 = data['data'][1]['old_phone_count']
                        data3 = data2 - input14
                        data2 = data['data'][1]['old_phone_count'] = data3
                        with open('inventory.json', 'w') as f:
                            json.dump(data, f)
                        print(f'Unfortuneatly you dont have enough money to buy {input14} old phones')
        if input13 == 'Book':
            input14 = int(input('How much books do you wish to buy? :'))
            with open('inventory.json','r') as f:
                data = json.load(f)
                data2 = data['data'][2]['book_count']
                data3 = data2 + input14
                data2 = data['data'][2]['book_count'] = data3
                with open('inventory.json','w') as f:
                    json.dump(data,f)
                print(f'You now have {data3} books')
                Dzep = open('Dzep.txt','r')
                Reading_Dzep = Dzep.read()
                Reading_Dzep_input14 = input14 * 20
                Reading_Dzep_Reading_Dzep_input14 = int(Reading_Dzep) - Reading_Dzep_input14
                if Reading_Dzep_Reading_Dzep_input14 > 0:
                    Dzep = open('Dzep.txt','w')
                    Dzep.write(f'{Reading_Dzep_Reading_Dzep_input14}')
                else:
                    with open('inventory.json', 'r') as f:
                        data = json.load(f)
                        data2 = data['data'][2]['book_count']
                        data3 = data2 - input14
                        data2 = data['data'][2]['book_count'] = data3
                        with open('inventory.json', 'w') as f:
                            json.dump(data, f)
                        print(f'Unfortuneatly you dont have enough money to buy {input14} books')
        if input13 == 'Phone':
            input14 = int(input('How much phones do you wish to buy? :'))
            with open('inventory.json','r') as f:
                data = json.load(f)
                data2 = data['data'][3]['phone_count']
                data3 = data2 + input14
                data2 = data['data'][3]['phone_count'] = data3
                with open('inventory.json','w') as f:
                    json.dump(data,f)
                print(f'You now have {data3} phones')
                Dzep = open('Dzep.txt','r')
                Reading_Dzep = Dzep.read()
                Reading_Dzep_input14 = input14 * 500
                Reading_Dzep_Reading_Dzep_input14 = int(Reading_Dzep) - Reading_Dzep_input14
                if Reading_Dzep_Reading_Dzep_input14 > 0:
                    Dzep = open('Dzep.txt','w')
                    Dzep.write(f'{Reading_Dzep_Reading_Dzep_input14}')
                else:
                    with open('inventory.json', 'r') as f:
                        data = json.load(f)
                        data2 = data['data'][3]['phone_count']
                        data3 = data2 - input14
                        data2 = data['data'][3]['phone_count'] = data3
                        with open('inventory.json', 'w') as f:
                            json.dump(data, f)
                        print(f'Unfortuneatly you dont have enough money to buy {input14} phones')
 else:
     print(f'You are not at the tarders place you are at {Reading_place}')
if Question == '10':
        input15 = str(input('Hi, where do you wish to go\n Bank - 50$\n Home - 20$ \n Trader - 30$ \n Job - 25$'))
        if input15 == 'Bank':
            Dzep = open('Dzep.txt','r')
            Reading_Dzep = Dzep.read()
            if int(Reading_Dzep) >= 50:
             Reading_Dzep_Bank = int(Reading_Dzep) - 50
             Dzep = open('Dzep.txt','w')
             Dzep.write(f'{Reading_Dzep_Bank}')
             print('Ok we will arrive in 10 minutes')
             time.sleep(0.5)
             print('Driving...')
             time.sleep(10)
             print('We arrived at the bank, have a good day!')
             Place = open('Place.txt','w')
             Place.write('Bank')
            else:
                print('You dont have enough money in your pocket')
        if input15 == 'Home':
            Dzep = open('Dzep.txt','r')
            Reading_Dzep = Dzep.read()
            if int(Reading_Dzep) >= 20:
             Reading_Dzep_Home = int(Reading_Dzep) - 20
             Dzep = open('Dzep.txt','w')
             Dzep.write(f'{Reading_Dzep_Home}')
             print('Ok we will arrive in 4 minutes')
             time.sleep(0.5)
             print('Driving...')
             time.sleep(4)
             print('We arrived at your house, have a good day!')
             Place = open('Place.txt','w')
             Place.write('Home')
            else:
                print('You dont have enough money in your pocket')
        if input15 == 'Trader':
            Dzep = open('Dzep.txt','r')
            Reading_Dzep = Dzep.read()
            if int(Reading_Dzep) >= 30:
             Reading_Dzep_Trader = int(Reading_Dzep) - 30
             Dzep = open('Dzep.txt','w')
             Dzep.write(f'{Reading_Dzep_Trader}')
             print('Ok we will arrive in 6 minutes')
             time.sleep(0.5)
             print('Driving...')
             time.sleep(6)
             print('We arrived at the Trader place, have a good day!')
             Place = open('Place.txt','w')
             Place.write('Trader')
            else:
                print('You dont have enough money in your pocket')
        if input15 == 'Job':
            Dzep = open('Dzep.txt','r')
            Reading_Dzep = Dzep.read()
            if int(Reading_Dzep) >= 50:
             Reading_Dzep_Job = int(Reading_Dzep) - 25
             Dzep = open('Dzep.txt','w')
             Dzep.write(f'{Reading_Dzep_Job}')
             print('Ok we will arrive in 5 minutes')
             time.sleep(0.5)
             print('Driving...')
             time.sleep(5)
             print('We arrived at your job, have a good day!')
             Place = open('Place.txt','w')
             Place.write('Job')
            else:
                print('You dont have enough money in your pocket')





