from unittest.mock import Mock
from typing import Any, Dict

# TODO : create json file for mock data

class MockStripeAdapter:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def create_customer(self, email: str, source: str) -> Dict[str, Any]:
        self.email = email
        self.source = source
        mock_customer = {
            "address": None,
            "balance": 0,
            "created": 1718011992,
            "currency": None,
            "default_source": "card_1PQ4bEBW2kmnQhJcMyvlBMnF",
            "delinquent": False,
            "description": None,
            "discount": None,
            "email": self.email,
            "id": "cus_QGboL1AkVWMeJi",
            "invoice_prefix": "79D413D4",
            "invoice_settings": {
                "custom_fields": None,
                "default_payment_method": None,
                "footer": None,
                "rendering_options": None
            },
            "livemode": False,
            "metadata": {},
            "name": None,
            "next_invoice_sequence": 1,
            "object": "customer",
            "phone": None,
            "preferred_locales": [],
            "shipping": None,
            "tax_exempt": "none",
            "test_clock": None
        }

        return mock_customer

    def create_charge(self, amount: int, currency: str, customer_id: str, description: str) -> Dict[str, Any]:
        self.amount = amount
        self.currency = currency
        self.customer_id = customer_id
        self.description = description
        # Return a dictionary with charge data
        mock_charge = {
            "amount": self.amount,
            "amount_captured": self.amount,
            "amount_refunded": 0,
            "application": None,
            "application_fee": None,
            "application_fee_amount": None,
            "balance_transaction": "txn_mock_xxx",
            "billing_details": {
                "address": {
                    "city": None,
                    "country": None,
                    "line1": None,
                    "line2": None,
                    "postal_code": None,
                    "state": None
                },
                "email": None,
                "name": None,
                "phone": None
            },
            "calculated_statement_descriptor": "TGROUP",
            "captured": True,
            "created": 1718011993,
            "currency": self.currency,
            "customer": "cus_mock_xxx",
            "description": self.description,
            "destination": None,
            "dispute": None,
            "disputed": False,
            "failure_balance_transaction": None,
            "failure_code": None,
            "failure_message": None,
            "fraud_details": {},
            "id": "ch_mock_xxx",
            "invoice": None,
            "livemode": False,
            "metadata": {},
            "object": "charge",
            "on_behalf_of": None,
            "order": None,
            "outcome": {
                "network_status": "approved_by_network",
                "reason": None,
                "risk_level": "normal",
                "risk_score": 47,
                "seller_message": "Payment complete.",
                "type": "authorized"
            },
            "paid": True,
            "payment_intent": None,
            "payment_method": "card_mock_xxxx",
            "payment_method_details": {
                "card": {
                    "amount_authorized": 2000,
                    "brand": "mock",
                    "checks": {
                        "address_line1_check": None,
                        "address_postal_code_check": None,
                        "cvc_check": "pass"
                    },
                    "country": "US",
                    "exp_month": 6,
                    "exp_year": 2025,
                    "extended_authorization": {
                        "status": "disabled"
                    },
                    "fingerprint": "xxx",
                    "funding": "credit",
                    "incremental_authorization": {
                        "status": "unavailable"
                    },
                    "installments": None,
                    "last4": "4242",
                    "mandate": None,
                    "multicapture": {
                        "status": "unavailable"
                    },
                    "network": "mock",
                    "network_token": {
                        "used": False
                    },
                    "overcapture": {
                        "maximum_amount_capturable": self.amount,
                        "status": "unavailable"
                    },
                    "three_d_secure": None,
                    "wallet": None
                },
                "type": "card"
            },
            "receipt_email": None,
            "receipt_number": None,
            "receipt_url": "https://pay.mock.com/receipts/payment/xxxx",
            "refunded": False,
            "review": None,
            "shipping": None,
            "source": {
                "address_city": None,
                "address_country": None,
                "address_line1": None,
                "address_line1_check": None,
                "address_line2": None,
                "address_state": None,
                "address_zip": None,
                "address_zip_check": None,
                "brand": "Visa",
                "country": "US",
                "customer": "cus_mock_xxx",
                "cvc_check": "pass",
                "dynamic_last4": None,
                "exp_month": 6,
                "exp_year": 2025,
                "fingerprint": "xxx",
                "funding": "credit",
                "id": "card_xxxx",
                "last4": "1234",
                "metadata": {},
                "name": None,
                "object": "card",
                "tokenization_method": None,
                "wallet": None
            },
            "source_transfer": None,
            "statement_descriptor": None,
            "statement_descriptor_suffix": None,
            "status": "succeeded",
            "transfer_data": None,
            "transfer_group": None
        }

        return mock_charge

    def check_payment(self, charge_id: str) -> Dict[str, Any]:
        self.charge_id = charge_id
        return Mock()