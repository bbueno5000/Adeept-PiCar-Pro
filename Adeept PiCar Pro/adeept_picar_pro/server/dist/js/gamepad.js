
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
    var t = "ws://" + location.hostname + ":8888/echo";
    const websocket = new WebSocket(t);
    websocket.onopen = () => websocket.send("admin:123456");
    sendMoves(websocket);
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
    const gamepads = navigator.webkitGetGamepads()
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

window.addEventListener("gamepadconnected", connectHandler);
window.addEventListener("gamepaddisconnected", disconnectHandler);
