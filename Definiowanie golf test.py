
def determine_golf_performance():
    par = int(input('What par was the hole?\n'))
    strokes = int(input('How many strokes did you use?\n'))

    if par-3 == strokes:
        print('Albatross')
    elif par-2 == strokes:
        print('Eagle')
    elif par-1 == strokes:
        print('Birdie')
    elif par == strokes:
        print('Par')
    elif par+1 == strokes:
        print('Bogey')
    elif par+2 == strokes:
        print('Double Bogey')
    elif par+3 == strokes:
        print('Triple Bogey')
    else:
        print('I don\'t know? Please try again.')
        print(">> Use this tool to give you feedback on how you golfed")
hole = 1
while hole <= 18:
    print(">> Hole", hole, "performance")
    determine_golf_performance()
    hole += 1
