import argparse

import pandas as pd


# Column names for the grades file
name_column = 'Nome'
surname_column = 'Sobrenome'
email_column = 'Endereço de email'
final_grade_column = 'Total do curso (Real)'
last_download_column = 'Último download realizado neste curso.'

# New full name column
fullname_column = 'Nome completo'


# Main cleaning function
def clean_dataset(source_dataset_path, target_dataset_path) -> None:
    """clean_dataset takes the path to the dataset to clean and saves the cleaned dataset on the target path.

    The procedure will remove the first name and surname columns and add a complete name column instead."""
    df = pd.read_excel(source_dataset_path)
    df = join_name_columns(df)
    with pd.ExcelWriter(target_dataset_path) as writer:
        df.to_excel(writer, index=False)


def join_name_columns(df) -> pd.DataFrame:
    """Combines first name and last name columns info one full name column."""
    df[fullname_column] = df[name_column] + ' ' + df[surname_column]
    df.drop([name_column, surname_column], axis=1, inplace=True)
    return df


# Main script
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''Use this tool to clean the grades obtained from moodle,
        transforming separated first and last name columns into one column with a full name.''')
    parser.add_argument("source_path", help="Path to the moodle grades to clean")
    parser.add_argument("target_path", help="Path to save the cleaned grades")

    args = parser.parse_args()
    clean_dataset(args.source_path, args.target_path)
