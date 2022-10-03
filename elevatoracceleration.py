import math

# Get input of forces on the y-axis from the user in Newtons
upward_force = float(input("Enter the upward force of the elevator in Newtons: "))
downward_force = float(input("Enter the downward force of the elevator in Newtons: "))


# Determine the acceleration of the object in m/s^2
# But first determine the direction of the acceleration

# Upward direction
if upward_force > downward_force:
    net_force = upward_force - downward_force
    total_force = upward_force + downward_force
    acceleration = net_force / (upward_force / 9.81) # The parenthesis is the conversion from Newtons to kg
    print("The acceleration of the elevator is", acceleration, "m/s^2 upward")

# Downward direction
else:
    net_force = downward_force - upward_force
    total_force = upward_force + downward_force
    acceleration = net_force / (downward_force / 9.81) # The parenthesis is the conversion from Newtons to kg
    print("The acceleration of the elevator is", acceleration, "m/s^2 downward")
    