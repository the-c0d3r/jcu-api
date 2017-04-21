# JCU API


This is a simple flask API that basically does the same thing as [JCU-Daily-Course-Info](https://github.com/the-c0d3r/jcu-daily-course-info) project but this is intended to be running as a RESTful API server. The application just need to query the API using the following endpoints and it will return in JSON format. 


API End Points
---

URL : `localhost/classinfo`  
GET/POST parameter : `classname=CPXXXX`

This end point is used to get the information of a **single** class. It will return `None` if it is empty. 

URL : `localhost/roominfo`  
GET/POST parameter : `room=XX-XX`

This end point is used to get the information of a **single** room. It will return `None` if it is empty.  

URL : `localhost/getclasses`  
GET/POST parameter : `codes=CPXXX,CPXXX,CPXXX`  

This end point will return the related information about the classes using the subject codes provided


Data Format
---

This API returns standard JSON format strings. A typical format is as follows.

```json
{
    "count": 0,
    "result": []
}
```
When the result exists
```json
{
    "count": 1,
    "result": [
    {
        "name": "xxxx",
        "room": "xx-xx",
        "time": "xx:xx - xx:xx",
        "type": "xxxx"
    }
    ]
}
```

