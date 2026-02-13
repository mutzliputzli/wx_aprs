# wx_aprs

### Python to forward local weather data from Wunderground to the APRS Network.

    
[Wunderground API documentation](https://twcapi.co/v2PWSO)

[How to get an APRS passcode](https://www.darc.de/der-club/distrikte/o/ortsverbaende/aprspasscode/)

There must be a property file aprs_beacon.properties in the same directory as the py file. It contains credentials for Wunderground and APRS access.

```
wundergroundStationId=<yourWundergroundStationId>
wundergroundApiKey=<yourWundergroundApiKey>
aprsCallsign=<yourCallsign>
aprsPasscode=<yourAprsPasscode>
```

