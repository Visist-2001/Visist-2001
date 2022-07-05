# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from unittest import main


sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)


# Run unit tests automatically
main(module='test_module', exit=False)
