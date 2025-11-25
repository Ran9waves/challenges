#Runs the pip library to generate a credit card number that pass Luhn's algorithm
#It includes a local BIN database to retrieve card details like brand, type, country and bank issuer
#All lookups are performed locally
#This tool was created for educational purposes only

from card_generator import CardGenerator, CardValidator

# Initializes the card generator for Visa cards
visacard_generator = CardGenerator('visa')

# Generates a standard card
card = visacard_generator.generate(count=1)
print(card)

card_number = card[0]['card']
c_expiry = card[0]['expiry_date']
c_cvv = card[0]['cvv']

validator = CardValidator(card_number)
print(f"Is Luhn valid? {validator.is_luhn_valid()}")

# Gets all available BIN Info
info = validator.get_bin_info()
print("BIN info:")
print(info)

