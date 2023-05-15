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
 * @param {any} event
 */
function connectHandler(event, websocket) {

    console.log(
        "Gamepad connected at index %d: %s",
        event.gamepad.index, event.gamepad.id
    );
    sendMoves(websocket, event.gamepad)
}

/**
 * 
 * @param {any} websocket
 */
function sendMoves(websocket, gamepad) {

    if (buttonPressed(gamepad.buttons[0])) {
        console.log('up')
        websocket.send(JSON.stringify('Switch_2_on'));
    }
}

/**
 * 
 */
function start() {

    var t = "ws://" + location.hostname + ":8888/echo";
    const websocket = new WebSocket(t);
    websocket.onopen = () => websocket.send("admin:123456");
    window.addEventListener("gamepadconnected", (e) => {
        connectHandler(e, websocket);
    }, false);
}

window.onload = start;
