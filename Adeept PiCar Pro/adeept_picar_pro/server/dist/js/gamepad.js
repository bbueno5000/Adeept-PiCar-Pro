"use strict";

let gamepad;
let interval;

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
function connectHandler(event) {

    console.log(
        "Gamepad connected at index %d: %s",
        event.gamepad.index, event.gamepad.id
    );
    gamepad = event.gamepad;
    interval = setInterval(sendMoves, 100);
}

/**
 * 
 * @param {any} websocket
 * @param {any} gamepad
 */
function sendMoves() {

    let command;
    if (buttonPressed(gamepad.buttons[0])) {
        console.log("up");
        command = "Switch_3_on";
        clearInterval(interval);
    }
    else if (buttonPressed(gamepad.buttons[1])) {
        console.log("down");
        command = "Switch_3_off";
        clearInterval(interval);
    }
    interval = setInterval(sendMoves, 100);
//    websocket.send(JSON.stringify(command));
}

/**
 * 
 */
function start() {

//    var t = "ws://" + location.hostname + ":8888/echo";
//    const websocket = new WebSocket(t);
//    websocket.onopen = () => websocket.send("admin:123456");
    window.addEventListener("gamepadconnected", connectHandler);
}

window.onload = start;
