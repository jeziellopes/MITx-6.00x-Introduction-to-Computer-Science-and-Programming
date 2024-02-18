# 6.00x Problem Set 7: Simulating robots

import math
import random

import ps7_visualize
import pylab

# For Python 2.7:
from ps7_verify_movement27 import testRobotMovement

# If you get a "Bad magic number" ImportError, comment out what's above and
# uncomment this line (for Python 2.6):
#from ps7_verify_movement26 import testRobotMovement


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = {}

        for i in range(0,self.width+1):
            for j in range(0,self.height+1):
                self.tiles[i,j] = 'dirty'

    def cleanTileAtPosition(self, pos):
        self.tiles[math.floor(pos.getX()), math.floor(pos.getY())] = 'clear'

    def isTileCleaned(self, m, n):
        if self.tiles[math.floor(m),math.floor(n)] == 'clear':
            return True
        return False
    
    def getNumTiles(self):
        return self.width * self.height

    def getNumCleanedTiles(self):
        numCleans = 0
        for i in self.tiles.values():
            if i == 'clear':
                numCleans += 1
        return numCleans

    def getRandomPosition(self):
        return Position(random.randrange(0,self.width), random.randrange(0,self.height))

    def isPositionInRoom(self, pos):
        if math.floor(pos.getX()) in range(self.width) and math.floor(pos.getY()) in range(self.height):
            return True
        return False


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        self.room = room
        self.speed = speed
        self.position = self.room.getRandomPosition()
        self.room.cleanTileAtPosition(self.position)
        self.direction = random.randrange(0, 360)

    def getRobotPosition(self):
        return self.position
    
    def getRobotDirection(self):
        return self.direction

    def setRobotPosition(self, position):
        self.position = position

    def setRobotDirection(self, direction):
        self.direction = direction

    def updatePositionAndClean(self):
        raise NotImplementedError # don't change this!


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        newPos = self.position.getNewPosition(self.direction, self.speed)
        while not self.room.isPositionInRoom(newPos):
            self.direction = random.randrange(0, 360)
            newPos = self.position.getNewPosition(self.direction, self.speed)
        self.setRobotPosition(newPos)
        self.room.cleanTileAtPosition(self.getRobotPosition())

# Uncomment this line to see your implementation of StandardRobot in action!
#testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 3
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    steps = 0.0
    for Trial in range(num_trials):
        anim = ps7_visualize.RobotVisualization(num_robots, width, height)
        room = RectangularRoom(width, height)
        robots = []
        for i in range(num_robots):
            robots.append(robot_type(room, speed))
        while room.getNumCleanedTiles() < room.getNumTiles() * min_coverage:
            for i in range(num_robots):
                robots[i].updatePositionAndClean()
                steps += 1
            anim.update(room, robots)
    anim.done()
    return steps/num_trials/num_robots

# === Problem 4
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        self.direction = random.randrange(0, 360)
        newPos = self.position.getNewPosition(self.direction, self.speed)
        while not self.room.isPositionInRoom(newPos):
            self.direction = random.randrange(0, 360)
            newPos = self.position.getNewPosition(self.direction, self.speed)
        self.setRobotPosition(newPos)
        self.room.cleanTileAtPosition(self.getRobotPosition())

#testRobotMovement(RandomWalkRobot, RectangularRoom)
        
avg = runSimulation(100, 1.0, 20, 20, 1.0, 1, StandardRobot)
print (avg)

def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print ("Plotting", num_robots, "robots...")
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300/width
        print ("Plotting cleaning time for a room of width:", width, "by height:", height)
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
    

# === Problem 5
#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#

#showPlot1('Time It Takes 1 - 10 Robots To Clean 80% Of A Room', 'Number of Robots', 'Time-steps')

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#

#showPlot2('Time It Takes A Robot To Clean 80% Of Variously Shaped Rooms', 'Aspect Ratio', 'Time-steps')
