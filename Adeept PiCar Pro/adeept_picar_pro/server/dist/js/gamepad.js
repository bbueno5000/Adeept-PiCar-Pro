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
    setInterval(sendMoves(websocket, event.gamepad), 100)
}

/**
 * 
 * @param {any} websocket
 */
function sendMoves(websocket, gamepad) {

    if (buttonPressed(gamepad.buttons[0])) {
        console.log('up')
        websocket.send(JSON.stringify('Switch_3_on'));
    }
    else if (buttonPressed(gamepad.buttons[1])) {
        console.log('down')
        websocket.send(JSON.stringify('Switch_3_off'));
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
