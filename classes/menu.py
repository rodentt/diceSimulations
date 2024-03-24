from classes.simulator import Simulator 

class Menu:

    """ Idea: easy rerun"""

    """
    Simulator menu which prompts user for input on which simulators to run
    and displays output on such simulations.

    welcome(): welcomes user and gives instructions on use of program
    runSimulation(): runs simulation by prompting user for parameters 
    getSimulationParameters(): gets simulation parameters from user
    getInput(inputName, verifier): gets input, validating it using the verifier func
    """

    def __init__(self):
        self._simulator = Simulator()

    def welcome(self):
        """ Welcomes user and instructs user on program use"""
        print("Filler Instructions")
    

    def getInput(self, inputName, verifier):

        """
        Gets input from user validated using a passed function

        args:
            inputName (str): the name of the input parameter
            verifier(func): function that takes in the inputName, possible input
                            returns None if given input is invalid, else returns 
                            the given valid input

        Returns:
            any: the given user input. Type depends on what the verifier func returns
        """

        # prompts user for input until valid input is given
        validInput = False
        while not validInput:
            
            # prompts user for input and verifies that it's valid
            userInput = input(f"Please enter {inputName}: ")
            userInput = verifier(inputName, userInput)
            
            # case that verifier states input is not valid
            # prompts for input again 
            if (userInput == None):
                continue
            
            # returns verified input
            return userInput
        
    def getSimulationParameters(self):
        """ 
        Prompts user for simulation parameters and returns them 
        
        Returns:
            tuple: tuple containing number of dice faces, trials to run,
                   rolls per trial and min/max roll to use in each trial
        """

        def numericVerifier(inputName, inputToCheck):
            """
            Verifies if given input is a positive integer

            Args:
                inputName (str): The name of the input. Used to display messages about input to user
                inputToCheck (any): The input to verify

            Returns:
                int?: Returns positive int if input is verified. None if not
            """

            convertedInput = inputToCheck
            try:
                # throws an exception if the input is not an integer
                convertedInput = int(inputToCheck)

                # checks if integer input is not positive
                if (convertedInput <= 0):
                    print(f"Error: {inputName} must be positive")
                    return None
            
            except:
                print(f"Error: {inputName} must be an integer")
                return None
            
            # the given input is a positive integer
            return convertedInput
        
        def booleanVerifier(inputName, inputToCheck):
            """No need to validate input, just converts input to boolean"""
            return inputToCheck == "y"
    
        
        # gets input from user, passing along an input verifier function and input prompt name
        numFaces = self.getInput("the number of die faces", numericVerifier)
        numTrials = self.getInput("the number of trials", numericVerifier)
        rollsPerTrial = self.getInput("the die rolls to perform per trial", numericVerifier)
        isMin = self.getInput("if the min or max roll will be selected (y for min, any other input for max)", booleanVerifier)        
        
        # passes input in tuple
        return numFaces, numTrials, rollsPerTrial, isMin

    def runSimulation(self):
        """ TODO: write better documentation"""

        # gets parameters and initializes simulator
        params = self.getSimulationParameters()
        self._simulator.initFromParams(params)
        print(params)
        
        # runs simulation and displays results
        self._simulator.runSimulation()
        self._simulator.displayResult()
        
