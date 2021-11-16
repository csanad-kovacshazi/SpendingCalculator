import numpy as np

how_many_people = int(input("How many people needs to pay?: "))
spending_list = []


for counter in range(how_many_people):
    spending = int(input("How much did person " + str(counter + 1) + " spend?: "))
    spending_list.append(spending)
    

total_spending = sum(spending_list)
print("You've spent {} together".format(total_spending))

average_payment = round(total_spending / how_many_people)
print("Average payment is: " + str(average_payment))

balance_list = []
for i in range(how_many_people):
    balance = round(spending_list[i] - average_payment) #*-1 so that the person who didnt pay enough will have neg balance
    balance_list.append(balance)
    print("balance of person {} is: {}".format(i + 1, balance))


def get_payment(payment_amount, neg_balance, pos_balance, pos_balance_index, neg_balance_index):
        neg_balance = round(neg_balance + payment_amount)
        pos_balance = round(pos_balance - payment_amount)
        balance_list[pos_balance_index] = pos_balance
        balance_list[neg_balance_index] = neg_balance
        print("Person {} pays {} to person: {}".format(neg_balance_index + 1, payment_amount, pos_balance_index + 1))

while not (np.array(balance_list) == 0).all():

    neg_balance = min(balance_list)
    neg_balance_index = balance_list.index(neg_balance)
    pos_balance = max(balance_list)
    pos_balance_index = balance_list.index(pos_balance)
        
    if abs(pos_balance) > abs(neg_balance):
        payment_amount = abs(pos_balance)
        get_payment(payment_amount, neg_balance, pos_balance, pos_balance_index, neg_balance_index)
    else:
        payment_amount = abs(neg_balance)
        get_payment(payment_amount, neg_balance, pos_balance, pos_balance_index, neg_balance_index)
            

