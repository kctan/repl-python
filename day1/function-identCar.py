
def identCar(car, color):
    print("Car %s has color %s"%(car, color))
    
identCar(color='red', car = 'honda')

'''
def identCar(car=None, color='red'):
    if car == None:
        print("You have to give me a car name")
        return 
    print("Car %s has color %s"%(car, color))

identCar(color='blue')
identCar(car='toyota')
'''
