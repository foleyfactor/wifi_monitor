# Wifi Monitor

We're having some speed issues with our Wifi at our AirBnb, so we're keeping
a log of the internet speed over the course of the days.

## How it works
I've created a quick and dirty script that pings the wifi every 5 min and does a download test on the hour. On completion, we push the data to github where its displayed on [a very simplistic frontend](https://foleyfactor.github.io/wifi_monitor).

## TODO:
 * Make frontend nicer (add filter)
 * E X T E N S I B I L I T Y

## Planning:
What we want to know:
Graph of download speed (done)

Is the WiFi currently down?
How do we know?
Lack of updates.
Both frontend and backend must agree on polling interval for pings
Should communicate downtimes (start and end time) through json
Frontend should be upset if no updates have come in by a certain time (polling interval)
Display of percentage uptime will be 24 hours - downtime
file['downtimes'] = mapping: start time -> end time

Check what happens if wget fails (we probably get an exception)
