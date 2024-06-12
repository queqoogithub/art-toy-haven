from domain.services.payment_service import PaymentService
from adapters.stripe_adapter import StripeAdapter
from adapters.mock_payment_adapter import MockStripeAdapter
from settings import settings


# Set your Stripe API keys
stripe_api_key = settings.stripe_api_key

# Create an instance of the Stripe adapter ⭐️
stripe_adapter = StripeAdapter(stripe_api_key)

# Create an instance of the Mock Stripe adapter ⭐️
# stripe_adapter = MockStripeAdapter(stripe_api_key)

# Create an instance of the payment service
payment_service = PaymentService(stripe_adapter)

# Create a customer : with tok_visa (test token for visa card)
customer = payment_service.create_customer(email="customer@example.com", source="tok_visa")

# Create a charge : amount in Cent
charge = payment_service.create_charge(amount=2000, currency="usd", customer_id=customer["id"], description="Example charge")

# Check the payment status
# payment_status = payment_service.check_payment(charge["id"])

# Display the charge details
print(f"Customer: {customer}")
print("--------------------")
print(f"Charge: {charge} \n")
print(f"Charge successful! Status: {charge['status']}, Amount: {charge['amount'] / 100:.2f} {charge['currency']}")

