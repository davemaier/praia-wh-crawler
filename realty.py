class Realty(object):

    __slots__ = ["title", "id", "description", "price", "post_code", "street", "city", "country", "house_number" ]

    def __init__(self, title, id, description, price, post_code, street, city, country, house_number):
        self.title = title
        self.id = id
        self.description = description
        self.price = price
        self.post_code = post_code
        self.street = street
        self.city = city
        self.country = country
        self.house_number = house_number

    def to_dict(self):
        return {
            "title": self.title, 
            "id": self.id,
            "description": self.description, 
            "price": self.price, 
            "post_code": self.post_code, 
            "street": self.street, 
            "city": self.city, 
            "country": self.country, 
            "house_number": self.house_number
        }

