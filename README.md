# FSND: Capstone Project

## Motivations

This is a mock site that demonstrate skills that thought throw-out the nano-degree.
It show case the usage of data base to store information.
It show case the usage of API endpoint that demonstrate the CRUD mechanics
It show case the usage of permission based web site
Deployment on Render

<a name="start-locally"></a>

## Start Project locally

Clone this repo.
In the terminal cd to the current repo
type the following command in the terminal to install dependencies

Install the dependencies:

```bash
$ pip install -r requirements.txt
```

Change database config so it can connect to your local postgres database

- Open `config.py` with your editor of choice.
- Here you can see this dict:

```python
database_setup = {
   "database_name_production" : "agency",
   "user_name" : "postgres", # default postgres user name
   "password" : "testpassword123", # if applicable. If no password, just type in None
   "port" : "localhost:5432" # default postgres port
}
```

Once the dependencies finished to download and you made the config changes run the following command

```bash
$ flask --app app.py --debug run
```

To execute tests, run

```bash
$ python test_app.py
```

Here are the access tokens:
(You can find them in the config file)

tokens = {
"casting_assistant": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjE5eWFxTXZWajRSTHJsX25pV2NONSJ9.eyJpc3MiOiJodHRwczovL2Rldi1paXNuMDZ5enJveHY1N3NnLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiI3RnJMeHk4aFB0Vkt4VEZBMVprT2RsdE9UdjM3Y3Q1WEBjbGllbnRzIiwiYXVkIjoiZGV2IiwiaWF0IjoxNjc1NDM5MzI5LCJleHAiOjE2NzYzMDMzMjksImF6cCI6IjdGckx4eThoUHRWS3hURkExWmtPZGx0T1R2MzdjdDVYIiwic2NvcGUiOiJnZXQ6YWN0b3JzIGdldDptb3ZpZXMiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.YUa25rCbByUgEHpMBDN-FaJ4McQrRS3tmxPLc_OP_YCPC0wEZNtPPpxPoGeTJG2NoEEQ-a0FAgkhQcGslbnmS--d62gJVpVj15bHW77ijurCfNMWWjZiC6ZRvvvy3xjnuVD5ykiznwPSy-IfF1wEsgJPBYf8Nkoyd0rCuhLbMbTKdXT95Dl-unPsKk0qK1DeYeEg4RvFXWmgUZpJpi4dqzcn5Z7HkorH1MK3nxRi3IVvhrQXLunx4TOBpkY6u5-Ku9GcRRBrX5kxAuiPAvFG-Ej_G1NLI_J2Ug0tCJmF8bxIR9740wZnDoOw59jp3Rx_IMDfYgHmCpY_ctGa5RnOfA",
"casting_director" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjE5eWFxTXZWajRSTHJsX25pV2NONSJ9.eyJpc3MiOiJodHRwczovL2Rldi1paXNuMDZ5enJveHY1N3NnLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiI3RnJMeHk4aFB0Vkt4VEZBMVprT2RsdE9UdjM3Y3Q1WEBjbGllbnRzIiwiYXVkIjoiZGV2IiwiaWF0IjoxNjc1NDQzNjcwLCJleHAiOjE2NzYzMDc2NzAsImF6cCI6IjdGckx4eThoUHRWS3hURkExWmtPZGx0T1R2MzdjdDVYIiwic2NvcGUiOiJnZXQ6YWN0b3JzIGdldDptb3ZpZXMgZGVsZXRlOmFjdG9yIHBhdGNoOmFjdG9yIHBhdGNoOm1vdmllIHBvc3Q6YWN0b3IiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsImRlbGV0ZTphY3RvciIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIl19.TrS0WGN9JCIaatU-ysnXxZG2cEl3zCdD11RxMtOwNpsVSZUvcfmsE-Emf4i6dOP2hjoTj1MKq_Tj8U8AVMnzwcjntBHE7ex4aRygIgsNlMod5iyxKcr-FpLDWzoA-574bHlpuR8v4jn06j7lnqfRkVoIFq3LgdaeHxouYc8alCcvAZttUr29RNVR-T4wamUCx42v6JqqlVMjNfVX-vLMXlMq1DMiLUpgqKtp_m-KvCUZ4kaEaGifMlUjmGIjv4a5G6HWyQymdd4nZOTW8aJPUKoUiqY995W6gRwf46l-XHThDtVjsysnqLXgVtCfPxXN2N9hzvYj5lnCoRdFXhm38A",
"executive_producer" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjE5eWFxTXZWajRSTHJsX25pV2NONSJ9.eyJpc3MiOiJodHRwczovL2Rldi1paXNuMDZ5enJveHY1N3NnLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiI3RnJMeHk4aFB0Vkt4VEZBMVprT2RsdE9UdjM3Y3Q1WEBjbGllbnRzIiwiYXVkIjoiZGV2IiwiaWF0IjoxNjc1NDQzNjM4LCJleHAiOjE2NzYzMDc2MzgsImF6cCI6IjdGckx4eThoUHRWS3hURkExWmtPZGx0T1R2MzdjdDVYIiwic2NvcGUiOiJnZXQ6YWN0b3JzIGdldDptb3ZpZXMgZGVsZXRlOmFjdG9yIHBhdGNoOmFjdG9yIHBhdGNoOm1vdmllIGRlbGV0ZTptb3ZpZSBwb3N0Om1vdmllIHBvc3Q6YWN0b3IiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsImRlbGV0ZTphY3RvciIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJkZWxldGU6bW92aWUiLCJwb3N0Om1vdmllIiwicG9zdDphY3RvciJdfQ.NlFnoisfjUtEIbCawtvNP840n2lOqPxoOLpibW0O2ITDILfUHNpP5cmhzQ5QlSeBDfKZW98i3-9XL1qGEhQuSNPkNH8gm2-cJ4-hrVLJn2_0ynXV4zDxSdCQ_FhsAQ56OxpPj0uJRBmlOHxU1-MkpE4tdmeyzFJ_LJmzz8VXy_OoCdJSC3JH8TSyaLPzZkQqUQstm0Lt2GXnS3mCqfWrO15fSas35TbVgDbVxT0MsY2xl28wuC7IAyTwWWnwSIS8iD6NBc6VsUiyATtvCiD1dgLFIptlgSFG3SId5ajJf0d2QFAz0GPwyxFS1FO08bWRfRUVwhFqUGOApo036JB06g"
}

## API Documentation

### Base URL

**_https://deploy-sagi.onrender.com/movies_**

### Available Endpoints

### 1. GET /actors

Get the full list of all actors

```bash
https://deploy-sagi.onrender.com/actors
```

- Requires permission: `get:actors`

#### Example response

```js
{
  "actors": [
    {
      "age": 25,
      "gender": "Male",
      "id": 1,
      "name": "Brad Pitt"
    }
  ],
  "success": true
}
```

### 2. GET /actors/actor_id

Get the data on specific actor by id

```bash
https://deploy-sagi.onrender.com/actors/1
```

- Requires permission: `get:actors`

#### Example response

```js
{
  "actors": [
    {
      "age": 25,
      "gender": "Male",
      "id": 1,
      "name": "Brad Pitt"
    }
  ],
  "success": true
}
```

### 3. POST /actors

Insert new actor into database.

```bash
https://deploy-sagi.onrender.com/actors
```

- Require data about the actor: name, age and gender
- Requires permission: `post:actor`

#### Example response

```js
{
    "actor_id": 2,
    "success": true
}

```

### 4. PATCH /actors

Edit an existing Actor

```bash
https://deploy-sagi.onrender.com/actors/1
```

- Require data about the actor: name, age and gender (the actor must be existing before patch)
- Requires permission: `patch:actor`

#### Example response

```js
{
    "success": true,
    "actor_id": 1
}
```

### 5. DELETE /actors

Delete an existing Actor

```bash
https://deploy-sagi.onrender.com/actors/1
```

- The actor must be existing before delete
- Requires permission: `delete:actor`

#### Example response

```js
{
    "id": 5,
    "success": true
}

```

### 1. GET /movies

Get the full list of all movies

```bash
https://deploy-sagi.onrender.com/movies
```

- Requires permission: `get:movies`

#### Example response

```js
{
  "movies": [
    {
      "id": 1,
      "release_date": "Fri, 04 Feb 2023 00:00:00 GMT",
      "title": "Fight Club"
    }
  ],
  "success": true
}
```

### 2. GET /movies/movie_id

Get the data on specific movie by id

```bash
https://deploy-sagi.onrender.com/movies/1
```

- Requires permission: `get:movies`

#### Example response

```js
{
  "movies": [
    {
      "id": 1,
      "release_date": "Fri, 04 Feb 2023 00:00:00 GMT",
      "title": "Fight Club"
    }
  ],
  "success": true
}
```

### 3. POST /movies

Insert new movie into database.

```bash
https://deploy-sagi.onrender.com/movies
```

- Require data about the movie: title and release date
- Requires permission: `post:movie`

#### Example response

```js
{
    "success": true,
    "movie_id": 2
}

```

### 4. PATCH /movies

Edit an existing Movie

```bash
https://deploy-sagi.onrender.com/movies/1
```

- Require data about the movie: name, age and gender (the movie must be existing before patch)
- Requires permission: `patch:movie`

#### Example response

```js
{
    "success": true,
    "movie_id": 1
}
```

### 5. DELETE /movies

Delete an existing Movie

```bash
https://deploy-sagi.onrender.com/movies/1
```

- The movie must be existing before delete
- Requires permission: `delete:movie`

#### Example response

```js
{
    "id": 5,
    "success": true
}

```

### Auth0 to use existing API

If you want to access the real, temporary API, bearer tokens for all 3 roles are included in the config.py file.

## Existing Roles

They are 3 Roles with distinct permission sets:

1. Casting Assistant:

- GET /actors (view:actors): Can see all actors
- GET /movies (view:movies): Can see all movies

2. Casting Director (everything from Casting Assistant plus)

- POST /actors (create:actors): Can create new Actors
- PATCH /actors (edit:actors): Can edit existing Actors
- DELETE /actors (delete:actors): Can remove existing Actors from database
- PATCH /movies (edit:movies): Can edit existing Movies

3. Exectutive Dircector (everything from Casting Director plus)

- POST /movies (create:movies): Can create new Movies
- DELETE /movies (delete:movies): Can remove existing Motives from database
