# create interface (port in hexagonal architecture) for payment with stripe

from abc import ABC, abstractmethod
from typing import Any, Dict

class PaymentPort(ABC):
    @abstractmethod
    def create_customer(self, email: str, source: str) -> Dict[str, Any]:
        pass

    @abstractmethod
    def create_charge(self, amount: int, currency: str, customer_id: str, description: str) -> Dict[str, Any]:
        pass

    # optional method to check payment status
    @abstractmethod
    def check_payment(self, charge_id: str) -> Dict[str, Any]:
        pass