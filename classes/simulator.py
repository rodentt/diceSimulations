from abc import ABC, abstractmethod

class Simulator(ABC):

    """
    Simulator which allows user to simulate probabilistic experiments
    and compare the resulting and expected probability distributions.

    initFromParams(params): Uses given parameters to initialize simulator 
    runExpectation(): Generates expected probability distribution
    runSimulation(): Runs the simulation using the given simulator parameters
    displayResult(): Displays resulting expectation and simulated probability distributions
    """

    def __init__(self):

        # default parameter values
        self._numTrials = 100
        # no other inherent parameters, should be added by inherited classes

        # these attributes are populated when the simulation is run
        self._results = [0]  # probability distribution experimentally created
        self._resultMeasures = [0, 0, 0] # expectation, variance, std. dev.

        # run expectation populates these attributes
        self._expected = [0] # probability distribution expected
        self._expectedMeasures = [0, 0, 0] # expectation, variance, std. dev.

    @abstractmethod
    def initFromParams(self, params):
        pass
    
    @abstractmethod
    def runExpectation(self):
        pass

    @abstractmethod
    def runSimulation(self):
        pass

    @abstractmethod
    def displayResult(self):
        pass


    
    
