"""
File Name: IntegratedFunctionSystems.py
Project: Integrated Function Systems
Made By: Ethan Leifer
Orginal Dependences: DEgraphics.py
"""

# imports
from ELDEgraphics import *
from math import cos, sin, radians
from random import randrange, random
from tkinter import colorchooser

transformations = []
probTransformations = []

win = DEGraphWin(defCoords=[-.1, -.1, 1.1, 1.1])
gui = DEGraphWin(title='GUI', width=600, height=600, offsets=[win.width, 0], defCoords=[0, 0, 10, 9], hBGColor='black')
gui.displayGrid()

# font used on gui's
FONT = 'helvetica'

# to manage the activating and deactivating of buttons
buttonsActive = False

# title text object
txtTitle = Text(Point(5, 8.5), "Integrated Function Systems Explorer")
txtTitle.setFace(FONT)
txtTitle.setSize(30)
txtTitle.draw(gui)

# buttons
btnExit = SimpleButton(win=gui, topLeft=Point(.1, .9), width=3.8, height=.8, label='EXIT', font=(FONT, 35),
                       buttonColor='red', )
btnDraw = SimpleButton(win=gui, topLeft=Point(4.1, .9), width=1.8, height=.8, label="DRAW", font=(FONT, 25),
                       buttonColor='blue', textColor='white')
btnClear = SimpleButton(win=gui, topLeft=Point(6.1, .9), width=1.8, height=.8, label="CLEAR", font=(FONT, 25),
                        buttonColor='blue', textColor='white')
btnZoomIn = SimpleButton(win=gui, topLeft=Point(2.1, 2.9), width=1.8, height=.8, label="ZOOM\nIN", font=(FONT, 20),
                         buttonColor='blue', textColor='white')
btnZoomOut = SimpleButton(win=gui, topLeft=Point(4.1, 2.9), width=1.8, height=.8, label="ZOOM\nOUT", font=(FONT, 20),
                          buttonColor='blue', textColor='white')
btnDeleteAll = SimpleButton(win=gui, topLeft=Point(8.1, .9), width=1.8, height=.8, label="DELETE\nALL", font=(FONT, 20),
                            buttonColor='blue', textColor='white')
btnConfirmChanges = SimpleButton(win=gui, topLeft=Point(4.1, 1.9), width=1.8, height=.8, label="CONFIRM\nEDITS",
                                 font=(FONT, 20),
                                 buttonColor='blue', textColor='white')
btnDeleteSelected = SimpleButton(win=gui, topLeft=Point(6.1, 1.9), width=1.8, height=.8,
                                 label="DELETE\nSELECTED", font=(FONT, 20),
                                 buttonColor='blue', textColor='white')
btnAddNew = SimpleButton(win=gui, topLeft=Point(8.1, 1.9), width=1.8, height=.8, label="ADD\nENTERED", font=(FONT, 19),
                         buttonColor='blue', textColor='white')
btnKochCurve = SimpleButton(win=gui, topLeft=Point(.1, 1.9), width=1.8, height=.8, label="KOCH\nCURVE",
                               font=(FONT, 20),
                               buttonColor='blue', textColor='white')
btnInfinity = SimpleButton(win=gui, topLeft=Point(2.1, 1.9), width=1.8, height=.8, label="INFINITY\nTHING",
                               font=(FONT, 20),
                               buttonColor='blue', textColor='white')

btnTwoToned = SimpleButton(win=gui, topLeft=Point(4.1, 3.9), width=.8, height=.8, label="SAME\nFORE\nROUND", font=(FONT, 10),
                           buttonColor='blue', textColor='white')

btnForeground = SimpleButton(win=gui, topLeft=Point(5.1, 3.9), width=.8, height=.8, label="", font=(FONT, 20),
                             buttonColor='Black', textColor='white')

btnTransformationColor = SimpleButton(win=gui, topLeft=Point(2.1, 3.9), width=.8, height=.8, label=" ", font=(FONT, 18),
                                      buttonColor='black', textColor='white')
btnTransformationColorSelection = SimpleButton(win=gui, topLeft=Point(3.1, 3.9), width=.8, height=.8,
                                               label="Transform\nColor", font=(FONT, 9),
                                               buttonColor='Blue', textColor='white')

# Initialize Dropdown menu
DROPDOWNWIDTH = 60
DROPDOWNPOINT = Point(6, 7.77)
drpTransformationSelection = DropDown(DROPDOWNPOINT, choices=[" "], width=DROPDOWNWIDTH, font=(FONT, 12))
drpTransformationSelection.draw(gui)
btnConfirmTransformation = SimpleButton(win=gui, topLeft=Point(3, 7.48), width=6, height=.4,
                                        label="Click to edit Transformation", font=(FONT, 12), buttonColor="blue",
                                        textColor="white")

# Transient Iterations entry
transientIterations = 1000

entTransientIterations = IntEntry(Point(7, 3.25), width=10, span=[0, 100000])
entTransientIterations.draw(gui)
entTransientIterations.setFace(FONT)
btnEnterTransientIterations = SimpleButton(gui, topLeft=Point(8.1, 3.45), width=1.8, height=.4, label="Enter",
                                           font=(FONT, 15),
                                           buttonColor='blue', textColor='white')
txtTransientIterations = Text(Point(8, 3.75), "# of Transient Iterations = ")
txtTransientIterations.setFace(FONT)
txtTransientIterations.draw(gui)

# Drawing Iterations entry
drawingIterations = 10000

entDrawingIterations = IntEntry(Point(7, 2.25), width=10, span=[0, 1000000])
entDrawingIterations.draw(gui)
entDrawingIterations.setFace(FONT)
btnEnterDrawingIterations = SimpleButton(gui, topLeft=Point(8.1, 2.45), width=1.8, height=.4, label="Enter",
                                         font=(FONT, 15),
                                         buttonColor='blue', textColor='white')
txtDrawingIterations = Text(Point(8, 2.75), "# of Drawing Iterations = ")
txtDrawingIterations.setFace(FONT)
txtDrawingIterations.draw(gui)

# Probability Weight entry
entProbabilityWeight = IntEntry(Point(1, 2.25), width=10, span=[0, 100])
entProbabilityWeight.draw(gui)
entProbabilityWeight.setFace(FONT)

txtProbabilityWeight = Text(Point(1, 2.75), "Probability Weight:")
txtProbabilityWeight.setFace(FONT)
txtProbabilityWeight.draw(gui)

# Vertical Shift entry
entVerticalShift = DblEntry(Point(1, 3.25), width=10, span=[0, 1])
entVerticalShift.draw(gui)
entVerticalShift.setFace(FONT)

txtVerticalShift = Text(Point(1, 3.75), "Vertical Shift:")
txtVerticalShift.setFace(FONT)
txtVerticalShift.draw(gui)

# Horizontal Shift entry
entHorizontalShift = DblEntry(Point(1, 4.25), width=10, span=[0, 1])
entHorizontalShift.draw(gui)
entHorizontalShift.setFace(FONT)

txtHorizontalShift = Text(Point(1, 4.75), "Horizontal Shift:")
txtHorizontalShift.setFace(FONT)
txtHorizontalShift.draw(gui)

# Theta entry
entTheta = DblEntry(Point(1, 5.25), width=10, span=[-90, 90])
entTheta.draw(gui)
entTheta.setFace(FONT)

txtTheta = Text(Point(1, 5.75), "Theta:")
txtTheta.setFace(FONT)
txtTheta.draw(gui)

# ScaleY entry
entScaleY = DblEntry(Point(1, 6.25), width=10, span=[0, 1])
entScaleY.draw(gui)
entScaleY.setFace(FONT)

txtScaleY = Text(Point(1, 6.75), "Y Scaling:")
txtScaleY.setFace(FONT)
txtScaleY.draw(gui)

# ScaleX entry
entScaleX = DblEntry(Point(1, 7.25), width=10, span=[0, 1])
entScaleX.draw(gui)
entScaleX.setFace(FONT)

txtScaleX = Text(Point(1, 7.75), "X Scaling:")
txtScaleX.setFace(FONT)
txtScaleX.draw(gui)

txtTransformations = []


class Transformation:
    '''Transform Class that manages each of the parts of a transform and allows easy reformatting'''
    def __init__(self, scaleX, scaleY, theta, phi, dx, dy, prob=1, color="black"):
        self.scaleX = scaleX
        self.scaleY = scaleY
        self.theta = theta
        self.phi = phi
        self.dx = dx
        self.dy = dy
        self.prob = prob
        self.color = color

    def __repr__(self, showProb=False):
        if not (self.prob == 1) or showProb:
            return "( r = " + str(self.scaleX) + ", s = " + str(self.scaleY) + ", theta = " + str(self.theta) + \
                   ", phi = " + str(self.phi) + ", h = " + str(self.dx) + ", k =" + str(self.dy) + ", prob = " + \
                   str(self.prob) + ", color = " + self.color + ")"
        else:
            return "( r = " + str(self.scaleX) + ", s = " + str(self.scaleY) + ", theta = " + str(self.theta) + \
                   ", phi = " + str(self.phi) + ", h = " + str(self.dx) + ", k =" + str(
                self.dy) + ", color = " + self.color + ")"

    def __str__(self):
        return self.__repr__()


def addprobTransformations():
    '''converts the list of transformations, into a list has probabilities'''
    global probTransformations
    probTransformations = []

    for t in transformations:
        for i in range(t.prob):
            probTransformations.append(t)


def runTransform(n, x, y):
    '''returns the transformed coordinates of each transform '''
    t = probTransformations[n]
    r = t.scaleX
    s = t.scaleY
    theta = t.theta
    phi = t.phi
    h = t.dx
    k = t.dy
    tempx = x * r * cos(radians(theta)) - y * s * sin(radians(phi)) + h
    y = x * r * sin(radians(theta)) + y * s * cos(radians(phi)) + k
    return (tempx, y)


def iterate(win, numTrans, numIters):
    '''iterates the transformations. NOTE: uses the color within each transformation.'''
    x = random()
    y = random()

    for i in range(numTrans):
        n = randrange(0, len(probTransformations))
        x, y = runTransform(n, x, y)

    for i in range(numIters):
        n = randrange(0, len(probTransformations))
        x, y = runTransform(n, x, y)
        win.plot(x, y, probTransformations[n].color)


def iterateTwoToned(win, numTrans, numIters, foregroundColor):
    '''iterates the transformations. NOTE: uses the passed in foregroundColor'''
    x = random()
    y = random()

    for i in range(numTrans):
        n = randrange(0, len(probTransformations))
        x, y = runTransform(n, x, y)

    for i in range(numIters):
        n = randrange(0, len(probTransformations))
        x, y = runTransform(n, x, y)
        win.plot(x, y, foregroundColor)


def changeButtonActivity():
    '''changes the activity of the buttons'''
    global buttonsActive

    if buttonsActive:
        btnExit.deactivate()
        btnClear.deactivate()
        btnDraw.deactivate()
        btnZoomIn.deactivate()
        btnZoomOut.deactivate()
        btnDeleteAll.deactivate()
        btnEnterDrawingIterations.deactivate()
        btnEnterTransientIterations.deactivate()
        btnConfirmTransformation.deactivate()
        btnConfirmChanges.deactivate()
        btnDeleteSelected.deactivate()
        btnAddNew.deactivate()
        btnKochCurve.deactivate()
        btnInfinity.deactivate()
        btnTwoToned.deactivate()
        btnForeground.deactivate()
        btnTransformationColor.deactivate()
        btnTransformationColorSelection.deactivate()
    else:
        btnExit.activate()
        btnClear.activate()
        btnDraw.activate()
        btnZoomIn.activate()
        btnZoomOut.activate()
        btnDeleteAll.activate()
        btnEnterDrawingIterations.activate()
        btnEnterTransientIterations.activate()
        btnConfirmTransformation.activate()
        btnConfirmChanges.activate()
        btnDeleteSelected.activate()
        btnAddNew.activate()
        btnKochCurve.activate()
        btnInfinity.activate()
        btnTwoToned.activate()
        btnForeground.activate()
        btnTransformationColor.activate()
        btnTransformationColorSelection.activate()

    buttonsActive = not (buttonsActive)


def resetDropDownOptions():
    '''replaces the old dropdown with a new one with updated transformations'''
    global drpTransformationSelection
    choices = []
    if len(transformations) > 0:
        for i in range(len(transformations)):
            choices.append(str(i) + ". " + transformations[i].__repr__())
    else:
        choices.append(" ")
    drpTransformationSelection.undraw()
    drpTransformationSelection = DropDown(DROPDOWNPOINT, choices=choices, width=DROPDOWNWIDTH, font=(FONT, 12))
    drpTransformationSelection.draw(gui)


def updateTextBoxes():
    '''updates textboxes on the gui'''
    txtDrawingIterations.setText("# of Drawing Iterations = " + str(drawingIterations))
    txtTransientIterations.setText("# of Transient Iterations = " + str(transientIterations))


def setEntrys(index):
    '''sets each of the entries equal the values transformations[index]'''
    if not (index == -1):
        entProbabilityWeight.setText(transformations[index].prob)
        entHorizontalShift.setText(transformations[index].dx)
        entVerticalShift.setText(transformations[index].dy)
        entTheta.setText(transformations[index].theta)
        entScaleX.setText(transformations[index].scaleX)
        entScaleY.setText(transformations[index].scaleY)
        btnTransformationColor.setButtonColor(transformations[index].color)


def getNewButtonColor(btn):
    '''asks the user for a new color uses colorchooser'''
    color = colorchooser.askcolor()[0]
    # NOTE: I use a try and except statement here to account for the user clicking cancel on the color chooser,
    # thus returning a 'NoneType' Object. I return the color of the button based in
    try:
        return color_rgb(int(color[0]), int(color[1]), int(color[2]))
    except TypeError:
        return btn.getButtonColor()


def readEntrys():
    '''creates and returns a new transformation with the values in the entry boxes'''
    prob = entProbabilityWeight.getValue()
    horz = entHorizontalShift.getValue()
    vert = entVerticalShift.getValue()
    theta = entTheta.getValue()
    scaleX = entScaleX.getValue()
    scaleY = entScaleY.getValue()
    color = btnTransformationColor.getButtonColor()
    return Transformation(scaleX, scaleY, theta, theta, horz, vert, prob, color)


def setEntrysTo0():
    '''sets the entries to default values'''
    entProbabilityWeight.setText(" ")
    entHorizontalShift.setText(" ")
    entVerticalShift.setText(" ")
    entTheta.setText(" ")
    entScaleX.setText(" ")
    entScaleY.setText(" ")
    btnTransformationColor.setButtonColor("white")


def displayTransformations():
    '''manages displaying the transformations below the dropdown object'''
    global txtTransformations
    for txt in txtTransformations:
        txt.undraw()
    x = 6
    y = 6.5
    i = 1
    size = 12
    for t in transformations:
        txtObj = Text(Point(x, y), str(i) + ". " + t.__repr__(showProb=True))
        txtObj.setFace(FONT)
        txtObj.setSize(size)
        txtObj.draw(gui)
        txtTransformations.append(txtObj)
        y -= .25
        i += 1

def main():
    global IFS, win, drawingIterations, transientIterations, transformations

    # weird infinity thing
    # (r, s, theta, phi, h, k)
    transformations.append(Transformation(.333, .333, 0, 0, 0, 0))
    transformations.append(Transformation(.333, .333, 0, 0, .333, 0))
    transformations.append(Transformation(.333, .333, 0, 0, .667, 0))
    transformations.append(Transformation(.667, .667, 0, 0, .167, .333, 4))
    '''
    # koch curve
    transformations.append(Transformation(.333, .333, 0, 0, 0, 0))
    transformations.append(Transformation(0.333, 0.333, 60, 60, 0.333, 0))
    transformations.append(Transformation(0.333, .333, -60, -60, 0.5, 0.2886))
    transformations.append(Transformation(.333, .333, 0, 0, .67, 0))

    # weird triangle thingy
    addTransform(0.5, 0.5, 0, 0, 0, 0)
    addTransform(0.5, 0.5, 0, 0, 0.5, 0)
    addTransform(0.5, 0.5, 0, 0, 0, .5)
    # addTransform(0.5, 0.5, 0, 0, 1, 0.5)
    '''

    resetDropDownOptions()
    changeButtonActivity()
    displayTransformations()
    btnTransformationColorSelection.deactivate()
    btnClear.deactivate()
    isDrawn = False
    twoToned = False
    foregroundColor = "Black"
    backgroundColor = "White"

    updateTextBoxes()
    clickPoint = gui.getMouse()

    while not (btnExit.clicked(clickPoint)):

        if btnDraw.clicked(clickPoint):
            if not (isDrawn):
                addprobTransformations()
                if twoToned:
                    iterateTwoToned(win, transientIterations, drawingIterations, foregroundColor)
                else:
                    iterate(win, transientIterations, drawingIterations)
                isDrawn = True
            btnDraw.deactivate()
            btnClear.activate()

        if btnClear.clicked(clickPoint):
            win.clear()
            isDrawn = False
            btnDraw.activate()
            btnClear.deactivate()

        if btnEnterTransientIterations.clicked(clickPoint):
            transientIterations = entTransientIterations.getValue()

        if btnEnterDrawingIterations.clicked(clickPoint):
            drawingIterations = entDrawingIterations.getValue()

        if btnConfirmTransformation.clicked(clickPoint):
            selectedTransformIndex = int(drpTransformationSelection.getChoice()[0])
            setEntrys(selectedTransformIndex)

        if btnConfirmChanges.clicked(clickPoint):
            if entProbabilityWeight.checkValue() and entHorizontalShift.checkValue() and entVerticalShift.checkValue() \
                    and entTheta.checkValue() and entScaleX.checkValue() and entScaleY.checkValue():
                editedTransform = readEntrys()
                transformations[selectedTransformIndex] = editedTransform

                resetDropDownOptions()
                selectedTransformIndex = 0
                setEntrysTo0()

        if btnDeleteSelected.clicked(clickPoint):
            transformations.pop(selectedTransformIndex)
            resetDropDownOptions()
            selectedTransformIndex = 0
            setEntrysTo0()

        if btnDeleteAll.clicked(clickPoint):
            transformations = []
            resetDropDownOptions()
            selectedTransformIndex = 0

        if btnAddNew.clicked(clickPoint):
            transformations.append(readEntrys())
            resetDropDownOptions()

        if btnTransformationColor.clicked(clickPoint):
            btnTransformationColor.setButtonColor(getNewButtonColor(btnTransformationColor))

        if btnForeground.clicked(clickPoint):
            btnForeground.setButtonColor(getNewButtonColor(btnTransformationColor))

        if btnTransformationColorSelection.clicked(clickPoint):
            twoToned = False
            btnTransformationColorSelection.deactivate()
            btnTwoToned.activate()

        if btnTwoToned.clicked(clickPoint):
            twoToned = True
            foregroundColor = btnForeground.getButtonColor()
            btnTwoToned.deactivate()
            btnTransformationColorSelection.activate()

        if btnKochCurve.clicked(clickPoint):
            transformations = []
            transformations.append(Transformation(.333, .333, 0, 0, 0, 0))
            transformations.append(Transformation(0.333, 0.333, 60, 60, 0.333, 0))
            transformations.append(Transformation(0.333, .333, -60, -60, 0.5, 0.2886))
            transformations.append(Transformation(.333, .333, 0, 0, .67, 0))
            resetDropDownOptions()
            selectedTransformIndex = 0

        if btnInfinity.clicked(clickPoint):
            transformations = []
            transformations.append(Transformation(.333, .333, 0, 0, 0, 0))
            transformations.append(Transformation(.333, .333, 0, 0, .333, 0))
            transformations.append(Transformation(.333, .333, 0, 0, .667, 0))
            transformations.append(Transformation(.667, .667, 0, 0, .167, .333, 4))
            resetDropDownOptions()
            selectedTransformIndex = 0


        displayTransformations()
        win.setBackground(backgroundColor)
        updateTextBoxes()
        clickPoint = gui.getMouse()

    win.close()


if __name__ == '__main__':
    main()
