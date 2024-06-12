import stripe

# Set your Stripe API keys
stripe.api_key = "sk_test_51JUKq6BW2kmnQhJc4b18XVVzrXjrEkiCaZvNsqW2zTnOHvGwdKWlUEzgMPY0bD3LaOnoaHPSQ9AB98xCK1POZaA600qVuydwi0"

# Create a customer
customer = stripe.Customer.create(
    email="customer@example.com",
    source="tok_visa"  # Obtained from Stripe.js on the client-side
)

# Create a charge
charge = stripe.Charge.create(
    amount=2000,  # Amount in cents
    currency="usd",
    customer=customer.id,
    description="Example charge"
)

# Display the charge details
print(f"Charge successful! Status: {charge.status}, Amount: {charge.amount / 100:.2f} {charge.currency}")