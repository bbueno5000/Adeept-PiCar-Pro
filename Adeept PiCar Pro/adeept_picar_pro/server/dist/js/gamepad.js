console.log('gamepad')

window.addEventListener("DOMContentLoaded", () => {
    //const app = document.querySelector(".app");
    var t = "ws://" + location.hostname + ":8888/echo";
    const websocket = new WebSocket(t);
    websocket.onmessage = function (e) { console.log(e.data); };
    websocket.onopen = () => websocket.send("admin:123456");
    sendMoves(websocket);
});

window.addEventListener("gamepadconnected", (e) => {
    console.log(
        "Gamepad connected at index %d: %s",
        e.gamepad.index,
        e.gamepad.id
    );
});

window.addEventListener("gamepaddisconnected", (e) => {
    console.log(
        "Gamepad disconnected from index %d: %s",
        e.gamepad.index,
        e.gamepad.id
    );
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
function sendMoves(websocket) {
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
