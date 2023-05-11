console.log('gamepad')

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

window.addEventListener("DOMContentLoaded", () => {
    const app = document.querySelector(".app");
    const websocket = new WebSocket("ws://http://192.168.1.164:5000/");
    sendMoves(app, websocket);
});

/**
 * 
 * @param {any} b
 * @returns
 */
function buttonPressed(b) {
    if (typeof b === "object") {
        return b.pressed;
    }
    return b === 1.0;
}

/**
 * 
 * @param {any} board
 * @param {any} websocket
 */
function sendMoves(board, websocket) {
    const gamepads = navigator.getGamepads()
    if (!gamepads) {
        return;
    }
    const gp = gamepads[0];
    if (buttonPressed(gp.buttons[0])) {
        console.log('up')
        const event = {
            'status': 'ok',
            'title': '',
            'data': 'forward'
        }
        websocket.send(JSON.stringify(event));
    }
}

/**
 * 
 * @param {any} message
 */
function showMessage(message) {
    window.setTimeout(() => window.alert(message), 50);
}
