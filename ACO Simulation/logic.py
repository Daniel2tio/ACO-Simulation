from math import atan2, sin, cos, sqrt, pi, pow
from random import uniform

"""
The Vector class created is used to implement the movement
and pheromone update rules for our ACO algorithm
"""

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __add__(a, b):
        if type(b) == Vector:
            return Vector(a.x + b.x, a.y + b.y)
        else:
            return Vector(a.x + b, a.y + b)
        
    def __sub__(a, b):
        if type(b) == Vector:
            return Vector(a.x - b.x, a.y - b.y)
        else:
            return Vector(a.x - b, a.y - b)
        
    def __mul__(a, b):
        if type(b) == Vector:
            return Vector(a.x * b.x, a.y * b.y)
        else:
            return Vector(a.x * b, a.y * b)
        
    def __truediv__(a, b):
        if type(b) == Vector:
            return Vector(a.x / b.x, a.y / b.y)
        else:
            return Vector(a.x / b, a.y / b)

    #we generate a random vector with x and y values within a certain range.
    def Random(value=1):
        return Vector(uniform(-value, value), uniform(-value, value))

    #we rotate the vector by a given angle in radians, and convert the result to a tuple of (x, y) coordinates.
    def Rotate(self, angle, convertToTuple=False):
        x = self.x * cos(angle) - self.y * sin(angle)
        y = self.x * sin(angle) + self.y * cos(angle)
        if convertToTuple:
            return (x, y)
        return Vector(x, y)
    
    #returns the length of the vector
    def Magnitude(self):
        return sqrt(self.x * self.x + self.y * self.y)
    
    #returns a normalised vector from the Magnitude method
    def Normalize(self):
        magnitude = self.Magnitude()
        if magnitude > 0:
            return Vector(self.x / magnitude, self.y / magnitude)
        
    #returns the angle in radians between the x-axis and the vector
    def Heading(self, toDegree=False):
        theta = atan2(self.y, self.x)
        if toDegree:
            return theta * (180/pi)
        return theta
    
    #We set the angle of the vector to a given value while keeping its magnitude constant.
    def SetAngle(self, angle):
        mag = self.Magnitude()
        return Vector(cos(angle) * mag, sin(angle) * mag )

    #We calculate the distance (and distance squared) between the two vectors.
    def GetDistance(a, b):
        return sqrt( pow(b.x - a.x, 2) + pow(b.y - a.y, 2) )
    def GetDistanceSQ(a, b):
        return pow(b.x - a.x, 2) + pow(b.y - a.y, 2)

    #We then check if two ants are within a given distance of each other.
    def WithinRange(a, b, dist):
        if abs(a.x - b.x) > dist:
            return False
        if abs(a.y - b.y) > dist:
            return False
        squared_dist = dist * dist
        return  True if Vector.GetDistanceSQ(a, b) <= squared_dist else False

    #We scale the vector
    def Scale(self, l):
        mag = self.Magnitude()
        if mag == 0:
            return Vector()
        else:
            scaler = l/mag
            return Vector(self.x * scaler, self.y * scaler)
        scaler = 0 if mag == 0 else l/mag
        return self * scaler
    
    #We calculate the average of a list of vectors
    def Average(vecs):
        if len(vecs) == 0:
            return Vector()
        avg = Vector(vecs[0].x, vecs[0].y)
        for i in range(1, len(vecs)):
            avg = avg + vecs[i]

        avg = avg / len(vecs)
        return avg
    
    def Negative(self):
        return Vector(self.x * -1, self.y * -1)
    
    def Copy(self):
        return Vector(self.x, self.y)
    
    #We return the tuple of x and y as integers
    def xy(self):
        return ( int(self.x), int(self.y) )
    
    def zero(self):
        return Vector(0, 0)
    
    #String representation of the vector
    def __repr__(self):
        return f" ({self.x}, {self.y})"
