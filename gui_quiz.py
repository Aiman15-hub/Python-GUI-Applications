import tkinter as tk
from tkinter import messagebox

# 1. Setup the Quiz Questions & Answers
quiz_data = [
    {"question": "What does HTML stand for?", "answer": "hyper text markup language"},
    {"question": "What is 3 + 4?", "answer": "7"},
    {"question": "What is 1 + 9?", "answer": "10"},
    {"question": "Who is the leader of BTS?", "answer": "rm"}
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aiman's Mini Quiz Game 🧠✨")
        self.root.geometry("450x300")
        self.root.config(bg="#f3e8ee")  # Soft, cute background color
        
        self.current_question_index = 0
        self.score = 0
        
        # 2. GUI Elements / Widgets
        self.title_label = tk.Label(root, text="Welcome to the Quiz!", font=("Helvetica", 16, "bold"), bg="#f3e8ee", fg="#4a3b4e")
        self.title_label.pack(pady=15)
        
        self.question_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f3e8ee", fg="#333333", wraplength=400)
        self.question_label.pack(pady=15)
        
        self.answer_entry = tk.Entry(root, font=("Helvetica", 12), width=30, bd=2, relief="groove")
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind("<Return>", lambda event: self.check_answer()) # Allows pressing 'Enter' to submit
        
        self.submit_button = tk.Button(root, text="Submit Answer 🚀", font=("Helvetica", 11, "bold"), bg="#d8b4f8", fg="#ffffff", activebackground="#c39bd3", bd=0, padx=10, pady=5, command=self.check_answer)
        self.submit_button.pack(pady=15)
        
        # Load the very first question
        self.load_question()
        
    def load_question(self):
        # Check if there are still questions left
        if self.current_question_index < len(quiz_data):
            current_q = quiz_data[self.current_question_index]["question"]
            self.question_label.config(text=current_q)
            self.answer_entry.delete(0, tk.END)  # Clear the entry box for the next question
        else:
            # Quiz finished! Show final score popup
            messagebox.showinfo("Quiz Completed! 🎉", f"Great job, buddy!\nYour final score is: {self.score}/{len(quiz_data)}")
            self.root.destroy()  # Close the app window
            
    def check_answer(self):
        user_input = self.answer_entry.get().strip().lower()
        correct_answer = quiz_data[self.current_question_index]["answer"]
        
        if user_input == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct! ✅", "Awesome job! That's correct!")
        else:
            messagebox.showerror("Incorrect! ❌", f"Oops! The correct answer was: '{correct_answer}'")
            
        # Move to the next question and update the screen
        self.current_question_index += 1
        self.load_question()

# 3. Initialize and Run the App Window
if __name__ == "__main__":
    window = tk.Tk()
    app = QuizApp(window)
    window.mainloop()