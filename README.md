# Quick API for rmm

## This is a quick API to show,search and sort data from [data](https://data.nist.gov/rmm/records)



## RUN

### With Docker
#### Prerequisite 
you need to have docker installed. If you don't, you can download it at [docker](https://www.docker.com/) 

- docker build -t rmm .
- docker run -d -p 5000:5000  rmm

### Local 
#### Prerequisite
Make sure you have python(3.7.3) and pip(22.3.1) installed

- pip install flask
- pip install -r requirements.txt
- python3 rmm/index.py

### Keys from the data 
["_id", "@context", "_schema", "_extensionSchemas", "@type", "@id", "title", "contactPoint", "modified", "status", "ediid", "landingPage", "description", "keyword", "theme", "topic", "references", "accessLevel", "license", "inventory", "components", "publisher", "language", "bureauCode", "programCode","version"]

### Routes
All HTTP methods are supported. You can use http or https for your requests.

* GET	`/data`	 // get all data
* GET	`/data/<key>/<id>`	// get all data from a precise key and precise id, you need to write the key and id
    * `GET /data/ediid/3C53B142D0C3268EE0531A570681EA991497`
* GET	`/getall/<key>`	// get all values of a key
* GET	`/searchkey/<val>`	// get only keys that contains `<val>` in data 
    * `GET /searchkey/Matt`
* GET	`/searchall/<val>` // get all data that contains `<val>` in one of their key
    * `GET /searchall/Matt`

* GET	`/sortkey/<key>`	// get only keys sorted based on `<key>`
    * `GET /sortkey/ediid`
* GET	`/sortall/<key>` // get all data sorted by based `<key>` 
    * `GET /sortall/ediid`

