from wx import *
app = App()
frame = Frame(None, title="Restaurant Management System", size=(1000,700))
panel = Panel(frame)
panel.SetBackgroundColour('#c2c2a3')
main = BoxSizer(HORIZONTAL)

displayValue = '                                    Welcome to Dinner Club.'
total = 0

left = BoxSizer(VERTICAL)
menuGrp = GridSizer(3,3,10,10)

#Menu Buttton
samosa = Button(panel, label="Samosa")
momo = Button(panel, label="momo")
chowmine = Button(panel, label="Chowmine")
iceCream = Button(panel, label="Ice Cream")
kachori = Button(panel, label="Kachori")
dosa = Button(panel, label="Dosa")
roll = Button(panel, label="Roll")
sandwitch = Button(panel, label="SandWitch")
coke = Button(panel, label="Coke")
font1 = Font(25,FONTFAMILY_DECORATIVE,FONTSTYLE_NORMAL, FONTWEIGHT_BOLD)
font2 = Font(15,FONTFAMILY_DECORATIVE,FONTSTYLE_NORMAL, FONTWEIGHT_BOLD)

momo.SetFont(font1)
samosa.SetFont(font1)
kachori.SetFont(font1)
roll.SetFont(font1)
dosa.SetFont(font1)
sandwitch.SetFont(font1)
coke.SetFont(font1)
chowmine.SetFont(font1)
iceCream.SetFont(font1)

momo.SetBackgroundColour("#003366")
samosa.SetBackgroundColour("#003366")
kachori.SetBackgroundColour("#003366")
roll.SetBackgroundColour("#003366")
dosa.SetBackgroundColour("#003366")
sandwitch.SetBackgroundColour("#003366")
coke.SetBackgroundColour("#003366")
chowmine.SetBackgroundColour("#003366")
iceCream.SetBackgroundColour("#003366")

momo.SetForegroundColour("white")
samosa.SetForegroundColour("white")
kachori.SetForegroundColour("white")
roll.SetForegroundColour("white")
dosa.SetForegroundColour("white")
sandwitch.SetForegroundColour("white")
coke.SetForegroundColour("white")
chowmine.SetForegroundColour("white")
iceCream.SetForegroundColour("white")

menuGrp.AddMany([
    (samosa, 1, EXPAND),
    (momo, 1, EXPAND),
    (roll, 1, EXPAND),
    (coke, 1, EXPAND),
    (dosa, 1, EXPAND),
    (sandwitch, 1, EXPAND),
    (kachori, 1, EXPAND),
    (iceCream, 1, EXPAND),
    (chowmine, 1, EXPAND),
])
left.Add(menuGrp, 3, EXPAND|BOTTOM|TOP|RIGHT|LEFT , border=10)
screen = TextCtrl(panel,style=TE_MULTILINE)
screen.SetBackgroundColour('#2c3e50')
screen.SetForegroundColour('white')
screen.SetFont(font2) 
screen.SetValue(displayValue)
left.Add(screen, 1, EXPAND|BOTTOM|TOP|RIGHT|LEFT , border=10)

main.Add(left, 3, EXPAND)

btnGrp = GridSizer(5,1,5,5)
order = Button(panel, label="Order")
Total = Button(panel, label="Total")
clear = Button(panel, label="Clear")
settings = Button(panel, label="Settings")
exit = Button(panel, label="Exit")
#Font 
order.SetFont(font1)
Total.SetFont(font1)
clear.SetFont(font1)
settings.SetFont(font1)
exit.SetFont(font1)

#Background Color
exit.SetBackgroundColour('#CC0000')
Total.SetBackgroundColour('#0099CC')
settings.SetBackgroundColour('#00695c')
clear.SetBackgroundColour('#FF8800')
order.SetBackgroundColour('#007E33')
#FontColor
exit.SetForegroundColour('white')
Total.SetForegroundColour('white')
settings.SetForegroundColour('white')
clear.SetForegroundColour('white')
order.SetForegroundColour('white')


btnGrp.AddMany([
    (order, 1, EXPAND),
    (Total, 1, EXPAND),
    (clear, 1, EXPAND),
    (settings, 1, EXPAND),
    (exit, 1, EXPAND),
])

main.Add(btnGrp, 1 ,EXPAND|TOP|BOTTOM|RIGHT, border=10)

#funstion start from here
def enable():
    samosa.Enable()
    roll.Enable()
    sandwitch.Enable()
    kachori.Enable()
    iceCream.Enable()
    coke.Enable()
    dosa.Enable()
    momo.Enable()
    chowmine.Enable()
    Total.Enable()

def disable():
    samosa.Disable()
    roll.Disable()
    sandwitch.Disable()
    kachori.Disable()
    iceCream.Disable()
    coke.Disable()
    dosa.Disable()
    momo.Disable()
    chowmine.Disable()
    Total.Disable()

def samosa_fun(event):
    global displayValue, total
    total += 7
    displayValue +='\nSamosa  -----   07/-'
    screen.SetValue(displayValue)

def dosa_fun(event):
    global displayValue, total
    total += 40
    displayValue +='\nDosa   ------    40/-'
    screen.SetValue(displayValue)

def kachori_fun(event):
    global displayValue, total
    total += 7
    displayValue +='\nKachori   -----  07/-'
    screen.SetValue(displayValue)

def iceCream_fun(event):
    global displayValue, total
    total += 20
    displayValue +='\nIce Cream  -----   20/-'
    screen.SetValue(displayValue)

def coke_fun(event):
    global displayValue, total
    total += 15
    displayValue +='\nCoke   -----    15/-'
    screen.SetValue(displayValue)

def sandwitch_fun(event):
    global displayValue, total
    total += 30
    displayValue +='\nSandwitch   ----- 30/-'
    screen.SetValue(displayValue)

def roll_fun(event):
    global displayValue, total
    total += 40
    displayValue +='\nEgg Roll   ------  40/-'
    screen.SetValue(displayValue)

def chowmin_fun(event):
    global displayValue, total
    total += 30
    displayValue +='\nChowmin   -----  30/-'
    screen.SetValue(displayValue)

def momo_fun(event):
    global displayValue, total
    total += 40
    displayValue +='\nMomo     -----   30/-'
    screen.SetValue(displayValue)

def Total_fun(event):
    global displayValue, total
    if total:
        displayValue += f'''\n------------------------\nSubTotal ------ {total}/-\n-------------------\nGST(18%) ------ {int(total*0.18)}/-\n------------------------\nTotal inc All Tax ----- {int(total+total*0.18)}/-\n\nThank You for Trying us. :)'''
        screen.SetValue(displayValue)
        disable()

def clear_fun(event):
    global displayValue, total
    displayValue = '                                    Welcome to Dinner Club.'
    total = 0
    enable()
    screen.SetValue(displayValue)

def exit_fun(event):
    Exit()


#function binding start from here
samosa.Bind(EVT_BUTTON, samosa_fun, samosa)
roll.Bind(EVT_BUTTON, roll_fun, roll)
sandwitch.Bind(EVT_BUTTON, sandwitch_fun, sandwitch)
kachori.Bind(EVT_BUTTON, kachori_fun, kachori)
iceCream.Bind(EVT_BUTTON, iceCream_fun, iceCream)
coke.Bind(EVT_BUTTON, coke_fun, coke)
dosa.Bind(EVT_BUTTON, dosa_fun, dosa)
momo.Bind(EVT_BUTTON, momo_fun, momo)
chowmine.Bind(EVT_BUTTON, chowmin_fun, chowmine)

Total.Bind(EVT_BUTTON, Total_fun, Total)
clear.Bind(EVT_BUTTON, clear_fun, clear)
exit.Bind(EVT_BUTTON, exit_fun, exit)


    

panel.SetSizer(main)
frame.Center()
frame.ShowFullScreen(True)
frame.Show()
app.ExitMainLoop()
app.MainLoop()
