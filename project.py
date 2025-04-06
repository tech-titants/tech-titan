import tkinter as tk
from tkinter import ttk
import random
import time
import winsound# For sound effects on Windows
# Define multiple-choice questions and answers
questions = [("What is 1258 +8521 ?", ["10000", "9779", "8745", "9790"], "9779"),
    ("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris"),
    ("What is the largest planet in our solar system?", ["Earth", "Jupiter", "Saturn", "Mars"], "Jupiter"),
    ("Who wrote 'Romeo and Juliet'?", ["Shakespeare", "Dickens", "Hemingway", "Austen"], "Shakespeare"),
    ("What is the freezing point of water in Celsius?", ["0", "10", "32", "100"], "0"),
    ("Which is the fastest animal in the forest?", ["Lion", "Cheetah", "Tiger", "Bear"], "Cheetah"),
    ("What is the tallest mountain in the world?", ["K2", "Everest", "Kangchenjunga", "Makalu"], "Everest"),
    ("What is the smallest planet in our solar system?", ["Mars", "Venus", "Mercury", "Earth"], "Mercury"),
    ("In which year did the Titanic sink?", ["1912", "1905", "1920", "1935"], "1912"),
    ("Which element's chemical symbol is 'O'?", ["Oxygen", "Osmium", "Ozone", "Oganesson"], "Oxygen"),
    ("What is the longest river in the world?", ["Amazon", "Nile", "Yangtze", "Ganges"], "Nile"),
    ("Who painted the Mona Lisa?", ["Van Gogh", "Picasso", "Leonardo da Vinci", "Rembrandt"], "Leonardo da Vinci"),
    ("What is the capital of Japan?", ["Beijing", "Seoul", "Tokyo", "Bangkok"], "Tokyo"),
    ("What is the symbol for gold on the periodic table?", ["Au", "Ag", "Pb", "Fe"], "Au"),
    ("How many continents are there?", ["5", "6", "7", "8"], "7"),
    ("Which country is known as the Land of the Rising Sun?", ["China", "South Korea", "Japan", "Thailand"], "Japan"),
    ("Who is the author of '1984'?", ["George Orwell", "J.K. Rowling", "Mark Twain", "Ernest Hemingway"], "George Orwell"),
    ("What is the speed of light?", ["300,000 km/s", "150,000 km/s", "500,000 km/s", "1,000,000 km/s"], "300,000 km/s"),
    ("Which ocean is the largest?", ["Atlantic", "Indian", "Arctic", "Pacific"], "Pacific"),
    ("Who discovered gravity?", ["Einstein", "Newton", "Galileo", "Tesla"], "Newton"),
    ("What is the chemical symbol for water?", ["CO2", "H2O", "O2", "NaCl"], "H2O"),
    ("What is the capital of Australia?", ["Sydney", "Melbourne", "Canberra", "Perth"], "Canberra"),
    ("What is the square root of 64?", ["6", "7", "8", "9"], "8"),
    ("Who invented the light bulb?", ["Edison", "Tesla", "Faraday", "Newton"], "Edison"),
    ("Which gas do plants absorb from the air for photosynthesis?", ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "Carbon Dioxide"),
    ("What is the smallest country in the world?", ["Vatican City", "Monaco", "Nauru", "San Marino"], "Vatican City"),
    ("What is the name of the longest bone in the human body?", ["Femur", "Tibia", "Fibula", "Humerus"], "Femur"),
    ("Which is the largest continent?", ["Africa", "Asia", "Europe", "North America"], "Asia"),
    ("Which is the fastest animal on land?", ["Cheetah", "Lion", "Tiger", "Elephant"], "Cheetah"),
    ("Who was the first man to walk on the moon?", ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "Michael Collins"], "Neil Armstrong"),
    ("Which famous scientist developed the theory of relativity?", ["Newton", "Einstein", "Tesla", "Hawking"], "Einstein"),
    ("What is the largest ocean in the world?", ["Atlantic", "Pacific", "Indian", "Arctic"], "Pacific"),
    ("Which bird is known for its ability to mimic human speech?", ["Parrot", "Crow", "Sparrow", "Eagle"], "Parrot"),
    ("What is the capital of Canada?", ["Ottawa", "Toronto", "Vancouver", "Montreal"], "Ottawa"),
    ("Who is known as the Father of Computers?", ["Charles Babbage", "Alan Turing", "Bill Gates", "Steve Jobs"], "Charles Babbage"),
    ("In what year did World War II end?", ["1940", "1942", "1945", "1950"], "1945"),
    ("What is the tallest building in the world?", ["Burj Khalifa", "Eiffel Tower", "Empire State Building", "Shanghai Tower"], "Burj Khalifa"),
    ("What is the capital of Egypt?", ["Cairo", "Alexandria", "Luxor", "Aswan"], "Cairo"),
    ("What is the largest desert in the world?", ["Sahara", "Gobi", "Arctic", "Antarctic"], "Antarctic"),
    ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Venus", "Jupiter"], "Mars"),
    ("What is the main ingredient in guacamole?", ["Tomato", "Avocado", "Onion", "Pepper"], "Avocado"),
    ("How many hearts does an octopus have?", ["1", "2", "3", "4"], "3"),
    ("Who is the author of 'Harry Potter'?", ["J.K. Rowling", "George R.R. Martin", "J.R.R. Tolkien", "C.S. Lewis"], "J.K. Rowling"),
    ("Which country is home to the Great Barrier Reef?", ["Australia", "South Africa", "USA", "India"], "Australia"),
    ("What is the largest species of shark?", ["Great White Shark", "Hammerhead Shark", "Whale Shark", "Tiger Shark"], "Whale Shark"),
    ("Which famous battle was fought in 1066?", ["Battle of Hastings", "Battle of Waterloo", "Battle of Gettysburg", "Battle of Agincourt"], "Battle of Hastings"),
    ("Which element has the atomic number 1?", ["Helium", "Oxygen", "Hydrogen", "Carbon"], "Hydrogen"),
    ("What is the deepest part of the world's oceans?", ["Mariana Trench", "Challenger Deep", "Abyssal Plain", "Great Barrier Reef"], "Mariana Trench"),
    ("Who discovered America?", ["Christopher Columbus", "Vasco da Gama", "Marco Polo", "Leif Erikson"], "Christopher Columbus"),
    ("Which animal is known for its ability to regenerate limbs?", ["Starfish", "Axolotl", "Lizard", "Spider"], "Axolotl"),
    ("What is the capital of Italy?", ["Rome", "Paris", "Berlin", "Madrid"], "Rome"),
    ("What is the hardest natural substance on Earth?", ["Diamond", "Gold", "Iron", "Platinum"], "Diamond"),
    ("Who was the first woman to fly solo across the Atlantic Ocean?", ["Amelia Earhart", "Harriet Quimby", "Bessie Coleman", "Ellen Church"], "Amelia Earhart"),
    ("What is the largest island in the world?", ["Australia", "Greenland", "New Guinea", "Borneo"], "Greenland"),
    ("Who invented the telephone?", ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Samuel Morse"], "Alexander Graham Bell"),
    ("What is the smallest bone in the human body?", ["Stapes", "Femur", "Tibia", "Radius"], "Stapes"),
    ("Which country is known as the Land of Ice and Fire?", ["Iceland", "Greenland", "Norway", "Sweden"], "Iceland"),
    ("What is the most common gas in the Earth's atmosphere?", ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "Nitrogen"),
    ("Which country is known as the 'Pearl of the Indian Ocean'?", ["Sri Lanka", "India", "Maldives", "Mauritius"], "Sri Lanka"),
    ("What is the capital of Brazil?", ["Rio de Janeiro", "São Paulo", "Brasília", "Salvador"], "Brasília"),
    ("What is the largest volcano in the world?", ["Mount St. Helens", "Mount Fuji", "Mauna Loa", "Mount Vesuvius"], "Mauna Loa"),
    ("What is the name of the first artificial Earth satellite?", ["Sputnik", "Apollo", "Gemini", "Explorer"], "Sputnik"),
    ("Which organ in the human body is primarily responsible for pumping blood?", ["Brain", "Lungs", "Heart", "Kidneys"], "Heart"),
    ("Which gas makes up most of the Earth's atmosphere?", ["Oxygen", "Nitrogen", "Carbon Dioxide", "Helium"], "Nitrogen"),
] * 1  # Repeat these questions to reach 100 questions (some are repeated for illustration)
random.shuffle(questions)

# Game settings
time_limit = 60 * 60  # 1 hour (currently unused, can add a timer later)
lives = 4
score = 0
current_question_index = 0
start_time = time.time()
game_over = False
correct_answers = 0
# Create the main window
root = tk.Tk()
root.title("Quiz Game")
root.geometry("600x500")
root.configure(bg="#2C3E50")

# Setup GUI elements
question_label = tk.Label(root, text="Question will appear here", font=("Helvetica", 16), width=40, height=2, bg="#f0f0f0")
question_label.pack(pady=20)


# Buttons for answer choices
answer_buttons = []

# Create styles for correct and incorrect answers
style = ttk.Style()
style.configure("Success.TButton", background="green", foreground="white")
style.map("Success.TButton", background=[("active", "dark green")])

style.configure("Danger.TButton", background="red", foreground="white")
style.map("Danger.TButton", background=[("active", "dark red")])

# Frame for quiz content
frame = ttk.Frame(root, padding="20", relief="solid", borderwidth=2)
frame.pack(padx=10, pady=10, expand=True)

# Lives and Score labels
lives_label = ttk.Label(frame, text=f"Lives: {lives}", font=("Arial", 14), background="#2C3E50", foreground="white")
lives_label.grid(row=0, column=0, pady=10)

score_label = ttk.Label(frame, text=f"Score: {score}", font=("Arial", 14), background="#2C3E50", foreground="white")
score_label.grid(row=0, column=1, pady=10)

# Question label
question_label = ttk.Label(frame, text="", font=("Arial", 16), wraplength=500, background="#2C3E50", foreground="white")
question_label.grid(row=1, column=0, columnspan=4, pady=20)

# Answer buttons
answer_buttons = []
def create_answer_buttons():
    for i in range(4):
        button = ttk.Button(frame, text="", width=20, command=lambda b=i: check_answer(b))
        button.grid(row=2 + i, column=0, columnspan=4, pady=5, padx=5)
        answer_buttons.append(button)
create_answer_buttons()

# Update the question and choices
def next_question():
    global current_question_index

    if current_question_index >= len(questions):
        show_results()
        return

    question, choices, _ = questions[current_question_index]
    question_label.config(text=question)

    for i, button in enumerate(answer_buttons):
        button.config(text=choices[i], style="TButton", state=tk.NORMAL)

# Check the selected answer
def check_answer(button_index):
    global lives, score, current_question_index

    question, choices, correct_answer = questions[current_question_index]
    user_answer = answer_buttons[button_index].cget("text")

    if user_answer == correct_answer:
        score += 1
        score_label.config(text=f"Score: {score}")
        change_button_color(answer_buttons[button_index], "green")
    else:
        lives -= 1
        lives_label.config(text=f"Lives: {lives}")
        change_button_color(answer_buttons[button_index], "red")

    # Disable buttons temporarily
    for button in answer_buttons:
        button.config(state=tk.DISABLED)

    current_question_index += 1

    if lives == 0:
        root.after(1000, show_results)
    else:
        root.after(1000, next_question)

# Change button color based on result
def change_button_color(button, color):
    if color == "green":
        button.config(style="Success.TButton")
    else:
        button.config(style="Danger.TButton")

# Show final results
def show_results():
    for button in answer_buttons:
        button.grid_remove()  # Hide answer buttons

    question_label.grid_remove()

    if score == len(questions):
        message = (
            "🎉🎉🎉 Congrats! You answered all questions correctly! 🎉🎉🎉\n"
            "🌸🌸🌸 Enjoy the flowers and candy! 🌸🌸🌸\n"
            "🍬🍬🍬 Here’s your reward! 🍬🍬🍬"
        )
    else:
        message = "Better luck next time! 😊"

    result_text = f"Your final score is {score} out of {len(questions)}."

    celebration_label = ttk.Label(frame, text=message, font=("Arial", 16), background="#2C3E50", foreground="white", wraplength=500)
    celebration_label.grid(row=2, column=0, columnspan=4, pady=20)

    result_label = ttk.Label(frame, text=result_text, font=("Arial", 16), background="#2C3E50", foreground="white")
    result_label.grid(row=7, column=0, columnspan=4, pady=10)

# Start the game
next_question()
root.mainloop()
