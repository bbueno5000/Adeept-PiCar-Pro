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

function pollGamepads() {

    const gamepads = navigator.getGamepads();
    for (const gamepad of gamepads) {
        console.log("Gamepad connected at index ${gamepad.index}: ${gamepad.id}.");
        var t = "ws://" + location.hostname + ":8888/echo";
        const websocket = new WebSocket(t);
        websocket.onopen = () => websocket.send("admin:123456");
        setInterval(sendMoves(websocket, gamepad), 100);
    }
}

/**
 * 
 * @param {any} websocket
 */
function sendMoves(websocket, gamepad) {

    let command;
    if (buttonPressed(gamepad.buttons[0])) {
        console.log("up");
        command = "Switch_3_on";
    }
    else if (buttonPressed(gamepad.buttons[1])) {
        console.log("down");
        command = "Switch_3_off";
    }
    websocket.send(JSON.stringify(command));
}

/**
 * 
 */
function start() {

    window.addEventListener("gamepadconnected", (e) => {
        setInterval(pollGamepads, 500);
    });
}

window.onload = start;
