from system import ExpenseSharingSystem, SplitType, Split

def main():
    system = ExpenseSharingSystem()

    ali = system.create_user("Ali", "ali@example.com", ["0300-1234567"])
    sara = system.create_user("Sara", "sara@example.com", ["0311-7654321"])
    ahmed = system.create_user("Ahmed", "ahmed@example.com", ["0322-9988776"])

    print(f"Users created: {ali.name}, {sara.name}, {ahmed.name}")

    friends = system.create_group("Friends", ali.user_id)
    system.add_to_group(friends.group_id, sara.user_id)
    system.add_to_group(friends.group_id, ahmed.user_id)
    print(f"Group '{friends.name}' created with 3 members.")

    print("\nAdding Expense: Ali paid 3000 for Dinner (Equal Split)")
    splits_dinner = [
        Split(ali.user_id),
        Split(sara.user_id),
        Split(ahmed.user_id)
    ]
    system.add_expense("Dinner", 3000, ali.user_id, SplitType.EQUAL, splits_dinner, friends.group_id)


    print("Adding Expense: Sara paid 1500 for Fuel (Equal Split)")
    splits_fuel = [
        Split(ali.user_id),
        Split(sara.user_id),
        Split(ahmed.user_id)
    ]
    system.add_expense("Fuel", 1500, sara.user_id, SplitType.EQUAL, splits_fuel, friends.group_id)


    print("\n--- Final Balances (Who owes whom) ---")
    balances = system.get_balances()
    if not balances:
        print("All settled!")
    for debtor_id, creditor_id, amount in balances:
        debtor = system.users[debtor_id].name
        creditor = system.users[creditor_id].name
        print(f"{debtor} owes {creditor}: {amount}")

    print("\n--- Net Balances ---")
    for u_id, user in system.users.items():
        net = system.get_user_net_balance(u_id)
        status = "Credit" if net > 0 else "Debt" if net < 0 else "Settled"
        print(f"{user.name}: {round(net, 2)} ({status})")

    print("\nAhmed settles part of his debt to Ali (500)")
    system.settle_payment(ahmed.user_id, ali.user_id, 500)
    
    print("\n--- Updated Balances after partial settlement ---")
    new_balances = system.get_balances()
    for debtor_id, creditor_id, amount in new_balances:
        debtor = system.users[debtor_id].name
        creditor = system.users[creditor_id].name
        print(f"{debtor} owes {creditor}: {amount}")

if __name__ == "__main__":
    main()
