from tabulate import tabulate
from classes.simulator import Simulator
from classes.helper import Helper
from abc import ABC

class diceSimulator(Simulator, ABC):

    """
    Simulator which allows user to simulate probabilistic experiments
    involving dice and compare the resulting and expected probability 
    distributions.

    initFromParams(params): Uses given parameters to initialize simulator 
    runExpectation(): Generates expected probability distribution
    runSimulation(): Runs the simulation using the given simulator parameters
    displayResult(): Displays resulting expectation and simulated probability distributions
    """

    def __init__(self):
        super().__init__()

        # default dice parameter values
        self._numFaces = 6
        self._rollsPerTrial = 1

        # these attributes are populated when the simulation is run
        self._results = [0] * 6
        self._resultMeasures = [0, 0, 0]

        # run expectation populates these attributes
        self._expected = [0] * 6
        self._expectedMeasures = [0, 0, 0]

    def initFromParams(self, params):

        # from parameters, we populate these attributes
        numFaces, numTrials, rollsPerTrial = params
        self._numFaces = numFaces
        self._numTrials = numTrials
        self._rollsPerTrial = rollsPerTrial

        # these attributes are populated when the simulation is run
        self._results = [0] * numFaces
        self._resultMeasures = [0, 0, 0]

        # run expectation populates these attributes
        self._expected = [0] * numFaces
        self._expectedMeasures = [0, 0, 0]

    def displayResult(self):

        # creates table of distributions
        displayTable = [0] * self._numFaces
        for i in range(1, self._numFaces + 1):
            expected = self._expected[i - 1]
            result = self._results[i - 1]
            displayTable[i - 1] = [i, expected, result, abs(expected - result)]
        
        # creates table of distribution measuremnts
        measurementTable = [["Expected"] + self._expectedMeasures, 
                            ["Results"] + self._resultMeasures, 
                            ["Abs Diff."] + Helper.subtractArr(self._expectedMeasures, self._resultMeasures, self._numFaces)]

        # displays distribution tables
        print("")
        print("Expected and Experimental Distributions\n")
        print(tabulate(displayTable, headers=["Value", "Expected", "Result", "Abs Diff."], floatfmt=".5f"))
        print("")
        print("Expected and Experimental Distribution Measurements\n")
        print(tabulate(measurementTable, headers=["", "Mean", "Variance", "Std. Dev."]))