from typing import Dict, List, Tuple
import heapq

class BalanceEngine:
    def __init__(self):
        self.user_balances: Dict[str, Dict[str, float]] = {}

    def update_balance(self, debtor: str, creditor: str, amount: float):
        if debtor == creditor:
            return
        
        if debtor not in self.user_balances:
            self.user_balances[debtor] = {}
        if creditor not in self.user_balances:
            self.user_balances[creditor] = {}
        
        self.user_balances[debtor][creditor] = self.user_balances[debtor].get(creditor, 0.0) - amount
        self.user_balances[creditor][debtor] = self.user_balances[creditor].get(debtor, 0.0) + amount

    def get_net_balances(self) -> Dict[str, float]:
        net_balances = {}
        for user, balances in self.user_balances.items():
            net_balances[user] = sum(balances.values())
        return net_balances

    def simplify_debts(self) -> List[Tuple[str, str, float]]:
        net_balances = self.get_net_balances()
        
        # Min-heap for debtors (negative balance)
        debtors = []
        # Max-heap for creditors (positive balance)
        creditors = []
        
        for user, balance in net_balances.items():
            if balance < -0.01: # Small epsilon for float comparison
                heapq.heappush(debtors, (balance, user))
            elif balance > 0.01:
                heapq.heappush(creditors, (-balance, user)) # Negate for max-heap
        
        transactions = []
        while debtors and creditors:
            debt_val, debtor_id = heapq.heappop(debtors)
            credit_val, creditor_id = heapq.heappop(creditors)
            credit_val = -credit_val # Convert back to positive
            
            settled_amount = min(-debt_val, credit_val)
            transactions.append((debtor_id, creditor_id, round(settled_amount, 2)))
            
            new_debt = debt_val + settled_amount
            new_credit = credit_val - settled_amount
            
            if new_debt < -0.01:
                heapq.heappush(debtors, (new_debt, debtor_id))
            if new_credit > 0.01:
                heapq.heappush(creditors, (-new_credit, creditor_id))
                
        return transactions

class SplitValidator:
    @staticmethod
    def validate_splits(amount: float, split_type: str, splits: List) -> bool:
        if not splits:
            return False
        
        if split_type == "EQUAL":
            return True
        
        total = sum(s.amount if split_type == "EXACT" else (s.percentage * amount / 100) for s in splits)
        return abs(total - amount) < 0.01
