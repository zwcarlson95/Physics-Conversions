train_mass = input("Enter the mass of the train (Kg): ")
train_acceleration = input("Enter the acceleration of the train (Km): ")
train_distance = input("Enter the distance traveled (Km): ")
bomb_mass = input("Enter the mass of the bomb (Kg): ")



def get_force(mass, acceleration):
  return mass * acceleration
train_force = get_force(int(train_mass), int(train_acceleration))
print("The train supplies " + str(train_force) + " Newtons of force.")
c = 3 * 10 ** 8
def get_energy(mass, c):
  return mass * c ** 2

bomb_energy = get_energy(int(bomb_mass), c)
print("A " + str(bomb_mass) + "kg bomb supplies " + str(bomb_energy) + " Joules")

def get_work(mass, acceleration, distance):
  return mass * acceleration * distance

train_work = get_work(int(train_mass), int(train_acceleration), int(train_distance))
print("The train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters." )
