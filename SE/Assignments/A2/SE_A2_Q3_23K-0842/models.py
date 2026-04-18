from dataclasses import dataclass, field
from typing import List, Dict, Set, Optional
from enum import Enum

class SplitType(Enum):
    EQUAL = "EQUAL"
    EXACT = "EXACT"
    PERCENT = "PERCENT"

@dataclass
class User:
    user_id: str
    name: str
    email: str
    phone_numbers: List[str] = field(default_factory=list)

    def add_phone(self, phone: str):
        if phone not in self.phone_numbers:
            self.phone_numbers.append(phone)

@dataclass
class Group:
    group_id: str
    name: str
    members: Set[str] = field(default_factory=set)
    admins: Set[str] = field(default_factory=set)

    def add_member(self, user_id: str):
        self.members.add(user_id)

    def remove_member(self, user_id: str):
        if user_id in self.members:
            self.members.remove(user_id)
            if user_id in self.admins:
                self.admins.remove(user_id)

    def add_admin(self, user_id: str):
        if user_id in self.members:
            self.admins.add(user_id)

@dataclass
class Split:
    user_id: str
    amount: float = 0.0
    percentage: float = 0.0

@dataclass
class Expense:
    expense_id: str
    description: str
    amount: float
    paid_by: str  # user_id
    split_type: SplitType
    splits: List[Split]
    group_id: Optional[str] = None
