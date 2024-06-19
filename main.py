from domain.ports.shipment_port import ShipmentPort
from adapters.mock_shipment_adapter import MockShipmentAdapter
from domain.services.shipment_service import ShipmentService

def main():
    # Initialize the MockShipmentAdapter
    shipment_adapter = MockShipmentAdapter()
    
    # Initialize the ShipmentService with the adapter
    shipment_service = ShipmentService(shipment_adapter)
    
    # Example usage of ShipmentService methods
    order_id = "12345"
    recipient_name = "John Doe"
    recipient_address = "123 Main St, Springfield"
    
    # Create a shipment
    shipment = shipment_service.create_shipment(order_id, recipient_name, recipient_address)
    print("Created shipment:", shipment)
    print("-----------------------")
    
    # Get shipment status
    shipment_status = shipment_service.get_shipment_status(shipment["order_id"])
    print("Shipment status:", shipment_status)
    print("-----------------------")
    
    # Cancel shipment
    cancel_response = shipment_service.cancel_shipment(shipment["order_id"])
    print("Cancelled shipment:", cancel_response)
    print("-----------------------")
    
    # Track shipment
    tracking = shipment_service.tracking_shipment(shipment["tracking_number"])
    print("Tracking shipment:", tracking)

if __name__ == "__main__":
    main()
















"""
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
"""