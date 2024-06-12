import stripe
from domain.ports.payment_port import PaymentPort
from typing import Any, Dict

class StripeAdapter(PaymentPort):
    def __init__(self, api_key: str):
        stripe.api_key = api_key

    def create_customer(self, email: str, source: str) -> Dict[str, Any]:
        customer = stripe.Customer.create(
            email=email,
            source=source
        )
        return customer
    
    def create_charge(self, amount: int, currency: str, customer_id: str, description: str) -> Dict[str, Any]:
        charge = stripe.Charge.create(
            amount=amount,
            currency=currency,
            customer=customer_id,
            description=description
        )
        return charge
    
    def check_payment(self, charge_id: str) -> Dict[str, Any]:
        charge = stripe.Charge.retrieve(charge_id)
        return charge