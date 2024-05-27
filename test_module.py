import unittest
import pandas as pd
from medical_data_visualizer import df, draw_cat_plot, draw_heat_map

class MedicalDataVisualizerTest(unittest.TestCase):
    def setUp(self):
        # Set up any necessary data for testing
        self.df = df.copy()

    def test_overweight_column(self):
        # Check if the overweight column has been correctly added
        self.assertIn('overweight', self.df.columns)
        self.assertTrue(all(self.df['overweight'].apply(lambda x: x in [0, 1])))

    def test_normalized_columns(self):
        # Check if cholesterol and gluc columns have been normalized
        self.assertTrue(all(self.df['cholesterol'].apply(lambda x: x in [0, 1])))
        self.assertTrue(all(self.df['gluc'].apply(lambda x: x in [0, 1])))

    def test_cat_plot(self):
        # Check if the categorical plot is created without errors
        fig = draw_cat_plot()
        self.assertIsNotNone(fig)

    def test_heat_map(self):
        # Check if the heatmap is created without errors
        fig = draw_heat_map()
        self.assertIsNotNone(fig)

def run_tests():
    unittest.main(argv=[''], exit=False)

if __name__ == "__main__":
    run_tests()
