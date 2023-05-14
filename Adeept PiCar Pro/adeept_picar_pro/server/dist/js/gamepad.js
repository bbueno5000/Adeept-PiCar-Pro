"use strict";

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
 * @param {any} e
 */
function connectHandler(e) {
    console.log(
        "Gamepad connected at index %d: %s",
        e.gamepad.index,
        e.gamepad.id
    );
    start();
}

/**
 * 
 * @param {any} websocket
 */
function sendMoves(websocket) {
    const gamepads = navigator.getGamepads()
    if (!gamepads) { return; }
    const gamepad = gamepads[0];
    if (buttonPressed(gamepad.buttons[0])) {
        console.log('up')
        websocket.send(JSON.stringify(forward));
    }
}

/**
 * 
 */
function start() {
    var t = "ws://" + location.hostname + ":8888/echo";
    const websocket = new WebSocket(t);
    websocket.onopen = () => websocket.send("admin:123456");
    setInterval(function () { sendMoves(websocket); }, 100)
}

window.addEventListener("gamepadconnected", connectHandler);
