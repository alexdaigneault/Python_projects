###Turn up the Temperature###
#Function to convert Fahrenheit into Celsius
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp
  
f100_in_celsius = f_to_c(100)
print("A temperature of 100 Fahrenheit is equal to %d Celsius." % f100_in_celsius)

#Function to convert Celsius into Fahrenheit
def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    return f_temp
  
c0_in_fahrenheit = c_to_f(0)
print("A temperature of 0 Celcius is equal to %d Fahrenheit." % c0_in_fahrenheit)

###Uses the Force###
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

#Function to get the force from mass and acceleration
def get_force(mass, acceleration):
    return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")
print("The force from a train with a mass of %d and an acceleration of %d is %d" % (train_mass, train_acceleration, train_force))

#Function that convert mass into energy in Joules
def get_energy(mass, c=3*10*8):
    return mass * c ** 2
  
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies %d Joules" % bomb_energy)

#Function to define work from mass, acceleration and distance
def get_work(mass, acceleration, distance):
    work = get_force(mass, acceleration) * distance
    return work

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does %d Joules of work over %d meters." % (train_work, train_distance))