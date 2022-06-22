import time

# Normal: 1, 2, 3, 4
# Hard: 2, 4, 6, 8

'''
def diffSel():
    mode_selected = False
    diff = [0,0,0,0]
    while mode_selected == False:
        print("Select difficulty (normal/hard)")
        mode_input = input()
        if mode_input == "normal":
            mode_selected = True
            difficulty1, difficulty2, difficulty3, difficulty4 = [1, 2, 3, 4]
            diffNums = [difficulty1, difficulty2, difficulty3, difficulty4]
            diff = diffNums
            return diff

        elif mode_input == "hard":
            mode_selected = True
            difficulty1, difficulty2, difficulty3, difficulty4 = [2, 4, 6, 8]
            diffNums = [difficulty1,difficulty2,difficulty3,difficulty4]
            diff = diffNums
            return diff
            # print(difficulty1, difficulty2, difficulty3, difficulty4)

        else:
                print("Input not accepted, please enter 'normal' or 'hard'")


# diff = [difficulty1,difficulty2,difficulty3,difficulty4]
diffSel()
print(diff)
'''

def diffSel():
    mode = ("normal", "hard")
    mode_input = input()
    while mode_input not in mode:
        print("Input not accepted, please enter 'normal' or 'hard'")
        mode_input = input()
        if mode_input in mode:
            break
    if mode_input == 'normal':
        print("Mode selected: Bitch mode")
        levels = [1,2,3,4]
        diffLevels = levels
        time.sleep(0.5)
        return diffLevels
    if mode_input == 'hard':
        print("Mode selected: Real muhfucka mode")
        levels = [2,4,6,8]
        diffLevels = levels
        time.sleep(0.5)
        return diffLevels

print("Please select difficulty (normal/hard)")
diffLevels = diffSel()
# print(mode_input)
#    while mode_selected == True:
#        if mode_input == 'normal'
