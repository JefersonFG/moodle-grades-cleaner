import os
import unittest

import pandas as pd

import grades_cleaner


class CleanerTest(unittest.TestCase):
    test_dataset_path = 'test_dataset.xlsx'
    cleaned_dataset_path = 'cleaned_dataset.xlsx'

    # List of columns to be removed on the cleaned dataset
    columns_to_be_removed = [grades_cleaner.name_column, grades_cleaner.surname_column,
                             grades_cleaner.email_column, grades_cleaner.last_download_column]

    def setUp(self):
        """"setUp creates the test dataset with valid data"""
        df = pd.DataFrame(
            {
                'Nome': [
                    'NOME1',
                    'NOME2',
                    'NOME3',
                ],
                'Sobrenome': [
                    'SOBRENOME ALUNO 1',
                    'SOBRENOME ALUNO 2',
                    'SOBRENOME ALUNO 3'
                ],
                'Endereço de email': [
                    'aluno1@email.com',
                    'aluno2@email.com',
                    'aluno3@email.com'
                ],
                'Tarefa 1': [
                    '10',
                    '20',
                    '30'
                ],
                'Tarefa 2': [
                    '40',
                    '50',
                    '60'
                ],
                'Tarefa 3': [
                    '70',
                    '80',
                    '90'
                ],
                'Total do curso (Real)': [
                    '50',
                    '50',
                    '50'
                ],
                'Último download realizado neste curso.': [
                    '123456789',
                    '123456789',
                    '123456789'
                ],
            }
        )

        with pd.ExcelWriter(self.test_dataset_path) as writer:
            df.to_excel(writer, index=False)

    def tearDown(self):
        """tearDown deletes both the source and the target files to clean up after the tests"""
        if os.path.exists(self.test_dataset_path):
            os.remove(self.test_dataset_path)
        if os.path.exists(self.cleaned_dataset_path):
            os.remove(self.cleaned_dataset_path)

    def test_create_cleaned_dataset(self):
        """Tests that the cleaned dataset is created, but doesn't validate its contents"""
        grades_cleaner.clean_dataset(self.test_dataset_path, self.cleaned_dataset_path)
        self.assertTrue(os.path.exists(self.cleaned_dataset_path), "Cleaned dataset not created")

    def test_join_first_and_last_names(self):
        """Tests that the first and last name columns are joined into one"""
        grades_cleaner.clean_dataset(self.test_dataset_path, self.cleaned_dataset_path)
        df = pd.read_excel(self.cleaned_dataset_path)
        self.assertIn(grades_cleaner.fullname_column, df.columns, 'Final dataset missing full name column')

    def test_removed_columns(self):
        """Tests that irrelevant columns have been removed from the dataset"""
        grades_cleaner.clean_dataset(self.test_dataset_path, self.cleaned_dataset_path)
        df = pd.read_excel(self.cleaned_dataset_path)
        for column in self.columns_to_be_removed:
            self.assertNotIn(column, df.columns, f"found column '{column}' in the cleaned dataset")


if __name__ == '__main__':
    unittest.main()
