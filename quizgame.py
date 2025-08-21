import tkinter as tk
window = tk.Tk()
window.title("Quiz game")
window.geometry("800x400")
window.config(bg="lightyellow")

label = tk.Label(window , text = "Welcome to the quiz game !" , font = ("Ariel" , 29 , "bold") , fg = "blue" , bg = "lightgreen")
label.pack(pady=20, anchor="center")
rules_label = tk.Label(window, text="(+1 for correct, -0.25 for wrong)", font=("Arial", 14), fg="green")
rules_label.pack()

def start_section(start_index):
   global question_index
   global section_end
   global current_section
   question_index = start_index
   section_end = start_index+5 
   try:
      next_btn.pack_forget()    # hide the "Next Section" button
   except:
      pass


   current_section = start_index // 5 
   
   for widget in window.winfo_children():
      widget.pack_forget()   # only forget not destroy
   label3.config(text="")   # reset feedback label
   next_section()


btn_cs= tk.Button(window , text = "Section1 = Computer Science(Ques 1 - 5)" ,command = lambda: (start_section(0)), font = ("Ariel" , 20 , "bold") , fg = "green" ,bg = "lightpink")
btn_cs.pack(pady = 20)
btn_gk = tk.Button(window , text = "Section2 = General Knowledge(Ques 6 - 10)" , command = lambda: (start_section(5)) , font = ("Ariel" , 20 , "bold") , fg = "green" , bg = "lightpink")
btn_gk.pack(pady = 20)
btn_math = tk.Button(window , text = "Section3 = Maths(Ques 11 - 15)" , command = lambda: (start_section(10)), font = ("Ariel" , 20 , "bold") , fg = "green" , bg = "lightpink")
btn_math.pack(pady = 20)
btn_his = tk.Button(window , text = "Section4 = History(Ques 16 - 20)" , command = lambda: (start_section(15)), font = ("Ariel" , 20 , "bold") , fg = "green" , bg = "lightpink")
btn_his.pack(pady = 20)
btn_sci = tk.Button(window , text = "Section5 = Science(Ques 21 - 25)" , command = lambda: (start_section(20)), font = ("Ariel" , 20 , "bold") , fg = "green" , bg = "lightpink")
btn_sci.pack(pady = 20)


label3 = tk.Label(window , text = "" , font = ("Ariel" , 18 , "bold"))

question_index = 0
score = 0 
questions = [
    {
        "question" :"Ques1.What does CPU stand for?",
       "options" : ["Central process unit" , "Central processing unit" , "Computer personal unit" , "Control Processing unit"],
       "answer" : 2 
    },
    {
        "question" :"Ques2.Which language is known as backbone of web development?",
       "options" : ["Python" , "HTML" , "Java" , "C++"],
       "answer" : 2
    },
    {
         "question" :"Ques3. What is the brain of the computer?",
       "options" : ["RAM" , "Hard Disc" , "CPU" , "Monitor"],
       "answer" : 3,
    },
    {
         "question" :"Ques4. Which of these is not an operating system?",
       "options" : ["Windows" , "Linux" , "Oracle" , "Macos"],
       "answer" : 3,
    },
    {
        "question" :"Ques 5. What does RAM stand for?",
       "options" : ["Random Access Memory " , "Read Access Memory" , "Run All Memory" , "Random All Memory"],
       "answer" : 1,
    },
    {
       "question" :"Ques6: Who is known as the Father of the Nation (India)?",
       "options" : ["Nehru " , "Bhagat Singh" , "Mahatma Gandhi" , "Dr.Ambedkar"],
       "answer" : 3,
    },
    {
       "question" :"Ques7: Which is the longest river in the world?",
       "options" : ["Amazon" , "Ganga" , "Nile" , "Yangtze"],
       "answer" : 3,
    },
    {
       "question" :"Ques8: What is the capital of Australia?",
       "options" : ["Sydeny" , "Melbourne" , "Canberra" , "Perth"],
       "answer" : 3,
    },
    {
       "question" :"Ques9: How many continents are there in the World?",
       "options" : ["5" , "6" , "7" , "8"],
       "answer" : 3,
    },
    {
       "question" :"Ques10: Who wrote Indian National Anthem?",
       "options" : ["Bankim Chandra Chatergee" , "Rabindranath Tagore" , "Sarojini Naidu" , "Shubhash Chandra Bose"],
       "answer" : 2,
    },
    {
       "question" :"Ques11: What is 12 * 8 ?",
       "options" : ["80" , "96" , "84" , "92"],
       "answer" : 2,
    },
    {
       "question" :"Ques12: What is the square root of 144?",
       "options" : ["10" , "11" , "12" , "13"],
       "answer" : 3,
    },
    {
       "question" :"Ques13: What is 15 percent of 200?",
       "options" : ["25" , "30" , "35" , "40"],
       "answer" : 2,
    },
    {
       "question" :"Ques14: Which number is a prime number?",
       "options" : ["21" , "33" , "17" , "39"],
       "answer" : 3,
    },
    {
       "question" :"Ques15:  What comes next in the pattern (2,4,8,16)?",
       "options" : ["20" , "24" , "32" , "30"],
       "answer" : 3,
    },
    {
       "question" :"Ques16:  Who was the first Mughal emperor?",
       "options" : ["Akbar" , "Babar" , "Humayan" , "Shah Jahan"],
       "answer" : 2,
    },
    {
       "question" :"Ques17: When did India get independence?",
       "options" : ["1945" , "1946" , "1947" , "1950"],
       "answer" : 3,
    },
    {
       "question" :"Ques18: Who built the Red Fort?",
       "options" : ["Akbar" , "Babar" , "Humayan" , "Shah Jahan"],
       "answer" : 4,
    },
    {
       "question" :"Ques19: Who was known as Iron Man of India?",
       "options" : ["Nehru" , "Patel" , "Gandhi" , "Bose"],
       "answer" : 2,
    },
    {
       "question" :"Ques20: Where did the Jallianwala Bagh massacre happen ?",
       "options" : ["Delhi" , "Amritsar" , "Kolkata" , "Chennai"],
       "answer" : 2,
    },
    {
       "question" :"Ques21: What planet is known as Red Planet?",
       "options" : ["Earth" , "Mars" , "Jupiter" , "Venus"],
       "answer" : 2,
    },
    {
       "question" :"Ques22: Which part of the plant conducts photosynthesis?",
       "options" : ["Root" , "Stem" , "Leaf" , "Flower"],
       "answer" : 3,
    },
    {
       "question" :"Ques23:  Water boils at what temperature (Celsius)?",
       "options" : ["90 C" , "95 C" , "100 C" , "110 C"],
       "answer" : 3,
    },
    {
       "question" :"Ques24:  What gas do humans breathe in that is essential for survival?",
       "options" : ["Carbon di oxide" , "Oxygen" , "Nitrogen" , "Hydrogen"],
       "answer" : 2,
    },
    {
       "question" :"Ques25: Which organ pumps blood through the body ?",
       "options" : ["Brain" , "Kidney" , "Lungs" , "Heart"],
       "answer" : 4,
    },
]

question_label = tk.Label(window , text = " " , font = ("Ariel" , 18 , "bold") , fg = "orange",  bg = "lightpink" )

selected_option = tk.IntVar()
options_button = tk.Radiobutton(window , text = " " , variable = selected_option , value = 1 ,  bg = "lightgreen")
options_button2 = tk.Radiobutton(window , text = " " , variable = selected_option , value = 2 , bg = "lightgreen" )
options_button3 = tk.Radiobutton(window , text = " " , variable = selected_option , value =3 , bg = "lightgreen")
options_button4 = tk.Radiobutton(window , text = " " , variable = selected_option , value = 4 , bg = "lightgreen")


def load_question():
    global question_index
    global score 
    selected_option.set(0)
    label3.config(text="")  # clear feedback message

    try:
        start_btn.pack_forget()   # hide Start Section when quiz starts
    except:
        pass
    
    question_label.config(text = questions[question_index]["question"] , font = ("Ariel" , 18 , "bold") , fg = "black" , bg = "lightpink")
    question_label.pack(pady = 20)
    options_button.config(text = questions[question_index]["options"][0], value = 1, font = ("Ariel" , 16 , "bold") , fg = "grey")
    options_button.pack(pady = 20)
    options_button2.config(text = questions[question_index]["options"][1], value = 2 , font = ("Ariel" , 16 , "bold") , fg = "grey")
    options_button2.pack(pady = 20)
    options_button3.config(text = questions[question_index]["options"][2], value = 3 , font = ("Ariel" , 16 , "bold") , fg = "grey")
    options_button3.pack(pady = 20)
    options_button4.config(text = questions[question_index]["options"][3], value = 4 , font = ("Ariel" , 16 , "bold") , fg = "grey")
    options_button4.pack()

    button.pack(pady=40 )  # Also move this here so Submit button appears only after quiz starts

    label.pack_forget()
    btn_cs.pack_forget()
    btn_gk.pack_forget()
    btn_his.pack_forget()
    btn_math.pack_forget()
    label3.pack_forget()

def next_section():
    global current_section , question_index , section_end
    #clear screen
    for widget in window.winfo_children():
        widget.pack_forget()

    #section title 
    section_names = ["Computer Science", "General Knowledge", "Maths", "History", "Science"]
    section_label = tk.Label(window , text = f" Section {current_section+1}  :  {section_names[current_section]} ", font=("Arial", 26 , "bold"), fg="purple" )
    section_label.pack(pady=20, anchor="center")

    #button to actually load question
    global start_btn 
    start_btn = tk.Button(window , text = "Start Section" , font=("Arial", 14, "bold"), command= load_question)
    start_btn.pack(pady=20, anchor="center")


def submit_answer():
    global question_index
    global score , next_btn , section_end

    if selected_option.get() == 0:   # user didn’t choose
        label3.config(text="⚠ Please select an option", fg="orange")
        return
    
    if selected_option.get() == questions[question_index]["answer"]:
        label3.config(text = "Correct answer ✅" , fg = "green")
        label3.pack(pady=10) 
        score += 1
    else:
        label3.config(text = "Wrong answer ❌" , fg = "red")
        label3.pack(pady=10) 
        score -= 0.25
    

    question_index += 1
   
    # If there are still questions left in this section, load the next one
    if question_index < section_end:
        window.after(1000, load_question)  # wait before next Q
        return

    # --- Section finished ---
    if question_index == section_end:
        question_label.pack_forget()
        options_button.pack_forget()
        options_button2.pack_forget()
        options_button3.pack_forget()
        options_button4.pack_forget()
        button.pack_forget()

        # All sections done?
        if section_end >= len(questions):  
            for widget in window.winfo_children():
                widget.destroy()

            # Calculate grade
            percentage = (score / len(questions)) * 100
            if percentage >= 90:
                grade = "A+"
            elif percentage >= 75:
                grade = "A"
            elif percentage >= 60:
                grade = "B"
            elif percentage >= 50:
                grade = "C"
            else:
                grade = "F"

            # Pass/Fail
            status = "Pass ✅" if percentage >= 50 else "Fail ❌"

            final_label = tk.Label(
                window,
                text=f"🎉 Quiz completed!\n\nFinal Score: {score}/{len(questions)}"
                     f"\nPercentage: {percentage:.2f}%"
                     f"\nGrade: {grade}"
                     f"\nStatus: {status}",
                font=("Arial", 18, "bold"),
                fg="blue",
                justify="center"
            )
            final_label.pack(pady=20, anchor="center", expand=True)
            return

        # Otherwise, show next-section button
        label3.config(text=f"✅ Section completed! Current score: {score}", fg="blue")
        label3.pack(pady=10)
        next_btn = tk.Button(window, text="Next section →", font=("Ariel", 16, "bold"), fg="purple",
                             command=lambda: start_section(section_end))
        next_btn.pack(pady=20)


button = tk.Button(window , text = "Submit answer" , command = submit_answer , font=("Ariel", 14, "bold"), bg = "lightgrey")


window.mainloop()
