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

function padZero(n) {
    return (n < 10 && n >= 0 ? "0" : "") + n;
}

let warnDownloadSpeed = 5;
let criticalDownloadSpeed = 2;
let warnPing = "Down";
let criticalPing = "Down";

let downloadPlotLayout = {
    title: 'Download Speeds',
    xaxis: {
        title: 'Time',
    },
    yaxis: {
        title: 'Download Speed (Mb/s)',
    },
};

let pingLayout = {
    title: 'Connection Status',
    annotations: [{
        showarrow: false,
        text: '',
    }],
};

$(document).ready(() => {
    $el_speed = $('#speed_data_body');
    $el_ping = $('#ping_data_body');

    let cutoff = parseInt(((new Date()).getTime() - 24*60*60*1000) / 1000);

    let x = new XMLHttpRequest();
    x.overrideMimeType('application/json');
    x.open('GET', 'output.json?' + (new Date()).getTime(), false);
    x.send();
    let loadedJSON = JSON.parse(x.responseText);

    let plotMe = {
        x: [],
        y: [],
        type: 'scatter'
    };

    let speedtimes = [];
    let pingtimes = [];
    for (key in loadedJSON['speeds']) speedtimes.push(parseInt(key));
    for (key in loadedJSON['pings']) pingtimes.push(parseInt(key));
    speedtimes.sort((a,b) => { return b-a; });
    pingtimes.sort((a,b) => { return b-a; });
    for (el of speedtimes) {
        if (el <= cutoff) continue;
        $el_speed.append(getDataRow(prettifyDate(el), loadedJSON['speeds'][el + ''], warnDownloadSpeed, criticalDownloadSpeed));
        let time = new Date(el*1000);
        let strTime = time.getFullYear() + "-" + padZero(time.getMonth() + 1)  + "-" + padZero(time.getDate())+ " " + padZero(time.getHours()) + ":" + padZero(time.getMinutes())+ ":" + padZero(time.getSeconds());

        plotMe.x.push(strTime);
        plotMe.y.push(loadedJSON['speeds'][el + '']);
    }

    let pass = 0;
    let fail = 0;

    for (el of pingtimes) {
        if (el <= cutoff) continue;
        $el_ping.append(getDataRow(prettifyDate(el), loadedJSON['pings'][el + ''] == 1 ? "Up" : "Down", warnPing, criticalPing));
        if (loadedJSON['pings'][el + '']) ++pass;
        else ++fail;
    }

    let pingPlot = {
        values: [pass, fail],
        labels: ["Up", "Down"],
        hoverinfo: 'label+percent',
        hole: 0.7,
        type: 'pie',
        marker: {
            colors: ["rgb(7, 142, 20)", "rgb(191, 22, 53)"],
        },
    };


    Plotly.newPlot('download_speeds', [plotMe], downloadPlotLayout);
    Plotly.newPlot('pings', [pingPlot], pingLayout);

});

window.onresize = function () {
    Plotly.Plots.resize('download_speeds');
    Plotly.Plots.resize('pings');
}
