import pandas as pd
import tkinter as tk
from tkinter import messagebox

def read_excel_file(file_path):
    df = pd.read_excel(file_path)
    return df

def shuffle_questions(df):
    shuffled_df = df.sample(frac=1).reset_index(drop=True)
    return shuffled_df

class QuizApp:
    def __init__(self, master, df):
        self.master = master
        self.df = df
        self.shuffled_df = shuffle_questions(df)
        self.current_question_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0

        
        self.master.geometry("500x300")  
        self.default_font = ("Helvetica", 12)

        
        self.question_label = tk.Label(
            master, text="", wraplength=400, font=self.default_font
        )
        self.question_label.pack(pady=20)

        
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=10)

        self.yes_button = tk.Button(
            self.button_frame, text="Yes", font=self.default_font, command=self.yes_pressed
        )
        self.yes_button.pack(side=tk.LEFT, padx=10)

        self.no_button = tk.Button(
            self.button_frame, text="No", font=self.default_font, command=self.no_pressed
        )
        self.no_button.pack(side=tk.RIGHT, padx=10)

        self.update_question()

        
        master.bind('1', lambda event: self.yes_pressed())
        master.bind('2', lambda event: self.no_pressed())

        
        self.stats_window = tk.Toplevel(master)
        self.stats_window.title("Quiz Stats")
        self.stats_window.geometry("300x150")

        self.stats_label = tk.Label(
            self.stats_window, text="", font=self.default_font
        )
        self.stats_label.pack(pady=20)
        self.update_stats()

    def update_question(self):
        if not self.shuffled_df.empty:
            question = self.shuffled_df.iloc[0]['Question']
            self.answer = str(self.shuffled_df.iloc[0]['Answer']).upper()
            self.question_label.config(text=question)
        else:
            self.show_results()

    def yes_pressed(self):
        self.check_answer("TRUE")

    def no_pressed(self):
        self.check_answer("FALSE")

    def check_answer(self, user_input):
        if user_input.upper() == self.answer:
            self.correct_answers += 1
        else:
            self.incorrect_answers += 1

        self.shuffled_df = self.shuffled_df.iloc[1:].reset_index(drop=True)
        self.update_question()
        self.update_stats()

    def update_stats(self):
        total_left = len(self.shuffled_df)
        stats_text = (f"Total Questions Left: {total_left}\n"
                      f"Correct Answers: {self.correct_answers}\n"
                      f"Wrong Answers: {self.incorrect_answers}")
        self.stats_label.config(text=stats_text)

    def show_results(self):
        total_questions = self.correct_answers + self.incorrect_answers
        if total_questions > 0:
            correctness_rate = self.correct_answers / total_questions * 100
        else:
            correctness_rate = 0
        messagebox.showinfo("Quiz Finished", f"You have a correctness rate of: {correctness_rate:.2f}%")
        self.master.quit()

def main():
    file_path = "stripped_questions.xlsx"
    df = read_excel_file(file_path)

    root = tk.Tk()
    root.title("INFO1 QUIZ")
    QuizApp(root, df)
    root.mainloop()

if __name__ == "__main__":
    main()
