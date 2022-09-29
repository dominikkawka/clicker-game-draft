def on_button_pressed_a():
    global cookieCount
    cookieCount += cookiePerClick
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global cookiePerClick, cookieCount, upgradePrice
    basic.show_string("Shop")
    if cookieCount > upgradePrice:
        cookiePerClick += 1
        cookieCount = cookieCount - upgradePrice
        upgradePrice += upgradePrice * 2
        basic.show_string("Upgrade")
    else:
        basic.show_icon(IconNames.CONFUSED)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_string("" + str((cookieCount)))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_icon(IconNames.HEART)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

cookieCount = 0
cookiePerClick = 0
upgradePrice = 0
upgradePrice = 50
cookiePerClick = 1