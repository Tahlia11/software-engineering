import time
def animateText(text):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(0.1)
animateText('Hello world')