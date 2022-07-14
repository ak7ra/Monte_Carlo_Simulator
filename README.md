This is the final project for University of Virginia School of Data Science's course DS5100.

# Monte_Carlo_Simulator

`Monte_Carlo_Simulator` is a python package containing three classes: Die, Game, and Analyzer. <br />
These three classes serve to mimic the Monte Carlo methods. <br />
Monte Carlo methods are family of techniques first developed by physicists in the 1940s to predict the outcomes of complex stochastic processes, such as nuclear fission and fusion. The behavior of random variables are modeled by chance mechanisms such as dice and computers, using random number generators. The data generated by these mechanisms through sampling are employed to influence the direction of a process.

## Metadata
Name: Ami Kano <br />
GitHub Username: ak7ra <br />
Project Name : Monte Carlo Simulator

## API description
### Classes:
#### Die class
The Die object takes in an array or list of values and creates a die. <br />
Each value in the input array/list becomes a face of the created die. <br />
<br />
Attributes: <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None <br />
<br />
Methods: <br />
* `__init__(self, faces)`
    * The initializer function creates the Die object.
    * Parameter(s):
        * `faces` : numpy array or list <br />
          faces is an numpy array or list of type str or int. It can be of any length.
* `change_weight(self, face, new_weight)`
    * The change_weight function changes the weight of a single face on the die.
    * Parameter(s):
        * `face` : str or int <br />
          face of which the weight will be changed
        * `new_weight` : float <br />
          the resulting weight of the face
    * Raises:
        * `ValueError` <br />
          if new_weight is not a float or convertible to float, change_weight will throw this error. <br />
          if face is not on the die, change_weight will throw this error. <br />
    * Returns:
        * None
* `roll(self, roll_num=1)`
    * A method to roll the die one or more times.
    * Parameter(s):
        * `roll_num` : int <br />
          int type parameter of how many times the die is to be rolled; defaults to 1.
    * Returns:
        * `result` : list <br />
          list of outcomes of the rolls.
* `show_faces_weights(self)`
    * A method to show the dataframe consisting of faces and weights of the die.
    * Parameter(s):
        * None
    * Returns:
        * the pandas dataframe consisting of faces and weights of the die
#### Game class
The Game object takes in a list of die to make a game. <br />
A game consists of rolling of one or more dice of the same kind one or more times. <br />
 <br />
Attributes: <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None <br />
<br />
Methods: <br />
* `__init__(self, list_of_die)`
    * The initializer function creates the Game object.
    * Parameter(s):
        * `list_of_die` : list <br />
          list_of_die is a list containing objects of the Die type. It can be of any length.
* `play(self, rolls)`
    * A method to play the game; roll each die for a certain amount of time.
    * Parameter(s):
        *  `rolls` : int <br />
           int type parameter of how many times each die is to be rolled.
    * Returns:
        * None 
* `show_result(self, form="wide")`
    * A method to return the dataframe including the most recent result from the play method.
    * Parameter(s):
        * `form` : string <br />
          String parameter to determine the format of the returned dataframe. Takes either "narrow" or "wide". <br />
          Defaults to "wide" 
    * Raises:
        * `ValueError` <br />
          if the value of the variable form is not "narrow" or "wide", show_result will throw this error.
    * Returns:
        * Pandas dataframe including the most recent result from the play method. <br />
          Shows the roll number, the die number and the face rolled for each roll.

#### Analyzer class
The Analyzer object takes in a game object and analyzes its results. <br />
 <br />
Attributes: <br />
* `jackpot_count` : int <br />
  jackpot_count is an int type attribute that contains the amount of jackpots in the results of the game. <br />
  Defaults to 0. Updated to correct amount when jackpot() is called.
* `jackpot_dataframe` : pandas dataframe <br />
  jackpot_dataframe is a pandas dataframe that contains the rows in which there are jackpots. <br />
  Defaults to an empty dataframe. Updated to correct data when jackpot() is called.
* `combo_frame` : pandas dataframe <br />
  combo_frame is a pandas dataframe that contains all combinations of the rolled face value, along with their occurrence. <br />
  Defaults to an empty dataframe. Updated to correct data when combo() is called.
* `face_count` : pandas dataframe <br />
  face_count is a pandas dataframe that counts the occurrence of each face value in each roll. <br />
  Defaults to an empty dataframe. Updated to correct data when face_counts() is called.
* `die_type` : string <br />
  die_type is a string type attribute. It stores the string specifying the type of face values of the dice.
<br />
Methods: <br />
* `__init__(self, game)`
    * The initializer function creates the Analyzer object.
    * Parameter(s):
        * `game` : Game <br />
          game is a Game object that is to be analyzed. 
* `jackpot(self)`
    * A method to count the occurrence of jackpots in the game.
    * Parameter(s):
        * None
    * Returns:
        * Pandas dataframe including the rows in which there were jackpots. <br />
          Shows the roll number, the die number and the face rolled for each roll.
* `combo(self, permutation=False)`
    * A method to return the dataframe that contains all combinations of the rolled face value, along with their occurrence.
    * Parameter(s):
        * `permutation` : Boolean <br />
          Boolean parameter to determine whether the function would count permutations instead of combinations. <br />
          Defaults to False.
    * Returns:
        * Pandas dataframe including all combinations or permutations from a game. <br />
          The face values are turned into multi-indexes. The column shows the occurrences of each combination/permutation. 
* `face_counts(self)`
    * A method to return the dataframe that counts the occurrence of each face value in each roll.
    * Parameter(s):
        * None
    * Returns:
        * Pandas dataframe including the counts of the occurrence of each face value in each roll. <br />
          The indexes indicate the roll number, and the columns indicate the face values of the dice.

## Synopsis
Show demo code of how the classes are used, i.e.
installing
importing
Creating dice
Playing games
Analyzing games.


## Manifest
* __init__.py
* montecarlo.py
* montecarlo_tests.py
* montecarlo_demo.ipynb
* FinalProjectSubmission.ipynb
* FinalProjectSubmission.pdf
* setup.py
* LICENSE
* README.md




Use `pip` to install the package from PyPI:

```bash
pip install lyricsgenius
```

Or, install the latest version of the package from GitHub:

```bash
pip install git+https://github.com/johnwmillr/LyricsGenius.git
```

## Usage
Import the package and initiate Genius:

```python
import lyricsgenius
genius = lyricsgenius.Genius(token)
```
