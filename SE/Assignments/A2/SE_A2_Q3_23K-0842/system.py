from models import User, Group, Expense, Split, SplitType
from engine import BalanceEngine, SplitValidator
from typing import Dict, List, Optional
import uuid

class ExpenseSharingSystem:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.groups: Dict[str, Group] = {}
        self.expenses: List[Expense] = []
        self.engine = BalanceEngine()


    def create_user(self, name: str, email: str, phones: List[str]) -> User:
        if any(u.email == email for u in self.users.values()):
            raise ValueError(f"User with email {email} already exists.")
        
        user_id = str(uuid.uuid4())[:8]
        user = User(user_id, name, email, phones)
        self.users[user_id] = user
        return user

    def create_group(self, name: str, admin_id: str) -> Group:
        if admin_id not in self.users:
            raise ValueError("Admin user does not exist.")
        
        group_id = str(uuid.uuid4())[:8]
        group = Group(group_id, name)
        group.add_member(admin_id)
        group.add_admin(admin_id)
        self.groups[group_id] = group
        return group

    def add_to_group(self, group_id: str, user_id: str):
        if group_id not in self.groups: raise ValueError("Group not found")
        if user_id not in self.users: raise ValueError("User not found")
        self.groups[group_id].add_member(user_id)

    def add_expense(self, description: str, amount: float, paid_by: str, 
                    split_type: SplitType, splits: List[Split], group_id: Optional[str] = None):
        
        if paid_by not in self.users: raise ValueError("Payer not found")
        if amount <= 0: raise ValueError("Amount must be positive")

        if split_type == SplitType.EQUAL:
            share = amount / len(splits)
            for s in splits:
                s.amount = share
        elif split_type == SplitType.PERCENT:
            total_pct = sum(s.percentage for s in splits)
            if abs(total_pct - 100) > 0.01:
                raise ValueError("Total percentage must be 100")
            for s in splits:
                s.amount = (s.percentage * amount) / 100
        elif split_type == SplitType.EXACT:
            total_exact = sum(s.amount for s in splits)
            if abs(total_exact - amount) > 0.01:
                raise ValueError("Total splits must equal amount")

        expense_id = str(uuid.uuid4())[:8]
        expense = Expense(expense_id, description, amount, paid_by, split_type, splits, group_id)
        self.expenses.append(expense)

        for s in splits:
            if s.user_id != paid_by:
                self.engine.update_balance(s.user_id, paid_by, s.amount)

        return expense

    def settle_payment(self, debtor_id: str, creditor_id: str, amount: float):
        if debtor_id not in self.users or creditor_id not in self.users:
            raise ValueError("User not found")
        self.engine.update_balance(creditor_id, debtor_id, amount)

    def get_balances(self):
        return self.engine.simplify_debts()

    def get_user_net_balance(self, user_id: str):
        net = self.engine.get_net_balances()
        return net.get(user_id, 0.0)
