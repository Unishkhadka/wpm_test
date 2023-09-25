from essential_generators import DocumentGenerator
import string
import time
import math

def sentence():
    gen = DocumentGenerator()
    sentence=gen.sentence()
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    print(sentence.lower())

def write():
    start_time = time.time()
    input_text = input("--->")
    end_time = time.time()
    time_taken = end_time - start_time
    total_words = len(input_text.split())
 # Calculate typing speed in words per minute (WPM)
    wpm = (total_words / time_taken) * 60
    wpm = math.floor(wpm)
    print(f"Your wpm is {wpm}")

sentence()
write()
