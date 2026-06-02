distance_mi = 1
is_raining = True
has_bike = True
has_car = False
has_ride_share_app = True

if(distance_mi <= 0):
    print("False")

elif(distance_mi <= 1 and is_raining == False):
    print("True")

elif(distance_mi <= 1 and is_raining == True):
    print("False")

elif(distance_mi > 1 and distance_mi <= 6 and is_raining == True and has_bike == False):
    print("False")

elif(distance_mi > 1 and distance_mi <= 6 and is_raining == False and has_bike == False):
    print("False")

elif(distance_mi > 1 and distance_mi <= 6 and is_raining == False and has_bike == True):
    print("True")

elif(distance_mi > 6 and has_ride_share_app == True):
    print("True")

elif(distance_mi > 6 and has_car == True):
    print("True")

elif(distance_mi > 6 and has_car == False and has_ride_share_app == False):
    print("False")