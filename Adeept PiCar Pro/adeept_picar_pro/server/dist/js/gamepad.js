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
 * @param {any} websocket
 * @param {any} gamepad
 */
function sendMoves(gamepad) {

    let command;
    if (buttonPressed(gamepad.buttons[0])) {
        console.log("up");
        command = "Switch_3_on";
    }
    else if (buttonPressed(gamepad.buttons[1])) {
        console.log("down");
        command = "Switch_3_off";
    }
//    websocket.send(JSON.stringify(command));
}

/**
 * 
 */
function start() {
//    var t = "ws://" + location.hostname + ":8888/echo";
//    const websocket = new WebSocket(t);
//    websocket.onopen = () => websocket.send("admin:123456");
    window.addEventListener("gamepadconnected", (e) => {
        console.log("Gamepad connected at index %d: %s",
            e.gamepad.index, e.gamepad.id);
        setInterval(function () {
            let command;
            if (buttonPressed(gamepad.buttons[0])) {
                console.log("up");
                command = "Switch_3_on";
            }
            else if (buttonPressed(gamepad.buttons[1])) {
                console.log("down");
                command = "Switch_3_off";
            }
        }, 100);
    });
}

window.onload = start;
