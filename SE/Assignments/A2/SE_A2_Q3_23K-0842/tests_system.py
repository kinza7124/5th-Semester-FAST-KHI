import unittest
from system import ExpenseSharingSystem, SplitType, Split

class TestSmartExpenseSystem(unittest.TestCase):
    def setUp(self):
        self.system = ExpenseSharingSystem()
        self.u1 = self.system.create_user("User1", "u1@test.com", ["111"])
        self.u2 = self.system.create_user("User2", "u2@test.com", ["222"])
        self.u3 = self.system.create_user("User3", "u3@test.com", ["333"])

    def test_unique_email_validation(self):
        with self.assertRaises(ValueError):
            self.system.create_user("Dupe", "u1@test.com", ["000"])

    def test_group_management(self):
        group = self.system.create_group("Test Group", self.u1.user_id)
        self.system.add_to_group(group.group_id, self.u2.user_id)
        self.assertIn(self.u1.user_id, group.members)
        self.assertIn(self.u2.user_id, group.members)
        self.assertIn(self.u1.user_id, group.admins)

    def test_equal_split_calculation(self):
        splits = [Split(self.u1.user_id), Split(self.u2.user_id)]
        self.system.add_expense("Lunch", 100, self.u1.user_id, SplitType.EQUAL, splits)
        # User2 should owe User1 50
        self.assertEqual(self.system.get_user_net_balance(self.u2.user_id), -50.0)
        self.assertEqual(self.system.get_user_net_balance(self.u1.user_id), 50.0)

    def test_exact_split_validation(self):
        splits = [Split(self.u1.user_id, amount=60), Split(self.u2.user_id, amount=40)]
        self.system.add_expense("Taxis", 100, self.u1.user_id, SplitType.EXACT, splits)
        self.assertEqual(self.system.get_user_net_balance(self.u2.user_id), -40.0)

    def test_exact_split_invalid_sum(self):
        splits = [Split(self.u1.user_id, amount=60), Split(self.u2.user_id, amount=30)]
        with self.assertRaises(ValueError):
            self.system.add_expense("Error", 100, self.u1.user_id, SplitType.EXACT, splits)

    def test_percentage_split_calculation(self):
        splits = [Split(self.u1.user_id, percentage=75), Split(self.u2.user_id, percentage=25)]
        self.system.add_expense("Gift", 1000, self.u1.user_id, SplitType.PERCENT, splits)
        self.assertEqual(self.system.get_user_net_balance(self.u2.user_id), -250.0)

    def test_debt_simplification_linear(self):
        # U2 owes U1 100
        self.system.add_expense("Ex1", 200, self.u1.user_id, SplitType.EQUAL, 
                                [Split(self.u1.user_id), Split(self.u2.user_id)])
        # U3 owes U2 100
        self.system.add_expense("Ex2", 200, self.u2.user_id, SplitType.EQUAL, 
                                [Split(self.u2.user_id), Split(self.u3.user_id)])
        
        # Simplified: U3 owes U1 100 directly
        balances = self.system.get_balances()
        self.assertEqual(len(balances), 1)
        self.assertEqual(balances[0], (self.u3.user_id, self.u1.user_id, 100.0))

    def test_circular_debt_resolution(self):
        # A owes B 100, B owes C 100, C owes A 100 -> All 0
        self.system.engine.update_balance(self.u1.user_id, self.u2.user_id, 100)
        self.system.engine.update_balance(self.u2.user_id, self.u3.user_id, 100)
        self.system.engine.update_balance(self.u3.user_id, self.u1.user_id, 100)
        
        balances = self.system.get_balances()
        self.assertEqual(len(balances), 0)

    def test_settlement(self):
        self.system.engine.update_balance(self.u1.user_id, self.u2.user_id, 100)
        self.system.settle_payment(self.u1.user_id, self.u2.user_id, 40)
        self.assertEqual(self.system.get_user_net_balance(self.u1.user_id), -60.0)

    def test_invalid_negative_amount(self):
        with self.assertRaises(ValueError):
            self.system.add_expense("Fail", -10, self.u1.user_id, SplitType.EQUAL, [])

if __name__ == "__main__":
    unittest.main()
