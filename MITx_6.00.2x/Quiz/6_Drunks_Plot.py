import random, math
import matplotlib.pyplot as plt

"""
    Suppose we use a simulation to simulate a random walk of a class of drunk, returning a collection of actual distances from the origin for a set of trials.

    Each graph below was generated by using one of the above five classes of a drunk (UsualDrunk, ColdDrunk, EDrunk, PhotoDrunk, or DDrunk). For each graph, indicate which Drunk class is mostly likely to have resulted in that distribution of distances. Click on each image to see a larger view.

    File will generate plots for each drunk type.
    (1000 tryours of 1000 steps for each drunk)

    Alcohol is bad, m'key?
    https://cdn.meme.am/instances/250x250/23187447.jpg

"""


class Drunk(object):
    def __init__(self):
        self.positions = [];
        self.position_x = 0.0;
        self.position_y = 0.0;
        pass

    def reset(self):
        self.position_x = 0
        self.position_y = 0
        return self;



    def move(self):
        pos = self.takeStep()
        self.position_x += pos[0]
        self.position_y += pos[1]
        # self.positions.append( ( self.position_x, self.position_y ) )
        return self;

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,0.9), (0.0,-1.03), (1.03, 0.0), (-1.03, 0.0)]
        return random.choice(stepChoices)

class EDrunk(Drunk):
    def takeStep(self):
        ang = 2 * math.pi * random.random()
        length = 0.5 + 0.5 * random.random()
        return (length * math.sin(ang), length * math.cos(ang))

class PhotoDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.0, 0.5),(0.0, -0.5),
                     (1.5, 0.0),(-1.5, 0.0)]
        return random.choice(stepChoices)

class DDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.85, 0.85), (-0.85, -0.85),
                     (-0.56, 0.56), (0.56, -0.56)]
        return random.choice(stepChoices)



if __name__ == '__main__':

    myDrunkWalks = {
        'usualDrunk' : UsualDrunk(),
        'coldDrunk' : ColdDrunk(),
        'eDrunk' : EDrunk(),
        'photoDrunk' : PhotoDrunk(),
        'DDrunk' : DDrunk()
    }

    n = 0;

    results = {}

    for j in range(1000):
        for typeofdrunk, drunk in myDrunkWalks.items():
            drunk.reset();

            for i in range(1000):
                drunk.move()


            r = results.get(typeofdrunk, [])
            r.append( (drunk.position_x, drunk.position_y) );
            results.update({ typeofdrunk : r });





    for k,i in myDrunkWalks.items():
        n += 1;
        plt.subplot(2,3, n);
        plt.title(k)

        x = [x[0] for x in results.get(k)],
        y = [y[1] for y in results.get(k)]
        print(x,y)

        plt.scatter( x, y );
        plt.axis('equal')
        plt.xlabel("X")
        plt.ylabel("Y")


    plt.show()
