import tkinter as tk
import time

#----------VARIABLE DECLARATIONS----------

root = tk.Tk()

# 2D array for the 5x5 tile layout
tiles = []
for i in range(5):
    tiles.append([0, 0, 0, 0, 0])

# total number of possible layouts
totalLayouts = 0

# number of chosen animals
numOfAnimals = 0
# name of the chosen location to choose animals from
locationName = 'filler'
# possible animals to choose from
animalOptions = []
# holds info on the chosen animals
selectedAnimals = []

# the time that the last root.after is set to occur
lastSetAfter = 0
# causes displayTiles_a() to run differently the first time it runs
firstSetOfAfters = True

#----------CLASS DECLARATIONS-----------

class patterns:
    class farm:
        sheep = [[1, 1, 1, 1]]
        pig = [[1, 1], [1, 1]]
        rabbit = [[1], [1], [1], [1]]
        horse = [[1], [1], [1]]
        cow = [[1, 1, 1]]
        unicorn = [[1, 0, 0], [0, 1, 1]]
    class outback:
        kangaroo = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        platypus = [[1, 1, 0], [0, 1, 1]]
        crocodile = [[1, 1, 1, 1]]
        koala = [[1, 1], [0, 1]]
        cockatoo = [[1, 0], [0, 1], [0, 1]]
        tiddalik = [[0, 1, 0], [1, 0, 1]]
    class savanna:
        zebra = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
        hippo = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        giraffe = [[1], [1], [1], [1]]
        lion = [[1, 1, 1]]
        elephant = [[1, 1], [1, 0]]
        gryphon = [[1, 0, 1], [0, 1, 0]]
    class northern:
        bear = [[1, 1], [0, 1], [0, 1]]
        skunk = [[0, 1, 1], [1, 1, 0]]
        beaver = [[0, 0, 1], [1, 1, 0], [0, 0, 1]]
        moose = [[1, 0, 1], [0, 1, 0]]
        fox = [[1, 1, 0], [0, 0, 1]]
        sasquatch = [[1], [1]]
    class polar:
        penguin = [[0, 1, 0], [0, 1, 0], [1, 0, 1]]
        seal = [[1, 0, 0, 0], [0, 1, 0, 1], [0, 0, 1, 0]]
        muskox = [[1, 1, 0], [1, 0, 1]]
        polar_bear = [[1, 0, 1], [0, 0, 1]]
        walrus = [[1, 0, 0], [0, 1, 1]]
        yeti = [[1], [0], [1]]
    class jungle:
        monkey = [[1, 0, 1, 0], [0, 1, 0, 1]]
        toucan = [[0, 1], [1, 0], [0, 1], [0, 1]]
        gorilla = [[1, 0, 1], [1, 0, 1]]
        panda = [[0, 0, 1], [1, 0, 0], [0, 0, 1]]
        tiger = [[1, 0, 1, 1]]
        phoenix = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
    class jurassic:
        diplodocus = [[1, 0, 0], [0, 1, 1], [0, 1, 0]]
        stegosaurus = [[0, 1, 1, 0], [1, 0, 0, 1]]
        raptor = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]
        t_rex = [[1, 0], [0, 0], [1, 1]]
        triceraptops = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
        dragon = [[1, 0, 0], [0, 0, 1]]
    class ice_age:
        wooly_rhino = [[0, 0, 1, 0], [1, 0, 0, 1], [0, 1, 0, 0]]
        giant_sloth = [[1, 0, 0], [0, 0, 1], [1, 0, 1]]
        dire_wolf = [[0, 1, 0, 0], [1, 0, 0, 1], [0, 1, 0, 0]]
        saber_tooth = [[1, 0, 0], [0, 0, 1], [0, 1, 0]]
        mammoth = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
        akhlut = [[0, 0, 1], [1, 0, 0], [0, 0, 1]]
    class city:
        raccoon = [[1, 0, 1, 0], [1, 0, 0, 1]]
        pigeon = [[1, 0, 0], [0, 1, 0], [0, 1, 1]]
        rat = [[1, 1, 0, 0], [0, 1, 0, 1]]
        squirrel = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
        opossum = [[1, 0, 0], [1, 0, 1]]
        sewer_turtle = [[1, 1]]
    class moon:
        moonkey = [[1, 0, 0], [1, 0, 1], [0, 0, 1]]
        lunar_tick = [[0, 1, 0], [0, 0, 0], [0, 1, 0], [1, 0, 1]]
        tribble = [[0, 1, 0], [1, 1, 1]]
        moonicorn = [[1, 0], [1, 1]]
        luna_moth = [[1, 0, 1], [0, 0, 0], [0, 1, 0]]
        jade_rabbit = [[1, 0], [0, 0], [0, 1]]
    class mountain:
        goat = [[1, 0, 0], [1, 1, 1]]
        cougar = [[1, 0, 0], [0, 1, 0], [1, 0, 1]]
        elk = [[1, 0, 1], [0, 1, 1]]
        eagle = [[1, 0], [1, 0], [0, 1]]
        coyote = [[1, 1, 0], [0, 0, 1]]
        aatxe = [[0, 0, 1], [1, 0, 0]]
    class mars:
        rock = [[1, 1], [1, 1]]
        marsmot = [[0, 1], [0, 1], [1, 1]]
        marsmoset = [[1, 0, 1], [0, 0, 1], [0, 1, 0]]
        rover = [[0, 1, 0], [1, 0, 1]]
        martian = [[1, 0, 1], [0, 1, 0]]
        marsmallow = [[1], [0], [1]]


class buttons:
    def newChosenAnimal(animalNum):
        global selectedAnimals, animalOptions
        selectedAnimals.append(animalOptions[animalNum])
        del animalOptions[animalNum]

    class phases:
        # ask how many animals will be chosen
        def phase1():
            clearScreen()

            label_askNumOfAnimals = tk.Label(root, text = 'How many animals are\nyou going to chose?')
            label_askNumOfAnimals.grid(row=0, column=0, columnspan=3)
            
            for n in range(1, 4):
                tk.Button(root, text=n, command = lambda x=n:buttons.phases.phase2(x)).grid(row = 1, column = n-1, sticky='nesw')

        # ask for the location
        def phase2(numAnimals):
            global numOfAnimals
            numOfAnimals = numAnimals

            clearScreen()

            label_askLocation = tk.Label(root, text = 'What location do you want to choose animals from?')
            label_askLocation.grid(row=0, column=0, columnspan=4)

            locations = ['Farm', 'Outback', 'Savanna', 'Northern', 'Polar', 'Jungle', 'Jurassic', 'Ice Age', 'City', 'Moon', 'Mountain', 'Mars']
            # runs for every location in locations
            for i in range(len(locations)):
                location = locations[i]
                tk.Button(root, text = location, width=7, height=1, command = lambda l=location:buttons.phases.phase3a(l)).grid(row=int(i/4)+1, column=i%4, sticky='nesw')

        # ask for chosen animal 1
        def phase3a(location):
            global locationName, animalOptions
            
            clearScreen()

            locationName = location.lower().replace(' ', '_')

            animalOptions = calcAnimalOptions(locationName)
            
            label_askLocation = tk.Label(root, text = 'What is animal #1')
            label_askLocation.grid(row=0, column=0)

            animalButtons = []
            for i in range(len(animalOptions)):
                animalButtons.append(tk.Button(root, text = animalOptions[i], command = lambda x=i:[buttons.newChosenAnimal(x), buttons.phases.phase3b()]).grid(row = i+1, column = 0, sticky='nesw'))
        
        # ask for chosen animal 2, if there is one
        def phase3b():
            global animalOptions
            
            if numOfAnimals >= 2:
                clearScreen()

                label_askLocation = tk.Label(root, text = 'What is animal #2')
                label_askLocation.grid(row=0, column=0)

                animalButtons = []
                for i in range(len(animalOptions)):
                    animalButtons.append(tk.Button(root, text = animalOptions[i], command = lambda x=i:[buttons.newChosenAnimal(x), buttons.phases.phase3c()]).grid(row = i+1, column = 0, sticky='nesw'))
            else:
                buttons.phases.phase3c()
        
        # ask for chosen animal 3, if there is one
        def phase3c():
            global animalOptions
            
            if numOfAnimals >= 3:
                clearScreen()

                label_askLocation = tk.Label(root, text = 'What is animal #3')
                label_askLocation.grid(row=0, column=0)

                animalButtons = []
                for i in range(len(animalOptions)):
                    animalButtons.append(tk.Button(root, text = animalOptions[i], command = lambda x=i:[buttons.newChosenAnimal(x), buttons.phases.phase4()]).grid(row = i+1, column = 0, sticky='nesw'))
            else:
                buttons.phases.phase4()
        
        # calculate and diplay total possible layouts
        def phase4():
            global totalLayouts, arraysToDisplay

            clearScreen()

            addPatternsToSA()

            # makes a 3d array of layouts for tiles and the first animal
            tiles1 = calcLayouts(tiles, selectedAnimals[0][1])
            # runs if theres more than 1 animal
            if len(selectedAnimals) > 1:
                # runs for every layout in tiles1
                for i in range(len(tiles1)):
                    # makes a 3d array of layouts for tiles1[i] and the second animal
                    tiles2 = calcLayouts(tiles1[i], selectedAnimals[1][1])
                    # runs for every layout in tiles2
                    for j in range(len(tiles2)):
                        # runs if theres more than 2 animals
                        if len(selectedAnimals) > 2:
                            # makes a 3d array of layouts for tiles2[j] and the third animal
                            tiles3 = calcLayouts(tiles2[j], selectedAnimals[2][1])
                            # runs for every layout in tiles3
                            for k in range(len(tiles3)):
                                # runs if tiles3[k] is a valid layout
                                if checkForValidLayout(tiles3[k]):
                                    totalLayouts += 1
                            displayTiles_a(tiles3)
                        elif checkForValidLayout(tiles2[j]):
                            totalLayouts += 1
                    if len(selectedAnimals) == 2:
                        displayTiles_a(tiles2)
            else:
                totalLayouts += len(tiles1)
                displayTiles_a(tiles1)


#----------FUNCTIONS----------

# returns a list of all the animal names from the location sent to it
def calcAnimalOptions(location):
    switcher = {
        'farm':['sheep', 'pig', 'rabbit', 'horse', 'cow', 'unicorn'],
        'outback':['kangaroo', 'platypus', 'crocodile', 'koala', 'cockatoo', 'tiddalik'],
        'savanna':['zebra', 'hippo', 'giraffe', 'lion', 'elephant', 'gryphon'],
        'northern':['bear', 'skunk', 'beaver', 'moose', 'fox', 'sasquatch'],
        'polar':['penguin', 'seal', 'muskox', 'polar bear', 'walrus', 'yeti'],
        'jungle':['monkey', 'toucan', 'gorilla', 'panda', 'tiger', 'phoenix'],
        'jurassic':['diplodocus', 'stegosaurus', 'raptor', 't-rex', 'triceraptops', 'dragon'],
        'ice_age':['wooly rhino', 'giant sloth', 'dire wolf', 'saber tooth', 'mammoth', 'akhlut'],
        'city':['raccoon', 'pigeon', 'rat', 'squirrel', 'opossum', 'sewer turtle'],
        'moon':['lunar tick', 'moonkey', 'tribble', 'luna moth', 'moonicorn', 'jade rabbit'],
        'mountain':['goat', 'cougar', 'elk', 'eagle', 'coyote', 'aatxe'],
        'mars':['rock', 'marsmot', 'marsmoset', 'rover', 'martian', 'marsmallow']
    }

    return switcher[location]


# add patterns to selectedAnimals
def addPatternsToSA():
    global selectedAnimals

    for i in range(len(selectedAnimals)):
        animalName = selectedAnimals[i]
        selectedAnimals[i] = [animalName, getattr(eval('patterns.'+locationName), animalName.replace(' ', '_').replace('-', '_'))]


# returns a list of all the layouts that can be made with the sent layout and animal pattern
def calcLayouts(layout1, animalPat):
    newArray = []
    for y in range(6 - len(animalPat)):
        for x in range (6 - len(animalPat[0])):
            newArray.append(combineArrays(layout1, animalPat, (x, y)))
    return newArray


# combines 2 2d arrays with an offset
def combineArrays(baseArray, arrayToAdd, offset = (0, 0)):
    array1 = baseArray.copy()
    array2 = arrayToAdd.copy()

    offX = offset[1]
    offY = offset[0]

    newArray = []
    for i in range(len(array1)):
        newArray.append(array1[i].copy())

    for i in range(len(array2)):
        for j in range(len(array2[0])):
            newArray[i+offX][j+offY] = array1[i+offX][j+offY] + array2[i][j]

    return newArray


# returns True or False depending on if the sent layout is valid
def checkForValidLayout(layout):
    possibleLayout = True

    for i in range(5):
        for j in range(5):
            if layout[i][j] > 1:
                possibleLayout = False

    if possibleLayout:
        return True
    else:
        return False


# clears the Tkinter window of all widgets
def clearScreen():
    widget_list = root.winfo_children()

    for item in widget_list :
        if item.winfo_children() :
            widget_list.extend(item.winfo_children())
    
    for item in widget_list:
        item.grid_remove()


# creates "afters" which will display layouts between intervals
def displayTiles_a(arrayOfLayouts):
    global lastSetAfter, firstSetOfAfters

    # runs if this is the first time displayTiles_a has ran
    if firstSetOfAfters:
        # makes sure that this if statement won't run again
        firstSetOfAfters = False
        # sets lastSetAfter to the current time (plus some) since no afters have been set
        lastSetAfter = time.time() + 1

        clearScreen()
        calculatingLabel = tk.Button(root, text='Calculating layouts...').grid(row=0, column=0)
    
    # interval between the afters, in miliseconds
    timeBetweenAfters = 250

    # how long untill the last set after is set to occur
    secondsUntillLastAfter = lastSetAfter - time.time()

    # runs for every layout in arrayOfLayouts
    for i in range(len(arrayOfLayouts)):
        # the amount of time the after is set to occur after
        timeUntillRun = i * timeBetweenAfters + int(round(secondsUntillLastAfter, 3) * 1000)

        # displays a layout after timeUntillRun miliseconds
        root.after(timeUntillRun, lambda layout=arrayOfLayouts[i]:displayTiles_b(layout))

        # the time that the last set after will occur
        lastSetAfter = time.time() + (timeUntillRun / 1000) + (timeBetweenAfters / 1000)


# clears the screen then displays the sent layout and the total number of layouts
def displayTiles_b(layout):
    clearScreen()

    if len(selectedAnimals) == 1:
        layoutsMsg = 'There are {} total valid layouts\nwith the animal {}.'.format(totalLayouts, selectedAnimals[0][0])
    elif len(selectedAnimals) == 2:
        layoutsMsg = 'There are {} total valid layouts with\nthe animals {} and {}.'.format(totalLayouts, selectedAnimals[0][0], selectedAnimals[1][0])
    else:
        layoutsMsg = 'There are {} total valid layouts with the\nanimals {}, {}, and {}.'.format(totalLayouts, selectedAnimals[0][0], selectedAnimals[1][0], selectedAnimals[2][0])
    tk.Label(root, text=layoutsMsg).grid(row=0, column=0)
    tk.Label(root, text='Now displaying all the layouts.').grid(row=1, column=0)

    # runs for every row in the layout
    for x in range(len(layout)):
        # runs for every tile in the row
        for y in range(len(layout)):
            # runs if the tile's value is 0
            if layout[y][x] == 0:
                # displays a blank, square, button to represent the tile
                tk.Button(root, state=tk.DISABLED, height=3, width=6).grid(row=y, column=x+1)
            # runs if the tile's value is 1
            elif layout[y][x] == 1:
                # displays a green, square, button to represent the tile
                tk.Button(root, state=tk.DISABLED, height=3, width=6, bg='green').grid(row=y, column=x+1)
            # runs if the tile's value is 2 or greater
            elif layout[y][x] >= 2:
                # displays a red, square, button to represent the tile
                tk.Button(root, state=tk.DISABLED, height=3, width=6, bg='red').grid(row=y, column=x+1)


#----------THE MAIN STUFF----------

if __name__ == "__main__":
    root.title('Disco Zoo Layouts')

    button_start = tk.Button(root, text = 'start', command = buttons.phases.phase1)
    button_start.grid(row=0, column=0)

    root.mainloop()
