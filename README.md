# Aircraft Logger App

## TODO - MUST HAVE

- [x] Airport -> {code:String}
- [x] Aircraft -> { serialnumber:String (PK), manufacturer: String}
- [x] Flights -> {departure:Airport, arrival: Airport, departureTime: Time, arrivalTime: Time, aircraft: Aircraft}
- [x] CRUD for aircrafts
- [x] CRUD for flights
- [x] CRUD for airports (optional)
- [x] Allow assignation of aircrafts to flights at creation time and later.
- [x] Flights departure date > creation date
- [x] Flights arrival date > departure date
- [x] Flights search by departure and arrival airports.
- [x] Flights search by departure time range.

## TODO - NICE TO HAVE

- [x] Get all departure airports by time (departure and arrival interval as required, provided as request param)... and for each airport the number of flights and in-flight times for each aircraft (this range time strictly within the time range of the search and the average in minutes).

## TODO - TECH SETUP

- [x] Python 2.7 or higher.
- [x] Web framework of choice.
- [x] No UI needed
- [x] But a well documented README is a plus.
- [x] Unit tests
- [x] Code quality
- [x] Standard convention compliance
- [x] Push into a private github repo and allow access to supervisor.
