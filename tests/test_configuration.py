import unittest
from unittest.mock import MagicMock
from projectse.configuration import ConfigurationBuilder

class ConfigurationBuilderTestCase(unittest.TestCase):

     def test_set_ai(self):

        cb = ConfigurationBuilder()
        cb.get_input = MagicMock(return_value=234)
        cb.print_out = MagicMock()

        cb.input_num_AIs()
        print(str(cb))
        cb.print_out.assert_not_called()

        cb.get_input.side_effect = ['yes','text',5]
        cb.input_num_AIs()
        cb.print_out.assert_called_with("\nError: Input must be an integer\n")


#TODO: Add additional test where Configuration-class is Mocked and check that AIplayers are added.

if __name__ == '__main__':
    unittest.main()
