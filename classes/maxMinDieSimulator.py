import random 
from tabulate import tabulate
from classes.helper import Helper
import math
from classes.diceSimulator import diceSimulator
from overrides import overrides

class maxMinDieSimulator(diceSimulator):

    """
    Simulator menu which prompts user for input on which simulators to run
    and displays output on such simulations.

    initFromParams(params): Uses given parameters to initialize simulator 
    runExpectation(): Generates expected probability distribution
    runSimulation(): Runs the simulation using the given simulator parameters
    displayResult(): Displays resulting expectation and simulated probability distributions
    """

    def __init__(self):

        # calls dice simulator constructor 
        # has additional min/max attribute
        super().__init__()
        self._isMin = False

        self.runExpectation()

    def initFromParams(self, params):

        # from parameters, we populate these attributes
        numFaces, numTrials, rollsPerTrial, isMin = params
        self._numFaces = numFaces
        self._numTrials = numTrials
        self._rollsPerTrial = rollsPerTrial
        self._isMin = isMin

        # these attributes are populated when the simulation is run
        self._results = [0] * numFaces
        self._resultMeasures = [0, 0, 0]

        # run expectation populates these attributes
        self._expected = [0] * numFaces
        self._expectedMeasures = [0, 0, 0]
        self.runExpectation()
    
    def runExpectation(self):

        """
        Generates the expected probability distribution given 
        the simulator parameters.
        """

        # these are the relevant values to 
        # calculate the probability distribution
        d = self._rollsPerTrial
        n = self._numFaces
        normalizer = pow(n, d)

        # iterates over every possible outcome value
        # and calculates their associated probability
        index = 0
        first = True
        lastPow = 0
        for x in range(1, self._numFaces + 1):
            
            # the formula is based on powers of the outcome values
            # we only calculate each power only once
            if (first):
                lastPow = pow(x - 1, d) 
                first = False
            currPow = pow(x, d)

            # probability distribution formula: P(X = x) = [x^d - (x - 1)^d] / n^d
            self._expected[index] = abs((currPow - lastPow) / normalizer)
            
            # updates the last power calculated and the index
            lastPow = currPow
            index = index + 1
        
        # if we select the minimum die roll, the probability distribution
        # is the same as if we were selecting the max roll, except reversed
        if (self._isMin):
            self._expected.reverse()

        # calculates the mean and variance using the generated probability distribution
        mean = Helper.calculateDieMean(self._expected, self._numFaces)
        variance = Helper.calculateDieVar(self._expected, self._numFaces, mean)
        self._expectedMeasures = [mean, variance, math.sqrt(variance)]

    def runSimulation(self):
        
        """ Runs the simulation using the stored simulator parameters"""

        # performs the specified number of trials
        for i in range(1, self._numTrials + 1):
            
            # performs the specified number of rolls per the trial
            # either selects the highest or lowest rolls, kept track in trial draw
            trialDraw = None
            for i in range(1, self._rollsPerTrial + 1):
                currDraw = random.randint(1, self._numFaces)

                if (trialDraw == None):
                    trialDraw = currDraw
                elif (self._isMin and currDraw < trialDraw):
                    trialDraw = currDraw
                elif(not self._isMin and currDraw > trialDraw):
                    trialDraw = currDraw
            
            # updates the simulation results by keeping track of 
            # the number of times a certain result was drawn
            index = trialDraw - 1
            self._results[index] = self._results[index] + 1
        
        # normalizes the results by dividing using the number of trials performed
        for i in range(0, self._numFaces):
            self._results[i] = self._results[i] / self._numTrials
        
        # gets the distribution measurements
        mean = Helper.calculateDieMean(self._results, self._numFaces)
        variance = Helper.calculateDieVar(self._results, self._numFaces, mean)
        self._resultMeasures = [mean, variance, math.sqrt(variance)]