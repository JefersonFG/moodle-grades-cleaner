import argparse


# Main cleaning function
def clean_dataset(source_dataset_path, target_dataset_path) -> None:
    """clean_dataset takes the path to the dataset to clean and saves the cleaned dataset on the target path.

    The procedure will remove the first name and surname columns and add a complete name column instead."""
    raise Exception("Not implemented")


# Main script
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''Use this tool to clean the grades obtained from moodle,
        transforming separated first and last name columns into one column with a full name.''')
    parser.add_argument("source_path", help="Path to the moodle grades to clean")
    parser.add_argument("target_path", help="Path to save the cleaned grades")

    args = parser.parse_args()
    clean_dataset(args.source_path, args.target_path)
