# Wifi Monitor

We're having some speed issues with our Wifi at our AirBnb, so we're keeping
a log of the internet speed over the course of the days.

## How it works
I've created a quick and dirty script that pings the wifi every 5 min and does a download test on the hour. On completion, we push the data to github where its displayed on [a very simplistic frontend](https://foleyfactor.github.io/wifi_monitor).

## TODO:
 * Make frontend nicer (maybe graph definitely add filter)
 * Wait for rpi to arrive then setup the cron job on rpi so that we get a good stream of data (and dont have a while True loop going)
 * E X T E N S I B I L I T Y
