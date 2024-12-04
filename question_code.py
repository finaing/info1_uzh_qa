import pandas as pd


def read_excel_file(file_path):
    df = pd.read_excel(file_path)
    return df


def shuffle_questions(df):
    shuffled_df = df.sample(frac=1).reset_index(drop=True)
    return shuffled_df


def main():
    # only change this if the code and the file are not in the same directory
    file_path = "stripped_questions.xlsx"
    df = read_excel_file(file_path)

    shuffled_df = shuffle_questions(df)

    for index, row in shuffled_df.iterrows():
        question = row['Question']
        answer = str(row['Answer']).upper()

        user_input = input(
            f"\nQuestion: {question}\nYour answer (True/False): ").upper()

        if user_input == answer:
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is {answer}.\n")


if __name__ == "__main__":
    main()
