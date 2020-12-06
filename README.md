## TODO

# MUST HAVE

[ ] - Airport -> {code:String}
[ ] - Aircraft -> { serialnumber:String, manufacturer: String}
[ ] - Flights -> {departure:Airport, arrival: Airport, departureTime: Time, arrivalTime: Time, aircraft: Aircraft}
[ ] - CRUD for aircrafts
[ ] - CRUD for flights
[ ] - CRUD for airports (optional)
[ ] - Allow assignation of aircrafts to flights at creation time and later.
[ ] - Flights departure date > creation date???
[ ] - Flights search by departure and arrival airports.
[ ] - Flights search by departure time range.

# NICE TO HAVE

[ ] - Get all departure airports by time (departure and arrival interval as required, provided as request param)... and for each airport the number of flights and in-flight times for each aircraft (this range time strictly within the time range of the search and the average in minutes).

# TECH SETUP

- Python 2.7 or higher.
- Web framework of choice.
- No UI needed
- but a well documented README is a plus.
- Unit tests
- Code quality
- Standard convention compliance
- Push into a private github repo and allow access to supervisor.
