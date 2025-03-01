'''
Python does not have a built-in do-while loop, but you can simulate it using a while loop. Here's how you can create a similar construct in Python:
'''

count = 0

while True:
    print("Count is:", count)
    count = count + 1

    if not (count < 5):
        break