// only player one asks for advance periodically
let advance_interval = null;
if (js_vars.player_id === 1) {
    advance_interval = window.setInterval(function () {
        liveSend('advance?')
    }, 5000);
} else {
    // we need to ask at least once in case player 1 is gone and in case that we arrived late to the waitpage
    liveSend('advance?')
}

function liveRecv(data) {
    if (data['advance'] === js_vars.current_page_name) {
        if (advance_interval !== null) {
            clearInterval(advance_interval);
        }
        document.getElementById('form').submit();
    }
}
