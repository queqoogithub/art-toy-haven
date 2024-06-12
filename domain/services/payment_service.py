from domain.ports.payment_port import PaymentPort
from typing import Any, Dict

class PaymentService:
    def __init__(self, payment_port: PaymentPort):
        self.payment_port = payment_port

    def create_customer(self, email: str, source: str) -> Dict[str, Any]:
        return self.payment_port.create_customer(email, source)

    def create_charge(self, amount: int, currency: str, customer_id: str, description: str) -> Dict[str, Any]:
        return self.payment_port.create_charge(amount, currency, customer_id, description)
    
    def check_payment(self, charge_id: str) -> Dict[str, Any]:
        return self.payment_port.check_payment(charge_id)