"use strict";

const gamepads = {};

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
function gamepadHandler(event, connecting) {

    console.log(
        "Gamepad connected at index %d: %s",
        event.gamepad.index,
        event.gamepad.id
    );
    const gamepad = event.gamepad;
    if (connecting) {
        gamepads[gamepad.index] = gamepad;
    }
    else {
        delete gamepads[gamepad.index];
    }
}

/**
 * 
 * @param {any} websocket
 */
function sendMoves(websocket) {

    if (!gamepads) {
        return;
    }
    if (buttonPressed(gamepads[0].buttons[0])) {
        console.log('up')
        websocket.send(JSON.stringify('forward'));
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
        gamepadHandler(e, true);
    }, false);
    window.addEventListener("gamepaddisconnected", (e) => {
        gamepadHandler(e, false);
    }, false);
    sendMoves(websocket)
}

window.onload = start;
