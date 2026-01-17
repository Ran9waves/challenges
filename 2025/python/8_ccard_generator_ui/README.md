#The FAKE CCARD GENERATOR

**DISCLAIMER:**  
This project is for educational and testing purposes only.  
It does NOT generate real credit card data and must NOT be used for fraud, illegal activity, or any real-world financial transactions.  
The author is not responsible for any misuse of this code.

This project uses open-source libraries (`pillow` and `card-generator`) and generates fake credit card numbers for educational and testing purposes only.

My aim was to better understand how Luhn's algorithm works and to combine my UI skills (the ccard template was designed by me after seeing the release of one of my favorite movies: TRON) with my code skills.



#HOW IT WORKS?
Inside this project there are 2 code files:

1) ccard_gen.py : generates the fake information of the credit card (BIN info) and also runs a Luhn algorithm test to validate if the credit card data generated is valid. All the information generated is totally fake and as mentioned previously it was created for educational purposes.

2) ccard_gen_template.py: retrieves the ccard number, cvv and the expiration date fake data generated through ccard_gen.py and adds it on the ccard jpeg template, which shows a nice visa elec-"TRON" design. 
The outcome of running this module is generated_card.jpeg

