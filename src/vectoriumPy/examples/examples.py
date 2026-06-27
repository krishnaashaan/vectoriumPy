from vectoriumPy import motion,momentum,impulse,Kinetic_energy,Potential_energy,Mechanical_energy
from vectoriumPy import ohms_law,electric_energy,mirror_formula,magnification
from vectoriumPy.Vectors import Vectors
#-------- KINEMATICS ------ #
# Example of motion function
print("Motion Example:")
solver = motion(10,None,5,1,0)
print(f'Final velocity: {solver:.2f} m/s')

#-------- FORCES ------ #
print("\nMomentum Example:")
# Example of momentum function
solver_momentum = momentum(20,5,None)
print(f'Momentum: {solver_momentum:.2f} kg*m/s')

print("\nImpulse Example:")
# Example of impulse function
solver_impulse = impulse(20,5,None)
print(f'Impulse: {solver_impulse:.2f} N*s')

#-------- ENERGY ------ #
print("\nKinetic Energy Example:")
# Example of Energy  related function
solver_kinetic = Kinetic_energy(None,50,10)
print(f'Kinetic Energy: {solver_kinetic:.2f} J')

print("\nPotential Energy Example:")
solver_potential = Potential_energy(None,50,9.8,10)
print(f'Potential Energy: {solver_potential:.2f} J')

print("\nMechanical Energy Example:")
solver_mechanical = Mechanical_energy(None,solver_kinetic,solver_potential)
print(f'Mechanical Energy: {solver_mechanical:.2f} J')

#--------ELECTRICITY ------ #
print("\nOhms law Example:")
solver_ohms = ohms_law(None,10,5)
print(f'Voltage is:{solver_ohms:.2f} V')

print("\nElectrical energy Example:")
solver_EE = electric_energy(None,100,10)
print(f"Electrical Energy is:{solver_EE} J")

#-------- OPTICS ------ #

print("\nMirror formula:")
solver_mirror = mirror_formula(None,-10,20)
print(f"Focal length is:{solver_mirror} m")

print("\n Magnification& nature")
magnification_solver = magnification(-30,60,mode="mirror")
print(f"Magnification & nature is:{magnification_solver}")

#------ VECTORS ------#
v1 = Vectors(3, 4, 0)
v2 = Vectors(1, 2, 3)

# Addition
print(v1 + v2)

# Magnitude
print(v1.magnitude())

# Dot Product
print(v1.dot(v2))

# Cross Product
print(v1.cross(v2))






