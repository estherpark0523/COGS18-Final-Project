#The following class is taken from the CarInventory class in the A4 Artificial 
#Agents assignment.The code has been modified, however, with slightly 
#different methods and an added price value.
class CarShop():
    """
    Stores cars and its various attributes. Reader is able to sell,
    compare the years of, buy, and exchange cars.
    
    Methods
    ----------
        customer_sells
        
        compare_year
        
        customer_buys
        
        exchange
        
        repair
    """
    
    #The budget is what you, the customer, has. This budget increases 
    #when you sell a car (of your imagination and creativity) to the shop. 
    #The budget decreases when you buy a car from the shop.
    def __init__(self, budget = 100000, number_of_cars = 5, 
                 cars = [('Mercedes-Benz', 'E-Class', 2017, 52000), 
                  ('Honda', 'Civic', 2012, 17000), 
                  ('Toyota', 'Prius', 2020, 25000), 
                  ('Tesla', 'Model S', 2018, 100000),
                  ('Lightning McQueen', 'Racecar', 2006, 462000)]):
        
        self.budget = budget
        self.number_of_cars = number_of_cars
        self.cars = cars
        
    
    def customer_sells(self, manufacturer, model, year, price):
        """Adds cars and all their attributes to the car list.
        
        Parameters
        -----------
        manufacturer : string
            String to be stored in the car list
            
        model : string
            String to be stored in the car list
            
        year : integer
            Integer to be stored in the car list
            
        price : integer
            Integer to be stored in the car list
        """
        
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.price = price
        
        #The following car list has details about the car that 
        #you would like to sell to the car shop.
        car_sell = (self.manufacturer, 
                    self.model, 
                    self.year, 
                    self.price)
        self.cars.append(car_sell)
        self.number_of_cars += 1
        self.budget = self.budget + self.price
        print('budget = ', self.budget)
     
    
    def compare_year(self, direction = 'newest'):
        """Compares the years of other cars in the car list \ 
        to return the newest or oldest car.
        
        Parameters
        ------------
        direction : string
            String input that indicates whether
            to output the newest or oldest car
            
        Returns
        ------------
        output : string
            String that displays 
        """
        
        #year references the 2nd index (or 3rd item) 
        #in the list of car attributes.
        #year is the years of the cars in the car shop.
        year = 2
        self.direction = direction
        oldest = self.cars[0]
        newest = self.cars[0]
        
        #For loop that goes through every car and sees which 
        #is oldest and newest in manufactured year.
        for car in self.cars:
            if car[year] < oldest[year]:
                oldest = car
            if car[year] > newest[year]:
                newest = car   
               
        if self.direction == 'newest':
            output = newest
        elif self.direction == 'oldest':
            output = oldest
            
        return output
    
    
    def customer_buys(self, manufacturer, model, year, price):
        """Removes cars and all their attributes from the car list.
        
        Parameters
        -----------
        manufacturer : string
            String to be stored in the car list
            
        model : string
            String to be stored in the car list
            
        year : integer
            Integer to be stored in the car list
            
        price : integer
            Integer to be stored in the car list
        """
        
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.price = price
        
        #The following car list has details about the car 
        #that you would like to buy from the car shop.
        car_buy = (self.manufacturer, 
                    self.model, 
                    self.year, 
                    self.price)
        self.cars.remove(car_buy)
        self.number_of_cars -= 1
        self.budget = self.budget - self.price
        print('budget = ', self.budget)
     
        
        
    def exchange(self, in_manufacturer, in_model, in_year, in_price,
                out_manufacturer, out_model, out_year, out_price):
        """Exchanges an outside car with one that 
           is already existing in the car list.
        
        Parameters
        -----------
        in_manufacturer : string
            String to be stored in the car dictionary
            
        in_model : string
            String to be stored in the car dictionary
            
        in_year : integer
            Integer to be stored in the car dictionary
           
        in_price : integer
            Integer to be stored in the car dictionary
            
        out_manufacturer : string
            String to be taken out of the car dictionary
            
        out_model : string
            String to be taken out of the car dictionary
            
        out_year : integer
            Integer to be taken out of the car dictionary
        
        out_price : integer
            Integer to be taken out of the car dictionary
        """
        
        self.in_manufacturer = in_manufacturer
        self.in_model = in_model
        self.in_year = in_year
        self.in_price = in_price
        
        self.out_manufacturer = out_manufacturer
        self.out_model = out_model
        self.out_year = out_year
        self.out_price = out_price
        
        #The car dictionary has the car that 
        #you want to put into the car list.
        car_in = (self.in_manufacturer, 
                    self.in_model, 
                    self.in_year, 
                    self.in_price)
        self.cars.append(car_in)
        self.number_of_cars += 1
        self.budget = self.budget + self.in_price
        
        #The car exchange has the car that you want 
        #to take out of the car list.
        car_exchange = (self.out_manufacturer, 
                    self.out_model, 
                    self.out_year, 
                    self.out_price)
        self.cars.remove(car_exchange)
        self.number_of_cars -= 1
        self.budget = self.budget - self.out_price
        
        print('budget = ', self.budget)
        
        
    def repair(self, price):
        """Given only the price of a car, the function will 
           take from the budget as cost of repair.
        
        Parameters
        -----------
        price : integer
            Integer to be compared to the rates of repair cost.
            
        Returns
        -----------
        repair_cost : integer
            Integer that will be taken from the budget.
        """
        self.price = price
            
        #If the price of the car you want to fix is too high, the price
        #of repair will also increase
        if self.price < 25000:
                repair_cost = 150
                
        if self.price >= 25000:
                repair_cost = 250
                
        if self.price > 50000:
                repair_cost = 400
                
        return repair_cost
            
        self.budget = self.budget - repair_cost
        print('budget = ', self.budget)
                
        
        