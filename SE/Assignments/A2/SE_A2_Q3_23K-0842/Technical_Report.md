# Technical Report: Smart Expense Sharing System

## Part 1: Approach and Understanding
This project implements a simplified backend for a Splitwise-like platform. The core objective is to manage users, groups, and complex expense-sharing logic while ensuring financial integrity.

**System Architecture:**
- **Modular OOP Design**: The system is partitioned into `models`, `engine`, and `system` layers to maintain a single responsibility principle.
- **Complex Splitting Algorithms**:
    1. **Equal Split**: Automatically distributes amounts, handling edge cases where division results in repeating decimals.
    2. **Percentage Split**: Validates that the sum of parts equals exactly 100%.
    3. **Exact Split**: Ensures that manually entered amounts sum up to the total transaction value.
- **Debt Simplification Engine**: Implements a **Min Cash Flow Algorithm** using a greedy matching strategy with Priority Queues (heaps). This reduces O(N^2) potential transactions down to O(N).

---

## Part 2: Manual Test Case Design

| Testcase ID | Description | Input | Expected Output | Observed Output | status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Create User (Functional) | Name: Ali, Email: ali@test.com | User created with unique ID | User "Ali" created successfully | **PASS** |
| **TC-02** | Add Multi-Phones (Functional) | Phones: ["0300-1", "0311-2"] | User info updated with list | Phone numbers stored correctly | **PASS** |
| **TC-03** | Unique Email (EP - Invalid) | Email: ali@test.com (duplicate) | Raise ValueError | ValueError: email exists | **PASS** |
| **TC-04** | Create Group (Functional) | Group: "Tour", Admin: Ali | Group created, Ali is Admin | Group "Tour" created, Admin assigned | **PASS** |
| **TC-05** | Exact Split (EP - Valid) | Amt: 100, Splits: [40, 60] | Balance updated by 40 and 60 | Balances updated correctly | **PASS** |
| **TC-06** | Exact Split (EP - Invalid) | Amt: 100, Splits: [40, 50] | Raise ValueError | Error: Splits do not match amount | **PASS** |
| **TC-07** | Percent Split (EP - Invalid) | Splits: [50%, 40%] | Raise ValueError (Must be 100%) | Error: Total percentage must be 100 | **PASS** |
| **TC-08** | Zero Amount (Boundary) | Amt: 0 | Raise ValueError | Error: Amount must be positive | **PASS** |
| **TC-09** | Negative Amount (Boundary) | Amt: -50 | Raise ValueError | Error: Amount must be positive | **PASS** |
| **TC-10** | Debt simplification (Logic) | A->B $10, B->C $10 | A->C $10 | Engine returns (A, C, 10.0) | **PASS** |
| **TC-11** | Circular Settlement (Edge) | A->B, B->C, C->A ($50 each) | All balances should be $0 | Engine returns empty (0 balances) | **PASS** |
| **TC-12** | Partial Settlement (Functional) | Ahmed pays Ali 500 of 1000 | Ahmed's remaining debt: 500 | Balance updated from 1000 to 500 | **PASS** |

---

## Part 3: Automated Testing Summary
- **Framework**: Python `unittest`
- **Coverage**: 100% of core logic modules (Equal, Exact, Percent splits, Debt Simplification, User/Group management).
- **Results**: 10 tests executed, 10 tests passed.

### Automated Test Analysis:

| Test Case | Type | Objective |
| :--- | :--- | :--- |
| `test_unique_email_val` | Unit | Validates the user creation logic and unique email constraint. |
| `test_group_management` | Integration | Checks how Users and Groups interact during assignment. |
| `test_equal_split_calc` | Integration | Verifies the core math between System and the Balance Engine. |
| `test_exact_split_val` | Integration | Ensures manual split amounts are tracked correctly. |
| `test_exact_split_inv` | Unit | Tests the error handling for mismatched split amounts. |
| `test_percent_split_calc` | Integration | Validates percentage-based splitting math. |
| `test_debt_simplify_lin` | Integration | **Algorithm Test**: Verifies A->B->C simplifies to A->C. |
| `test_circular_debt_res` | Unit | **Algorithm Test**: Verifies A->B, B->C, C->A loops are cleared. |
| `test_settlement` | Integration | Checks that manual payments correctly update the ledger. |
| `test_invalid_neg_amt` | Boundary | Ensures negative financial inputs are blocked at the system level. |

---

## Part 4: Test Report Explanation

### 1. Why Specific Test Cases were Chosen
- **Functional Testing**: To ensure the core USP (splitting money) works.
- **Boundary Testing**: To prevent the "Zero/Negative" bug which could crash financial engines or allow fraud.
- **Equivalence Partitioning**: Instead of testing every number, we test "Valid" vs "Invalid" classes (e.g., Totals that sum to 100% vs those that don't).

### 2. Challenges in Testing Logic
- **Precision Matching**: Handling `33.33 + 33.34 + 33.33 = 100`. We solved this by using an epsilon threshold (0.01) in logic comparisons.
- **Complexity of Graphs**: Debt simplification converts a graph of debts into a tree/forest of transactions. Testing requires verifying the *Net Balance* remains identical before and after simplification.

### 3. Comparison: Manual vs Automated Testing
- **Manual Testing** was vital for designing the *user flow* and checking descriptive error messages. It ensures the "human" element of the requirements is met.
- **Automated Testing** is the backbone of financial calculation integrity. It allows us to verify that a change in the Simplification Algorithm doesn't break the splitting logic. It provides instant feedback for regression. 

---
