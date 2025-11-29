from PIL import Image, ImageDraw, ImageFont
from ccard_gen import card_number, c_expiry, c_cvv

def create_card_image(card_number, c_expiry, c_cvv):
    # Loads the card template in jpg format
    img = Image.open("CCard.jpg")

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("Orbitron-Bold.ttf", 14)

    draw.text((60, 262), f"CCARD: {card_number}", (0,0,0), font=font)
    draw.text((60, 320), "NAME:",(190,57,38), font=font)
    draw.text((60, 340), "JOHN DOE", (190,57,38), font=font)
    draw.text((275, 320), "EXPIRY DATE:",(190,57,38), font=font)
    draw.text((275, 340), f"{c_expiry}", (190,57,38), font=font)
    draw.text((500, 320), "CVV:", (190,57,38), font=font)
    draw.text((500, 340), f"{c_cvv}", (190,57,38), font=font)

    img.save("generated_card.jpg")

create_card_image(card_number, c_expiry, c_cvv)