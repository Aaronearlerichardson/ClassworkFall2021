# BMI-calculator
#### Aaron Earle-Richardson
## Installation
Clone the repository from this page

## Requirements
Python 3.7, 3.8, or 3.9 standard library, no 3rd party packages required

## Usage 

### Main Functionality
* Open a command line interface that has access to a python interpreter (e.g. git bash)
* Type ```python bme_calc.py``` and this will begin the user prompt
* Enter in your patient data as prompted. If you make a typo, it will ask again.
  * Weight can be input in pounds or kilograms (if not indicated, it will assume kilograms)
  * Height can be entered in inches or meters (if not indicated, it will assume meters)
  * Typos beyond one letter mistakes will result in an error

### Other Functionalities
  Many other useful utilities can be taken advantage of in this repository. To do so, open a python console and try some commands!
  
```
from get_inputs import edits_one
from utils import print_results, sig_fig_round, num_counter

#find all one letter typo permutations of any word
print(edits_one("word"))

#give a bmi, get the clinical categorization
print_results(24)

#similar to python's round() function, only it rounds to significant digits instead of number od decimal digits
sig_fig_round(34.2642,4)

#take any number and count the number of digits in that number (decimals and interger)
num_counter(34.2642)
```