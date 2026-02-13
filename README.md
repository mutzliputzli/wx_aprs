# wx_aprs

### Python script to forward local weather data from Wunderground to the APRS network.

There must be a property file aprs_beacon.properties in the same directory as the py file. It contains credentials for Wunderground and APRS access.

```
wundergroundStationId=<yourWundergroundStationId>
wundergroundApiKey=<yourWundergroundApiKey>
aprsCallsign=<yourCallsign>
aprsPasscode=<yourAprsPasscode>
```

[Wunderground API documentation](https://twcapi.co/v2PWSO)

[APRS weather data API](http://www.aprs.net/vm/DOS/WX.HTM)

[How to get an APRS passcode](https://www.darc.de/der-club/distrikte/o/ortsverbaende/aprspasscode/)

[Converting APRS coordinates](https://kd8tnv.com/coord.php)