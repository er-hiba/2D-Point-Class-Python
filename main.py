# Import the 'Point' class from the 'Point' file
from Point import Point

# Create 3 points using the default constructor (default x and y coordinates are 0)
point1 = Point()
point2 = Point()
point3 = Point()

# Change the attributes of points 2 and 3
point2.set_x_coordinate(4)
point2.set_y_coordinate(3)

point3.set_x_coordinate(2)
point3.set_y_coordinate(-1)

# Display

print("- Point 1:")
print("X Coordinate:", point1.get_x_coordinate())
print("Y Coordinate:", point1.get_y_coordinate())

print("\n- Point 2:")
print("X Coordinate:", point2.get_x_coordinate())
print("Y Coordinate:", point2.get_y_coordinate())

print("\n- Point 3:")
print("X Coordinate:", point3.get_x_coordinate())
print("Y Coordinate:", point3.get_y_coordinate())

# Call the Distance method which returns the distance between the current point
# and the point passed as a parameter

print("\n- The distance between point 2 and point 3:", point3.distance(point2))

# Call the Norm method which returns the distance between the current point (point 2)
# and the origin of the coordinate system
print("\n- The distance between point 2 and the origin of the coordinate system:", point2.norm())
