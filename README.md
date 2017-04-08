# JCU API


This is a simple flask API that basically does the same thing as [JCU-Daily-Course-Info](https://github.com/the-c0d3r/jcu-daily-course-info) project but this is intended to be running as a RESTful API server. The application just need to query the API using the following endpoints and it will return in JSON format. 


API End Points
---

URL : `localhost/classinfo`  
POST parameter : `classname=CPXXXX`

This end point is used to get the information of a **single** class. It will return `None` if it is empty. 



URL : `localhost/roominfo`  
POST parameter : `room=XX-XX`

This end point is used to get the information of a **single** room. It will return `None` if it is empty. 
