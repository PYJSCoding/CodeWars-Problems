def freeway_game(dist_km_to_exit, my_speed_kph, other_cars):
    points = 0
    How_long_togo = (dist_km_to_exit/ my_speed_kph) * 60
    for car in other_cars:
        if car[0] < 0:
          OtherCar_toExit = ((dist_km_to_exit/car[1]) * 60) + car[0]
          if  How_long_togo < OtherCar_toExit:
               points = points + 1
        else:
            Other_howFar_toCatch = ((dist_km_to_exit/car[1]) * 60) + car[0]
            if Other_howFar_toCatch < How_long_togo:
                points = points - 1
            
    return points

freeway_game(50.0, 130.0, [[-1.0, 120.0], [-1.5, 120.0]])
