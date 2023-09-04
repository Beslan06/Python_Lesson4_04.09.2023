def apply_tax(amount, tax_rate):
    return amount - amount * tax_rate

def deposit(balance, op_count, transactions):
    amount = int(input("Введите сумму для пополнения: "))
    if amount % 50 == 0:
        tax_rate = 0.10
        if op_count % 3 == 2:
            tax_rate += 0.03
        balance += apply_tax(amount, tax_rate)
        op_count += 1
        transactions.append(f"Пополнение: +{amount} у.е.")
    return balance, op_count

def withdraw(balance, op_count, transactions):
    amount = int(input("Введите сумму для снятия: "))
    if amount % 50 == 0 and amount <= balance:
        fee = min(max(amount * 0.015, 30), 600)
        balance -= amount + fee
        op_count += 1
        transactions.append(f"Снятие: -{amount} у.е. (включая комиссию {fee} у.е.)")
    return balance, op_count

def main():
    balance, op_count = 0, 0
    transactions = []

    while True:
        print(f"Баланс: {balance} у.е.")
        action = input("Действие (пополнить/снять/выйти): ")

        if action == "пополнить":
            balance, op_count = deposit(balance, op_count, transactions)
        elif action == "снять":
            balance, op_count = withdraw(balance, op_count, transactions)
        elif action == "выйти":
            print("Программа завершена.")
            break
        else:
            print("Неверное действие. Попробуйте снова.")

        if balance > 5000000:
            balance = apply_tax(balance, 0.10)

    print("Операции:")
    for transaction in transactions:
        print(transaction)

if __name__ == "__main__":
    main()
