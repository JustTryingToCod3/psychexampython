class Question:
    def __init__(self, prompt, correct_answer):
        self.prompt = prompt
        self.correct_answer = correct_answer

    def check_answer(self, user_input):
        return user_input.strip().lower() == self.correct_answer.lower()

def run_exam(questions):
    while True:
        your_score = 0
        total_score = len(questions)

        for q in questions:
            answer = input(q.prompt + "\nYour answer: ")
            if q.check_answer(answer):
                print("✅ Correct")
                your_score += 1
            elif answer.strip().lower() == "0":  # Assuming you want to break if the answer is 0
                break
            else:
                print("❌ Incorrect")
                print(f"The correct answer was: {q.correct_answer.upper()}")

        percentage = (your_score / total_score) * 100
        grade = handle_grades(percentage)

        print(" ")
        print(f"\nYour Score: {your_score}/{total_score} ({percentage:.2f}%)")
        print(f"Your Letter Grade: {grade}")
        print(" ")

        # Ask to retake the quiz
        again = input("\nWould you like to retake the exam or continue? Press y to retake and n to continue? (y/n): ").strip().lower()
        print(" ")
        if again != "y":
            print("Thank you for taking the exam! Good luck with your studies 😊")
            break

def handle_grades(percentage):
        if percentage >= 90: return "A, you earned a Diamond"
        elif percentage >= 80: return "B you found a four leaf clover"
        elif percentage >= 70: return "C you tripped over a rock, don't worry, no one saw"
        elif percentage >= 60: return "D congrats on showing up.. at least..."
        return "F... no words here.... Start over"

# Part 1 – questionpt1
neuro1 = [
    Question("What is the primary difference between sensation and perception?\na. Sensation is the brain’s interpretation of stimuli; perception is the detection of stimuli\nb. Sensation is the detection of stimuli; perception is the brain’s interpretation", "b"),
    Question("What do sensory receptors do in the sensory process?\na. Transmit chemical signals to muscles\nb. Transduce physical energy into electrical signals", "b"),
    Question("What does high receptor density in an area (e.g., fingertips or fovea) indicate?\na. Greater sensitivity and fine discrimination\nb. Decreased sensory acuity and reduced resolution", "a"),
    Question("How is sensory input primarily represented in the brain?\na. Through emotion centers\nb. Through topographic maps in sensory cortex", "b"),
    Question("Which of the following best explains perceptual illusions?\na. Failures of sensation due to receptor fatigue\nb. The brain actively constructs perception, sometimes inaccurately", "b"),
]

# Part 2 – questionpt2
neuro2 = [
    Question("Which part of the eye contains the most densely packed cones and is responsible for sharp vision?\na. Optic disc\nb. Fovea", "b"),
    Question("Which photoreceptors are primarily responsible for color vision and function best in bright light?\na. Rods\nb. Cones", "b"),
    Question("What is the correct pathway of visual information from the eye to the brain?\na. Photoreceptors → Bipolar cells → Ganglion cells → Optic nerve\nb. Ganglion cells → Bipolar cells → Photoreceptors → Optic nerve", "a"),
    Question("Which brain structure is the first major relay for visual information from the optic tract?\na. Superior colliculus\nb. Lateral geniculate nucleus (LGN)", "b"),
    Question("What does the striate cortex (V1) primarily do?\na. Interpret sound frequency\nb. Maintain a topographic map of the visual field", "b"),
]

# Part 3 – questionpt3
neuro3 = [
    Question("What is the main function of the dorsal visual stream?\na. Object recognition and color perception\nb. Processing motion and spatial location", "b"),
    Question("Damage to the ventral stream can result in which condition?\na. Optic ataxia\nb. Prosopagnosia", "b"),
    Question("What does the trichromatic theory of color vision propose?\na. Opposing color channels determine color perception\nb. Three cone types (red, green, blue) account for color vision", "b"),
    Question("What does the opponent-process theory of color vision explain?\na. Cone responses in the retina only\nb. Opponent color channels and afterimages", "b"),
    Question("What does tonotopic organization in the auditory cortex mean?\na. Sound frequencies are mapped to specific locations\nb. Sounds are processed by visual pathways", "a"),
]

# Part 4 – questionpt4
neuro4 = [
    Question("Which hemisphere typically processes speech and language?\na. Left hemisphere\nb. Right hemisphere", "a"),
    Question("What is the function of Broca’s area?\na. Language comprehension\nb. Speech production", "b"),
    Question("What area is primarily responsible for language comprehension?\na. Wernicke’s area\nb. Fusiform face area", "a"),
    Question("What is a receptive field in sensory systems?\na. The entire sensory organ\nb. The specific area a sensory neuron responds to", "b"),
    Question("What do topographic maps in the sensory cortex represent?\na. Emotional valence of stimuli\nb. Spatial arrangement of sensory input", "b"),
]

# Part 5 – questionpt5
neuro5 = [
    Question("Which area of the brain is involved in facial recognition?\na. Fusiform face area (FFA)\nb. Parahippocampal place area (PPA)", "a"),
    Question("Which visual stream processes the 'what' of visual information?\na. Dorsal stream\nb. Ventral stream", "b"),
    Question("What is the function of the anterior intraparietal area (AIP)?\na. Object recognition\nb. Visual control of grasping", "b"),
    Question("Which visual pathway contributes to circadian rhythms?\na. Hypothalamic tract\nb. Geniculostriate system", "a"),
    Question("Which cortical region first receives visual input from the LGN?\na. Primary visual cortex (V1)\nb. Parietal lobe", "a"),
]



print("Welcome to your exam")
name = input("Enter Your Name: ")
classroom = input("Enter your class: ")
print("Hello " + name + " you are about to take a course for " + classroom)
print(" ")

while True:
  choices = input("This 25-question exam is split up into 5 parts. Which part would you like to take? 1,2,3,4,5? Press 0 to Exit" )
  print(" ")
  if choices == "1":
      run_exam(neuro1)
  elif choices == "2":
      run_exam(neuro2)
  elif choices == "3":
      run_exam(neuro3)
  elif choices == "4":
      run_exam(neuro4)
  elif choices == "5":
      run_exam(neuro5)
  elif choices == "0":
    break
  else:
    print("Improper input, please try again")
    print(" ")
