import unittest
from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer
import pandas as pd
import numpy as np
import pandas.testing as pdt

class SimulatorClassesTestCase(unittest.TestCase): 
    
    def test_change_weight_happypath(self):
        die = Die([1,2,3,4,5,6])
        die.change_weight(3, 4.0)
        expected = 4
        actual = die.show_faces_weights().loc[die.show_faces_weights()['Faces'] == 3, "Weights"].values[0]
        self.assertEquals(expected, actual)

    def test_change_weight_face_not_exist(self):
        die = Die([1,2,3,4,5,6])
        die2 = Die([1,2,3,4,5,6])
        die.change_weight(7, 4.0)
        pdt.assert_frame_equal(die.show_faces_weights(), die2.show_faces_weights())
        
    def test_change_weight_not_float(self):
        die = Die([1,2,3,4,5,6])
        die.change_weight(1, "Hi")
        wrong_weight = "Hi"
        actual_weight = die.show_faces_weights().loc[die.show_faces_weights()['Faces'] == 1, "Weights"].values[0]
        self.assertFalse(wrong_weight==actual_weight)
     

    def test_roll_one(self):
        die = Die([1,2,3,4,5,6])
        expected = 1
        actual = len(die.roll())
        self.assertEquals(expected, actual)
        
    def test_roll_multiple(self):
        die = Die([1,2,3,4,5,6])
        expected = 5
        actual = len(die.roll(5))
        self.assertEquals(expected, actual)
        
    def test_show_faces_weights(self):
        die = Die([1,2,3,4,5,6])
        expected_dataframe = pd.DataFrame({"Faces":[1,2,3,4,5,6], "Weights":[1.0,1.0,1.0,1.0,1.0,1.0]})
        actual_dataframe = die.show_faces_weights()
        pdt.assert_frame_equal(expected_dataframe, actual_dataframe)
        
    def test_play(self):
        game = Game([Die([1,2,3]), Die([1,2,3]), Die([1,2,3])])
        game.play(100)
        expected_rows = 100
        actual_rows = game.show_result().shape[0]
        self.assertEquals(expected_rows, actual_rows)
        expected_columns = 3
        actual_columns = game.show_result().shape[1]
        self.assertEquals(expected_columns, actual_columns)
    
    def test_show_results_wide(self):
        game = Game([Die([1,2,3]), Die([1,2,3]), Die([1,2,3])])
        game.play(100)
        expected_rows = 100
        actual_rows = game.show_result(form="wide").shape[0]
        self.assertEquals(expected_rows, actual_rows)
        expected_columns = 3
        actual_columns = game.show_result(form="wide").shape[1]
        self.assertEquals(expected_columns, actual_columns)
        
    def test_show_results_narrow(self):
        game = Game([Die([1,2,3]), Die([1,2,3]), Die([1,2,3])])
        game.play(100)
        expected_rows = 300
        actual_rows = game.show_result(form="narrow").shape[0]
        self.assertEquals(expected_rows, actual_rows)
        expected_columns = 1
        actual_columns = game.show_result(form="narrow").shape[1]
        self.assertEquals(expected_columns, actual_columns)
    
    def test_jackpot(self):
        game = Game([Die([1,2,3]), Die([1,2,3]), Die([1,2,3])])
        game.play(100)
        analyzer = Analyzer(game)
        jackpot_amt = analyzer.jackpot()
        jackpot_dataframe_rows = analyzer.jackpot_dataframe.shape[0]
        self.assertEquals(jackpot_amt, jackpot_dataframe_rows)
        
    def test_combo(self):
        game = Game([Die([1,2,3]), Die([1,2,3]), Die([1,2,3])])
        game.play(100)
        analyzer = Analyzer(game)
        combo_dataframe = analyzer.combo()
        expected_amt_of_col = 1
        actual_amt_of_col = combo_dataframe.shape[1]
        self.assertEquals(expected_amt_of_col, actual_amt_of_col)
        expected_amt_of_index = 3
        actual_amt_of_index = len(combo_dataframe.index.names)
        self.assertEquals(expected_amt_of_index, actual_amt_of_index)
        
    def test_combo_permutation(self):
        game = Game([Die([1,2,3]), Die([1,2,3]), Die([1,2,3])])
        game.play(100)
        analyzer = Analyzer(game)
        permutation_dataframe = analyzer.combo(permutation=True)
        expected_amt_of_col = 1
        actual_amt_of_col = permutation_dataframe.shape[1]
        self.assertEquals(expected_amt_of_col, actual_amt_of_col)
        expected_amt_of_index = 3
        actual_amt_of_index = len(permutation_dataframe.index.names)
        self.assertEquals(expected_amt_of_index, actual_amt_of_index)
        
        
    def test_face_counts(self):
        game = Game([Die([1,2,3]), Die([1,2,3]), Die([1,2,3])])
        game.play(100)
        analyzer = Analyzer(game)
        face_count_dataframe = analyzer.face_counts()
        expected_amt_of_col = 3
        actual_amt_of_col = face_count_dataframe.shape[1]
        self.assertEquals(expected_amt_of_col, actual_amt_of_col)
        expected_amt_of_rows = 100
        actual_amt_of_rows = face_count_dataframe.shape[0]
        self.assertEquals(expected_amt_of_rows, actual_amt_of_rows)
        
    
if __name__ == '__main__':
    unittest.main(verbosity=2)