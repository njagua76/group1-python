def speed_checker(car_speed):
    speed_limit = 70
    
    if car_speed < speed_limit:
        print("Ok")
    else:
        excess_speed = car_speed - speed_limit
        points = excess_speed // 5
        
        if points > 12:
            print("License suspended")
        else:
            print("Points: " + str(points))

car_speed = int(input("Car speed is: "))
speed_checker(car_speed)