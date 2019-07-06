import csv
import random
from os import system
from time import sleep

def row_count(filename):
    with open(filename) as in_file:
        return sum(1 for _ in in_file)

def main():
    filename = 'vocab/JadenVocab.csv'
    last_line_number = row_count(filename)
        # print(last_line_number)

    with open(filename) as csv_file:
        
        ans = random.randint(1,last_line_number)
        samples = random.sample(range(1,last_line_number),5)
        if not(ans in samples):
            # answer is not in the sample, so replace one sample with answer
            samples[random.randint(0,4)] = ans

        system('clear') # clear screen
        print(samples)
        print(ans)

        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader) # skip header row
        
        line_number = 0
        sample_number = 1
        # first pass to get the answer word, and definition
        for row in csv_reader:
            line_number += 1
            if line_number == ans:
                ans_word = row[0]
                ans_definition = row[1]
            
        print(f"What is the definition of \'{ans_word}\'?")
        print('\n')        
        
        csv_file.seek(0) #go back to top of the file
        next(csv_reader) # skip header row

        # print answer choices        
        line_number = 0
        sample_number = 1
        samples_to_answers = dict()
        for row in csv_reader:
            line_number += 1
            if line_number in samples:
                print(f"{sample_number}. {row[1]}")
                samples_to_answers[str(sample_number)] = line_number
                sample_number += 1
        
        print("\n")
        print(samples_to_answers)
        print("\n")
        
        choice = input("Choose your answer: ")
        if samples_to_answers[choice] == ans:
            print("Correct!")
        else:
            print("Wrong!!!")

main()
keep_running = True
while keep_running:
    print("\n")
    to_continue = input("Type \'y\' to continue, \'n\' to exit: (default=y) ")
    if to_continue == 'n':
        print("Good Bye!")
        keep_running = False
    else:
        main()
        


    