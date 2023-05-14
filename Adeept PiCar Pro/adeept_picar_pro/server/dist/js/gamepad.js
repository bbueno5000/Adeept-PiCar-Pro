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
}

/**
 * 
 * @param {any} e
 */
function disconnectHandler(e) {
    console.log(
        "Gamepad disconnected from index %d: %s",
        e.gamepad.index,
        e.gamepad.id
    );
}
/**
 * 
 * @param {any} websocket
 */
function sendMoves(websocket) {
    const gamepads = navigator.getGamepads()
    if (!gamepads) { return; }
    const gamepad = gamepads[0];
    if (gamepad.buttons[0] === 1) {
        console.log('up')
        //const event = {
        //    'status': 'ok',
        //    'title': '',
        //    'data': 'forward'
        //}
        //websocket.send(JSON.stringify(event));
    }
}

function start() {
    var t = "ws://" + location.hostname + ":8888/echo";
    const websocket = new WebSocket(t);
    websocket.onopen = () => websocket.send("admin:123456");
    window.addEventListener("gamepadconnected", connectHandler);
    window.addEventListener("gamepaddisconnected", disconnectHandler);
    setInterval(function () { sendMoves(websocket); }, 100)
}

window.onload = start;