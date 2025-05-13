class App:
    """This is an example of a Google Style Docstring, used to document a class.

    I'm writing this as an example for other Themis developers.

    Args:
        msg (str): Human readable string describing the exception.
        code (:obj:`int`, optional): Error code.

    Attributes:
        msg (str): Human readable string describing the exception.
        code (int): Exception error code.

    """

    def run(self):
        """Runs the app."""
        print("Welcome to Themis!")

    def add(self, a: int, b: int) -> int:
        """Adds two integers together.

        Args:
            param1: The first integer.
            param2: The second integer.

        Returns:
            The sum of the two integers.

        """
        return a + b
