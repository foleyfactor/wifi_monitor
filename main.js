function getDataRow(first, second, warn, critical) {
    let cls = second <= warn ? (second <= critical ? 'critical' : 'warn') : 'ok'
    return '<tr class="' + cls + ' table-row"><td class="left">' + first + '</td><td class="right">' + second + '</td></tr>';
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

function loadAndRenderContent() {
    $el_speed = $('#speed_data_body');
    $el_ping = $('#ping_data_body');
    $el_downtimes = $('#downtime-body');

    let cutoff = parseInt(((new Date()).getTime() - 24*60*60*1000) / 1000);

    let x = new XMLHttpRequest();
    x.overrideMimeType('application/json');
    x.open('GET', 'output.json?' + (new Date()).getTime(), false);
    x.send();
    let loadedJSON = JSON.parse(x.responseText);

    console.log('here');

    let y = new XMLHttpRequest();
    y.overrideMimeType('application/json');
    y.open('GET', 'interval.json?' + (new Date()).getTime(), false);
    y.send();
    let intervals = JSON.parse(y.responseText);
    console.log(intervals);

    let plotMe = {
        x: [],
        y: [],
        type: 'scatter'
    };

    // Used to have a list of pings, now we only have the most recent

    let speedtimes = [];
    let downtimes = [];

    for (key in loadedJSON['speeds']) speedtimes.push(parseInt(key));
    for (key in loadedJSON['downtimes'])
        downtimes.push([parseInt(key), loadedJSON['downtimes'][key]])
    speedtimes.sort((a,b) => { return b-a; });
    for (el of speedtimes) {
        if (el <= cutoff) continue;
        // $el_speed.append(getDataRow(prettifyDate(el), loadedJSON['speeds'][el + ''], warnDownloadSpeed, criticalDownloadSpeed));
        let time = new Date(el*1000);
        let strTime = time.getFullYear() + "-" + padZero(time.getMonth() + 1)  + "-" + padZero(time.getDate())+ " " + padZero(time.getHours()) + ":" + padZero(time.getMinutes())+ ":" + padZero(time.getSeconds());

        plotMe.x.push(strTime);
        plotMe.y.push(loadedJSON['speeds'][el + '']);
    }

    mostRecent = loadedJSON['pings']['most_recent'] * 1000;

    console.log((new Date()).getTime() - mostRecent, (intervals['pings'] + 60) * 1000);

    if ((new Date()).getTime() - mostRecent > (intervals['pings'] + 60) * 1000) {
        $('#announce').text('The WiFi is (probably) currently down.');
    }

    let totalDowntime = 0;
    for (el of downtimes) {
        if (el[1] <= cutoff) continue;
        let start = Math.max(el[0], cutoff);
        totalDowntime += el[1] - start;
    }
    let totalUptime = 24 * 60 * 60 - totalDowntime;

    let downKeys = [];
    for (el of downtimes) downKeys.push(parseInt(el[0]));
    downKeys.sort((a,b) => { return b-a; });
    $el_downtimes.empty();
    for (key of downKeys) {
        if (loadedJSON['downtimes'][key + ''] <= cutoff) continue;
        $el_downtimes.append(getDataRow(prettifyDate(key), prettifyDate(loadedJSON['downtimes'][key + '']), -1, -1));
    }


    let pingPlot = {
        values: [totalUptime, totalDowntime],
        labels: ["Up", "Down"],
        hoverinfo: 'label+percent',
        hole: 0.7,
        type: 'pie',
        marker: {
            colors: ["rgb(7, 142, 20)", "rgb(191, 22, 53)"],
        },
    };


    Plotly.purge('download_speeds');
    Plotly.purge('pings');
    Plotly.newPlot('download_speeds', [plotMe], downloadPlotLayout);
    Plotly.newPlot('pings', [pingPlot], pingLayout);
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
    loadAndRenderContent();
    setInterval(loadAndRenderContent, 60000);
});

window.onresize = function () {
    Plotly.Plots.resize('download_speeds');
    Plotly.Plots.resize('pings');
}
