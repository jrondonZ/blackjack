#Christopher Meza, Josiah Rondon, Ava Dobro
#11/29/22
#File: buttonforblackjack.py
#Button class

from graphics import *

#Makes it easier to create buttons, and additionally helps determine whether they've been clicked or not.
class Button:

    #Takes in all the initial commands, and allows the user to set specific features of the button such as height, width, and the label text.
    def __init__(self, win, center, width, height, label):
        w, h = width/2.0, height/2.0
        x, y = center.getX(), center.getY()
        self.center = Point(x, y)
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)

        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.activate()

    #Will return true or false based on whether the coordinate clicked falls within the bounds of the button or not.
    def clicked(self, p):
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        return self.label.getText()

    #Sets the button to active, allowing the user to click it, and the program in return will execute some command.
    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    #Makes it so the program will no longer register if the button has been clicked or not.
    def deactivate(self):
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

    #Allows the user to change the text label on the button.
    def update(self, win, label):
        self.label.undraw()
        center = self.center
        self.label = Text(center, label)
        self.active = False
        self.label.draw(win)