console.log('hello world')

window.addEventListener("gamepadconnected", (e) => {
    console.log(
        "Gamepad connected at index %d: %s. %d buttons, %d axes.",
        e.gamepad.index,
        e.gamepad.id,
        e.gamepad.buttons.length,
        e.gamepad.axes.length
    );
});

window.addEventListener("gamepaddisconnected", (e) => {
    console.log(
        "Gamepad disconnected from index %d: %s",
        e.gamepad.index,
        e.gamepad.id
    );
});

let a = 0;

function buttonPressed(b) {
    if (typeof b === "object") {
        return b.pressed;
    }
    return b === 1.0;
}

function update() {

    const gamepads = navigator.getGamepads()

    if (!gamepads) {
        return;
    }

    const gp = gamepads[0];

    if (buttonPressed(gp.buttons[0])) {
        a++;
        console.log('up')
    }

        window.requestAnimationFrame(update)
}

window.requestAnimationFrame(update)