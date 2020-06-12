def test():
    from car_functions import CarShop

    #tests for the object
    assert CarShop
    test_carshop = CarShop()
    assert test_carshop.number_of_cars == 5
    assert type(test_carshop.cars) == list


    #tests for the customer sells method
    test_carshop.customer_sells('Honda', 'Accord', 2019, 24000)
    assert test_carshop.number_of_cars == 6


    #tests for the compare year method
    compare_car = test_carshop.compare_year('newest')
    assert compare_car == ('Toyota', 'Prius', 2020, 25000)


    #tests for the customer buys method
    test_carshop.customer_buys('Toyota', 'Prius', 2020, 25000)
    assert test_carshop.number_of_cars == 5


    #tests for the exchange method
    test_carshop.exchange('Subaru', 'Outback', 2020, 27000, 'Honda', 'Civic', 2012, 17000)
    assert test_carshop.number_of_cars == 5


    #tests for the repair method
    repair_cost = test_carshop.repair(30000)
    assert isinstance(repair_cost, int)
    assert repair_cost == 250