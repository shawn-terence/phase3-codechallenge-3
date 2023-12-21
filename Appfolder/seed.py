from restaurant import Base, engine, session, Customer, Restaurant, Review

customer1 = Customer(first_name='Giovanni', last_name='medici')
customer2 = Customer(first_name='Donnatella', last_name='Gusta')
restaurant1 = Restaurant(name='Fine Dining', price=5)
restaurant2 = Restaurant(name='Fast Food', price=2)

review1 = Review(customer=customer1, restaurant=restaurant1, star_rating=4)
review2 = Review(customer=customer2, restaurant=restaurant1, star_rating=5)