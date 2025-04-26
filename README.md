# project
six lines


FILE TO RUN: gui.py
The project is a simple divination app for based on the Six Lines (Liu Yao) method from the I Ching (Book of Changes)

 Six Lines is an ancient Chinese divination method that consists of six lines, which can be either yin(———— ————) (or yang(——————————). These six lines are divided into two groups, with each group corresponding to one of the trigrams from the Eight Trigrams (Ba Gua).

 
 HOW IT WORKS, BASICS
 - users are prompted to input 3 three-digit numbers into the gui
 - the numbers determine:
    - the upper trigram (first number, modulo 8)
    - the lower trigram (second number, modulo 8)
    - the changing line (third number, modulo 6)
- based on the combination, a hexagram and an interpretation will be generated froma  pre-translated database containing the 64 possible outcomes

GENERATING THE NUMBERS
- the user can choose the numbers and type them in themselves
- the user can generate the numbers (all three inputs) using a simple random number generator
- the user can generate the numbers randomly by using the built-in turtle graphic simulator
    - the turtle moves randomly until the user presses SPACE to stop it
    - the longer the user lets the turtle wander, the bigger the number generated will be
    - this was added to provide a more interactive way of generating the numbers

FILES
- gui.py : the main graphic interface, this is the file that should be run
- core.py: contains the logic for calculating the trigrams, changing lines, and the results
- hexagrams.py - the database of the hexagram interpretations
- turtle_num_generator.py : the animated turtle number generator graphic
- main.py : the first, text-based version created for testing
- README.md : project description

During the coding phase, the user will be prompted to input three three-digit numbers. After the input is completed, the first and second three-digit numbers will be divided by 8, and the third number will be divided by 6. The remainder of each division will then be taken. In traditional Six Lines (Liu Yao) divination, the numbers 1 to 8 correspond to one of the trigrams (each composed of three lines). The remainder of the first number will determine the upper half of the Six Lines, while the remainder of the second number will determine the lower half. The remainder of the third number will serve as the "changing line," which modifies the 6-lines formed by the first two remainders. For example, if the remainder of the third number is 1, the bottom line of the hexagram will change (if it is a yin line, it will become a yang line, and vice versa). If the third remainder is 2, the second line from the bottom will change, and so on. 



JOB DISTRIBUTION:
Qifei – Source code, base logic, and part of app design
Emilia – app design, GUI design, turtle graphics, organization
