"use strict";

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
    const gamepads = navigator.getGamepads()
    const gamepad = gamepads[0];
    var t = "ws://" + location.hostname + ":8888/echo";
    const websocket = new WebSocket(t);
    websocket.onopen = () => websocket.send("admin:123456");
    setInterval(sendMoves(gamepad, websocket), 100)
}

/**
 * 
 * @param {any} websocket
 */
function sendMoves(gamepad, websocket) {

    if (gamepad.buttons[0].pressed) {
        console.log('up')
        websocket.send(JSON.stringify('forward'));
    }
    else if (gamepad.buttons[1].pressed) {
        console.log('down')
        websocket.send(JSON.stringify('stop'));
    }
}

window.addEventListener("gamepadconnected", connectHandler);
