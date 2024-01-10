
from restaurant import Base, engine, session, Customer, Restaurant, Review


customer1 = Customer(first_name='Pete', last_name='Anders')
customer2 = Customer(first_name='patrick', last_name='flander')
customer3=Customer(first_name='jack',last_name='dan')
#feel free to add more instances
restaurant1 = Restaurant(name='mc fryz', price=5)
restaurant2 = Restaurant(name='indominoes', price=2)
restaurant3= Restaurant(name='eka',price=1)

review1 = Review(customer=customer1, restaurant=restaurant1, star_rating=4)
review2 = Review(customer=customer2, restaurant=restaurant1, star_rating=5)
review3= Review(customer=customer3,restaurant=restaurant3,star_rating=3)

session.add_all([customer1, customer2,customer3, restaurant1, restaurant2,restaurant3, review1, review2,review3])
session.commit()

print (customer3.full_name())#prints customers full names 
print(customer3.favorite_restaurant().name)#print customers favorite 
# print(customer1.full_name()) 
# print(customer2.favorite_restaurant().name)  
# customer1.add_review(restaurant2, 3)
# customer1.delete_reviews(restaurant1)
# print(review1.full_review()) 
# print(Restaurant.fanciest().name)  
# print('\n'.join(restaurant1.all_reviews()))