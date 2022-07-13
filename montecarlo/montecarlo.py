import numpy as np
import random
import pandas as pd

class Die:
    
    '''
    The Die object

    Parameters
    ----------
    faces : numpy array
        faces is an numpy array of type str or int. It can be of any length.

    '''
    
    def __init__(self, faces):
        faces = np.array(faces)
        self._faces_and_weights = pd.DataFrame(data = faces, columns = ["Faces"], index = range(len(faces)))
        self._faces_and_weights["Weights"] = np.array([1.0 for i in range(len(faces))])
    
    def change_weight(self, face, new_weight):
        '''
        A method to change the weight of a single side.

        Parameters
        ----------
        face : str or int
            face of which the weight will be changed
        new_weight : float
            the resulting weight of the face

        Raises
        ------
        ValueError
            if new_weight is not a float or convertible to float, change_weight will throw this error.

        Returns
        -------
        None
        '''
        if not (isinstance(new_weight, float)):
            try:
                new_weight = float(new_weight)
            except ValueError:
                print("Weight must be convertible to float")
                return
        
        if not (face in list(self._faces_and_weights['Faces'])):
            print("Face does not exist.")
            return
        else:
            self._faces_and_weights.loc[self._faces_and_weights['Faces'] == face, "Weights"] = new_weight
    
    
    def roll(self, roll_num=1):        
        '''
        A method to roll the die one or more times.

        Parameters
        ----------
        roll_num
            int type parameter of how many times the die is to be rolled; defaults to 1.

        Returns
        -------
        result
            list of outcomes of the rolls.
        '''
        result = random.choices(self._faces_and_weights["Faces"].values, weights=self._faces_and_weights["Weights"].values, k=roll_num)
        return result
    
    def show_faces_weights(self):
        '''
        A method to show the dataframe consisting of faces and weights of the die.
        
        Returns
        -------
        the dataframe consisting of faces and weights of the die
        '''
        return self._faces_and_weights
    
#-------------------------------------------------------------
    
class Game:
    
    '''
    The Game object

    Parameters
    ----------
    list_of_die : list
        list_of_die is a list containing objects of the Die type. It can be of any length.

    '''
    
    def __init__(self, list_of_die):
        self._result = pd.DataFrame()
        self._list_of_die = list_of_die
    
    def play(self, rolls):
        '''
        A method to play the game; roll each die for a certain amount of time.

        Parameters
        ----------
        rolls
            int type parameter of how many times each die is to be rolled.

        Returns
        -------
        None
        '''
        self._result = pd.DataFrame()
        for i in range(len(self._list_of_die)):
            new_res = pd.DataFrame(self._list_of_die[i].roll(rolls))
            new_res.index = [num+1 for num in range(rolls)]
            new_res.index.name = "Roll Number"
            new_res.columns = [i+1]
            new_res.columns.name = "Die Number"
            self._result = pd.concat([self._result, new_res], axis=1)

    def show_result(self, form="wide"):
        '''
        A method to return the dataframe including the most recent result from the play method.

        Parameters
        ----------
        form
            String parameter to determine the format of the returned dataframe. Takes either "narrow" or "wide". 
            Defaults to "wide"

        Raises
        ------
        ValueError
            if the value of the variable form is not "narrow" or "wide", show_result will throw this error.

        Returns
        -------
        Dataframe including the most recent result from the play method. 
        Shows the roll number, the die number and the face rolled for each roll.
        '''
        if not (form=="wide" or form=="narrow"):
            raise ValueError("Variable \"form\" must have value of \"wide\" or \"narrow\"")
            return
        elif form=="wide":
            return self._result
        elif form=="narrow":
            return self._result.stack().to_frame().rename(columns={0:"Face Rolled"})
        

#-------------------------------------------------------------
        
class Analyzer:
    
    '''
    The Analyzer object

    Parameters
    ----------
    game : Game
        game is a Game object.
        
    Attributes
    ----------
    jackpot_count : int
        jackpot_count is an int type attribute that contains the amount of jackpots in the results of the game.
        Defaults to 0. Updated to correct amount when jackpot() is called.
    jackpot_dataframe : pandas dataframe
        jackpot_dataframe is a pandas dataframe that contains the rows in which there are jackpots.
        Defaults to an empty dataframe. Updated to correct data when jackpot() is called.
    combo_frame : pandas dataframe
        combo_frame is a pandas dataframe that contains all combinations of the rolled face value, along with their occurrence.
        Defaults to an empty dataframe. Updated to correct data when combo() is called.
    face_count : pandas dataframe
        face_count is a pandas dataframe that counts the occurrence of each face value in each roll.
        Defaults to an empty dataframe. Updated to correct data when face_counts() is called.
    die_type : string
        die_type is a string type attribute. It stores the string specifying the type of face values of the dice.
    '''
    
    def __init__(self, game):
        self.game = game
        self.jackpot_count = 0
        self.jackpot_dataframe = pd.DataFrame()
        self.combo_frame = pd.DataFrame()
        self.face_count = pd.DataFrame()
        self.die_type = type(game._list_of_die[0])
        
    def jackpot(self):
        '''
        A method to count the occurrence of jackpots in the game.

        Parameters
        ----------
        None

        Returns
        -------
        Dataframe including the rows in which there were jackpots. 
        Shows the roll number, the die number and the face rolled for each roll.
        '''
        self.jackpot_dataframe = pd.DataFrame()
        for i in range(1, self.game.show_result().T.shape[1]+1):
            if ((len(set(self.game.show_result().loc[[i]].values[0].flatten())))==1):
                temp = self.game.show_result().loc[[i]]
                self.jackpot_dataframe = pd.concat([self.jackpot_dataframe, temp], axis=0)
        self.jackpot_count = self.jackpot_dataframe.shape[0]
        return self.jackpot_count
    
    def combo(self, permutation=False):
        '''
        A method to return the dataframe that contains all combinations of the rolled face value, along with their occurrence.

        Parameters
        ----------
        permutation
            Boolean parameter to determine whether the function would count permutations instead of combinations.
            Defaults to False.

        Returns
        -------
        Dataframe including all combinations or permutations from a game. 
        The face values are turned into multi-indexes. The column shows the occurrences of each combination/permutation.
        '''
        self.combo_frame = pd.DataFrame()
        if permutation:
            new_names = ["#"+str(i)+" die's value" for i in range(1, len(self.game._list_of_die)+1)]
            temp_df = self.game.show_result()
            temp_df.columns = new_names
            x = list(range(len(self.game._list_of_die)))
            return temp_df.set_index(new_names).sort_index().groupby(level=x).size().to_frame("Occurence")
        else:
            self.combo_frame = self.game.show_result().apply(lambda x: pd.Series(sorted(x)), 1).value_counts().to_frame('Occurrence')
            self.combo_frame.index.names = ["Face Value #"+str(i) for i in range(1, len(self.game._list_of_die)+1)]
            return self.combo_frame
    
    
    def face_counts(self):
        '''
        A method to return the dataframe that counts the occurrence of each face value in each roll.

        Parameters
        ----------
        None

        Returns
        -------
        Dataframe including the counts of the occurrence of each face value in each roll.
        The indexes indicate the roll number, and the columns indicate the face values of the dice.
        '''
        self.face_count = self.game.show_result().apply(pd.Series.value_counts, axis=1).fillna(0).astype(int)
        self.face_count.columns.name = "Face of Die"
        return self.face_count
        