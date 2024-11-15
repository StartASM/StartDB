from ignition.parser import Parser
from ignition.runtime import Runtime
from ignition.ast import AbstractSyntaxTree

class Interpreter:
    _instance = None  #Singleton

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Interpreter, cls).__new__(cls)
        return cls._instance

    def __init__(self, compiler_image):
        if not hasattr(self, "_initialized"):
            #Core components (all singletons)
            self.ast = None  #Abstract Syntax Tree
            self.parser = Parser()  #Parser
            self.runtime = None  #Runtime environment
            self.error_string = ""  #Error messages
            self.compiler_image = compiler_image
            self._initialized = True

    # PUBLIC METHODS

    def initialize(self, program):
        #Create a new blank runtime
        self.runtime = Runtime()
        #Call the parser to parse the given program at the local path
        self.ast = self.parser.parse_program(program, self.compiler_image)
        if self.ast is None:
            return False
        return True

    def forward(self):
        print("Stepping forward")

    def finish(self):
        print("Moving to EOF")

    def dump(self):
        print("Dumping state")

    def terminate(self):
        #Clear the runtime and AST
        self.runtime = None
        self.ast = None

    # PRIVATE METHODS
