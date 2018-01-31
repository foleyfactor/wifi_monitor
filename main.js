function getDataRow(first, second, warn, critical) {
    let cls = second <= warn ? (second <= critical ? 'critical' : 'warn') : 'ok'
    return '<tr class="' + cls + '"><td class="left">' + first + '</td><td class="right">' + second + '</td></tr>';
}

function prettifyDate(d) {
    let date = new Date(d*1000);
    let ms = ['Jan', 'Feb', 'Mar', 'Apr', 'Jun', 'Jul', 'Aug', 'Sep', 'Nov', 'Dec'];
    let    mon = ms[date.getMonth()];
    let    day = date.getDate();
    let    hours = date.getHours();
    let    min = date.getMinutes();
    return mon + ' ' + day + ' - ' + hours + ':' + (min >= 10 ? min : '0' + min);
}

let warnDownloadSpeed = 10;
let criticalDownloadSpeed = 5;
let warnPing = "Down";
let criticalPing = "Down";

$(document).ready(() => {
    $el_speed = $('#speed_data_body');
    $el_ping = $('#ping_data_body');

    let x = new XMLHttpRequest();
    x.overrideMimeType('application/json');
    x.open('GET', 'output.json?' + (new Date()).getTime(), false);
    x.send();
    let loadedJSON = JSON.parse(x.responseText);

    let speedtimes = [];
    let pingtimes = [];
    for (key in loadedJSON['speeds']) speedtimes.push(parseInt(key));
    for (key in loadedJSON['pings']) pingtimes.push(parseInt(key));
    speedtimes.sort((a,b) => { return b-a; });
    pingtimes.sort((a,b) => { return b-a; });
    for (el of speedtimes) {
        $el_speed.append(getDataRow(prettifyDate(el), loadedJSON['speeds'][el + ''], warnDownloadSpeed, criticalDownloadSpeed));
    }
    for (el of pingtimes) {
        $el_ping.append(getDataRow(prettifyDate(el), loadedJSON['pings'][el + ''] == 1 ? "Up" : "Down", warnPing, criticalPing));
    }

});

