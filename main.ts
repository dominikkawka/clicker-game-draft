input.onButtonPressed(Button.A, function () {
    cookieCount += cookiePerClick
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("Shop")
    if (cookieCount > upgradePrice) {
        cookiePerClick += 1
        cookieCount = cookieCount - upgradePrice
        upgradePrice += upgradePrice * 2
        basic.showString("Upgrade")
    } else {
        basic.showIcon(IconNames.Confused)
    }
})
input.onButtonPressed(Button.B, function () {
    basic.showString("" + cookieCount)
})
input.onGesture(Gesture.Shake, function () {
    basic.showIcon(IconNames.Heart)
})
let cookieCount = 0
let cookiePerClick = 0
let upgradePrice = 0
upgradePrice = 50
cookiePerClick = 1
