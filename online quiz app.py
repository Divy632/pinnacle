import tkinter as tk
from tkinter import messagebox


quiz_data = {
    'Spritual': [
        {
            'question': 'What is the name of sabha of Shri Krishn?',
            'choices': ['A. MahaSabha', 'B. Swadharmasabha', 'C. Krishnsabha', 'D. Shrisabha'],
            'answer': 'B'
        },
        {
            'question': 'How many Shlokas MAHABHARAT has?',
            'choices': ['A. 18000', 'B. 50000', 'C. 100000', 'D. NONE OF THESE'],
            'answer': 'C'
        },
        {
            'question': 'Who is considered the author of the Bhagavad Gita?',
            'choices': ['A. Lord Krishna', 'B. Vyasa', 'C. Valmiki', 'D. Hanuman'],
            'answer': 'B'
        },
        {
            'question': 'What is the name of the sacred river in India?',
            'choices': ['A. Ganges', 'B. Yamuna', 'C. Brahmaputra', 'D. Godavari'],
            'answer': 'A'
        }
    ],
    'General Knowledge': [
        {
            'question': 'What is the capital of INDIA?',
            'choices': ['A. New Delhi', 'B. Mumbai', 'C. UP', 'D. J&K'],
            'answer': 'A'
        },
        {
            'question': 'Who wrote "Romeo and Juliet"?',
            'choices': ['A. Charles Dickens', 'B. William Shakespeare', 'C. Mark Twain', 'D. J.K. Rowling'],
            'answer': 'B'
        },
        {
            'question': 'Which country is known as the Land of the Rising Sun?',
            'choices': ['A. China', 'B. Japan', 'C. India', 'D. South Korea'],
            'answer': 'B'
        },
        {
            'question': 'Who was the first President of the United States?',
            'choices': ['A. George Washington', 'B. Abraham Lincoln', 'C. John F. Kennedy', 'D. Thomas Jefferson'],
            'answer': 'A'
        }
    ],
    'Science': [
        {
            'question': 'What is the chemical symbol for water?',
            'choices': ['A. H2O', 'B. O2', 'C. CO2', 'D. H2O2'],
            'answer': 'A'
        },
        {
            'question': 'What planet is known as the Red Planet?',
            'choices': ['A. Earth', 'B. Mars', 'C. Jupiter', 'D. Venus'],
            'answer': 'B'
        },
        {
            'question': 'What gas do plants absorb from the air?',
            'choices': ['A. Oxygen', 'B. Nitrogen', 'C. Carbon Dioxide', 'D. Hydrogen'],
            'answer': 'C'
        },
        {
            'question': 'What is the human body’s largest organ?',
            'choices': ['A. Liver', 'B. Skin', 'C. Heart', 'D. Brain'],
            'answer': 'B'
        }
    ]
}



class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Online Quiz Platform")
        self.root.geometry("500x500")
        self.quiz_category = ""
        self.question_index = 0
        self.score = 0

        self.title= tk.Label(self.root, text="Welcome to the Quiz!", font=("Helvotica", 20))
        self.title.pack(pady=20)

        self.category= tk.Label(self.root, text="Select Quiz Category:", font=("Arial", 14))
        self.category.pack(pady=20)
        

        self.category_listbox = tk.Listbox(self.root, height=4, font=("Arial", 12))
        self.load_categories()
        self.category_listbox.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Start Quiz", font=("Arial", 12), command=self.start_quiz)
        self.start_button.pack(pady=20)

    def load_categories(self):
        self.category_listbox.delete(0, tk.END)
        if quiz_data:
            for category in quiz_data:
                self.category_listbox.insert(tk.END, category)
        else:
            self.category_listbox.insert(tk.END, "No quizzes yet!")

    def start_quiz(self):
        selected_index = self.category_listbox.curselection()
        if selected_index:
            self.quiz_category = self.category_listbox.get(selected_index)
            self.question_index = 0
            self.score = 0
            self.category.pack_forget()
            self.category_listbox.pack_forget()
            self.start_button.pack_forget()

            self.ask_question()
        else:
            messagebox.showerror("Error", "Please first select a quiz category.")

    def ask_question(self):
        questions = quiz_data[self.quiz_category]
        if self.question_index < len(questions):
            question_data = questions[self.question_index]
            question_text = question_data["question"]
            choices = question_data["choices"]
            self.question_label = tk.Label(self.root, text=question_text, font=("Arial", 14))
            self.question_label.pack(pady=10)

            self.choices_var = tk.StringVar()
            self.choice_buttons = []
            for choice in choices:
                button = tk.Radiobutton(self.root, text=choice, value=choice[0], variable=self.choices_var, font=("Arial", 12))
                button.pack(pady=5)
                self.choice_buttons.append(button)

            self.submit_button = tk.Button(self.root, text="Submit Answer", font=("Arial", 12), command=self.check_answer)
            self.submit_button.pack(pady=20)
        else:
            self.show_results()

    def check_answer(self):
        selected_answer = self.choices_var.get()
        correct_answer = quiz_data[self.quiz_category][self.question_index]["answer"]

        if selected_answer == correct_answer:
            self.score += 1
        self.question_index += 1
        self.clear_ui()
        self.ask_question()

    def clear_ui(self):
        self.question_label.pack_forget()
        for button in self.choice_buttons:
            button.pack_forget()
        self.submit_button.pack_forget()

    def show_results(self):
        messagebox.showinfo("Quiz Finished", f"Your score is: {self.score}")
        self.reset_ui()
    def reset_ui(self):
        self.category.pack(pady=10)
        self.category_listbox.pack(pady=10)
        self.start_button.pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
