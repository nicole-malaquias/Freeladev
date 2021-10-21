## <font size="7">**FreelaDev**</font>

​
## <font size="6">Base URL https://freela-dev.herokuapp.com/api </font>


## <font size="6">Routes</font>

​
​

### <font color="purple"> GET </font> List of jobs that don't have a developer assigned to it *****

​

```json
freeladev.com/api
```

```json
{
  "name": "SpaceBlog",
  "description": "an website about astronomy",
  "price": 3000,
  "difficulty_level": "beginner",
  "expiration_date": "12/12/2021 23:59",
  "contractor": {"name": "Thiago Almeida",
  "email":"thiagoi43@gmailcom", 
  "cnpj": "13.339.532/0001-09"}
}
```



### <font color="purple"> GET </font> List of developers

​

```json
freeladev.com/api/developers
```

```json
{
  "name": "Vitor Menezes",
  "email": "menezes.vitor@mail.com",
  "birthdate": "17/10/1990",
  "technologies": [{"name": "python"}, {"name": "javascript"}]
}
```





​
### <font color="purple"> GET </font> List of contractors

​

```json
freeladev.com/api/contractors
```

​

```json
{
  "name": "Pedro Musk",
  "email": "pedro.space@mail.com",
  "cnpj": "13.339.532/0001-09"
}
```

​
cnpj can be optional

```json
{
  "name": "Pedro Musk",
  "email": "pedro.space@mail.com",
}
```

# Developer

### <font color="gree"> POST </font> Login (Developer and Contractor)

​

```json
freeladev.com/api/login
```

<font color="caramel"> _Request_ </font>
​

```json
{
  "email": "tiago90@gmail.com",
  "password": "freela123"
}
```

​
<font color="yellow"> _Response_ </font>
​

```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNDc3NzQ2OSwianRpIjoiN2ZmY2YwMmMtNmY5Zi00ZDdjLTgzNWMtNWRkMmNmMjQxODFhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJuYW1lIjoiYmlsbGllIiwiZW1haWwiOiJiaWxsaWVAZ21haWwuY29tIiwiYmlydGhkYXRlIjoiVGh1LCAxMiBEZWMgMjAwMiAwMzowMDowMCBHTVQifSwibmJmIjoxNjM0Nzc3NDY5LCJleHAiOjE2MzQ3NzgzNjl9.GuL7ZL3zwKDndeMDUGXYbInyJ1egt-dngY80TIIiQHo"
}
```

​

### <font color="green"> POST </font> Developer's signup

​

```json
freeladev.com/api/developers/signup
```

<font color="caramel"> _Request_ </font>
​

```json
{
"name": "Kiko Solimões",
"email": "kidakdssxo@mail.com",
"password": "Nino2016*#",
"birthdate": "01/01/2012",
"technologies": [{"name": "python"},
 {"name": "react"}]
}
```

​
<font color="yellow"> _Response_ </font>
​

```json
{
  "name": "Thiago Camargo",
  "email": "thiago.camargo@mail.com",
  "birthdate": "07/07/1998",
  "technologies": [{"name": "python"},
  {"name": "react"}]
}
```

### <font color="purple"> GET </font> Developer's information

​

```json
freeladev.com/api/developers/profile
```

<font color="yellow"> _Response_ </font>
​

```json
{
  "name": "Thiago Camargo",
  "email": "thiago.camargo@mail.com",
  "birthdate": "07/07/1998",
  "technologies": [{"name": "python"},
 {"name": "react"}]
}
```

​

### <font color="orange"> PATCH </font> Update developer information

​

```json
freeladev.com/api/developers/update
```

​
Can contain:
"<font color="lightblue">name</font>",
"<font color="lightblue">email</font>" and/or
"<font color="lightblue">birthdate</font>" and/or
"<font color="lightblue">technologies</font>"
"<font color="caramel"> _Request_ </font>"

```json
{
  "technologies": [{"name": "python"}, {"name": "react"}]
}
```

​
<font color="yellow"> _Response_ </font>
​

```json
{
  "name": "Thiago Camargo",
  "email": "thiago.camargo@mail.com.br",
  "birthdate": "07/07/1998",
  "technologies": [{"name": "python"},
   {"name": "react"}]
}
```

if you want to patch the technologies list you need to request all the previous technologies along with the new one or any modification


### <font color="red"> DELETE </font> Delete Developer

​

```json
freeladev.com/api/developers/delete
```

<font color="yellow"> _Response_ </font>
​

```json
NO CONTENT, 204
```

​

# Contractor routes

​

### <font color="gree"> POST </font> Contractor's signup

​

```json
freeladev.com/api/contractors/signup
```

​
<font color="caramel"> Request </font>
​

```json
{
  "name": "Pedro Musk",
  "email": "pedro.space@mail.com",
  "cnpj": "13.339.532/0001-09",
  "password": "Bertyt2017*#"
}
```

​
<font color="yellow"> _Response_ </font>
​

```json
{
  "name": "Pedro Musk",
  "email": "pedro.space@mail.com",
  "cnpj": "13.339.532/0001-09"
}
```

### <font color="purple"> GET </font> Contractor's information

​

```json
freeladev.com/api/contractor/profile
```

<font color="yellow"> _Response_ </font>
​

```json
{
  "name": "Pedro Musk",
  "email": "pedro.space@mail.com",
  "cnpj": "13.339.532/0001-09"
}
```

​

### <font color="orange"> PATCH </font> Update contractor's information

​

```json
freeladev.com/api/contractor/update
```

​
Body json can contain:
"<font color="lightblue">name</font>",
"<font color="lightblue">email</font>" 
"<font color="lightblue">cnpj</font>"
"<font color="caramel"> _Request_ </font>"
​

```json
{
  "email": "pedro.space@mail.com.br"
}
```

​
<font color="yellow"> _Response_ </font>
​

```json
{
  "name": "Pedro Musk",
  "email": "pedro.space@mail.com.br",
  "cnpj": "13.339.532/0001-09"
}
```

​

### <font color="red"> DELETE </font> Delete Contractor

​

```json
freeladev.com/api/contractor/delete
```

<font color="yellow"> _Response_ </font>
​

```json
NO CONTENT, 204
```

​

# Jobs

​

### <font color="gree"> POST </font> Create a job

​

```json
freeladev.com/api/jobs/create
```

​
<font color="caramel"> _Request_ </font>
​

```json
{
  "name": "SpaceBlog",
  "description": "a website about astronomy",
  "price": 3000,
  "difficulty_level": "beginner",
  "expiration_date": "12/12/2021 23:59"
}
```

​
<font color="yellow"> _Response_ </font>
​

```json
{
    "name": "SpaceBlog",
    "description": "a website about astronomy",
    "price": 3000,
    "difficulty_level": "beginner",
    "expiration_date": "12/12/2021 23:59",
    "progress": null
​
}
```

​

### <font color="purple"> GET </font> Get job by price and difficulty

​

```json
freeladev.com/api/jobs/info?price=3000&difficulty=beginner
```

<font color="yellow"> _Response_ </font>
​
If it's a developer using the route it'll also return:


```json
    {
      "id": 1,
      "name": "SpaceBlog",
      "description": "a website about astronomy",
      "price": 3000.0,
      "difficulty_level": "beginner",
      "expiration_date": "07/07/2022",
      "progress": null,
      "developer": null,
      "contractor": {
        "name": "Kika06",
        "email": "kisaa87@gmail.com",
        "cnpj": "16.466.789/0000-00"
      }
    }
```




### <font color="purple"> GET </font> Information about a specific job

​

```json
freeladev.com/api/job/info/<job_id>
```

<font color="yellow"> _Response_ </font>
​

```json
{
  "id": 63,
  "name": "Project with python",
  "description": "a website about astronomy, using python, react, java, flask, springboot",
  "price": 3000.0,
  "difficulty_level": "beginner",
  "expiration_date": "Sun, 12 Dec 2021 23:59:00 GMT",
  "progress": null,
  "developer": null,
  "contractor": {
    "name": "Rubens",
    "email": "rubesns89@gmail.com",
    "cnpj": "97.789.087/1245-09"
  }
}
```


### <font color="purple"> GET </font> Get job by Tech *****

​

```json
freeladev.com/api/job
```

<font color="yellow"> _Response_ </font>
​

```json
{
  "name": "SpaceBlog",
  "description": "a website about astronomy",
  "price": 3000,
  "difficulty_level": "beginner",
  "expiration_date": "12/12/2021 23:59",
  "progress": "ongoing"
}
```

​
### <font color="purple"> GET </font> Get job by id authenticated *****

​
```json
freeladev.com/api/job/info/<job_id>
```

<font color="yellow"> _Response_ </font>
​

```json
{
  "name": "SpaceBlog",
  "description": "a website about astronomy",
  "price": 3000,
  "difficulty_level": "beginner",
  "expiration_date": "12/12/2021 23:59",
  "progress": "ongoing"
}
```

If it's a developer using the route it'll also return:
​

```json
{
  "contractor": {
    "name": "Rubens",
    "email": "rubesns89@gmail.com",
    "cnpj": "97.789.087/1245-09"
  }
}
```

​
If it's a contractor using the route it'll also return if there's already a developer assigned to the job:
​

```json
{
  "developer": "Thiago Camargo",
  "developer_email": "tiago32@gmail.com",
  "developer_birthday": "01/01/1998"
}
```


### <font color="orange"> PATCH </font> Update a job

​

```json
freeladev.com/api/job/update/<job_id>
```

Body json can contain:
"<font color="lightblue">name</font>",
"<font color="lightblue">description</font>",
"<font color="lightblue">price</font>",
"<font color="lightblue">difficulty\_level</font>",
"<font color="lightblue">expiration\_date</font>" e
"<font color="lightblue">developer: email</font>"


<font color="caramel"> \
_Request_ </font>
​

```json
{
  "developer": "vi32@gmail.com"
}
```

​
<font color="yellow"> \_Response_ </font>
​

```json
{
    "name": "SpaceBlog",
    "description": "a website about astronomy",
    "price": 3000,
    "difficulty_level": "beginner",
    "expiration_date": "12/12/2021 23:59",
    "progress": "ongoing",
    "developer": {"name": "Filipe Ramos",
    "email": "filipe43@gmail.com",
    "birthdate": "01/01/1998"}

}
```

​
​

### <font color="red"> DELETE </font> Delete a job you must owner of the job to delete it 

​

```json
freeladev.com/api/job/delete/<job_id>
```

​
<font color="yellow"> \
_Response_ </font>
​

```json
NO CONTENT, 204
```

​

### <font color="purple"> GET </font> Developer jobs

​

```json
freeladev.com/api/developers/jobs
```

<font color="yellow"> _Response_ </font>
​

```json
[
  {
    "name": "FishWorld",
    "description": "a website about fishing",
    "price": 4000,
    "difficulty_level": "begginer",
    "expiration_date": "06/06/2021 23:59",
    "progress": "completed",
    "contractor": {"name": "Thiago Almeida" "email": "thiagoi43@gmail.com",
    "cnpj": "10.332.532/0002-09"}
  },
  {
    "name": "SpaceBlog",
    "description": "a website about astronomy",
    "price": 3000,
    "difficulty_level": "beginner",
    "expiration_date": "12/12/2021 23:59",
    "progress": "ongoing",
    "contractor": {"name": "Thiago Almeida" "email": "thiagoi43@gmail.com",
    "cnpj": "13.339.532/0001-09"}
  }
]
```

​

### <font color="purple"> GET </font> Contractor jobs

​

```json
freeladev.com/api/contractor/jobs
```

<font color="yellow"> _Response_ </font>
​

```json
[
  {
    "name": "Developers hub",
    "description": "a website about programming",
    "price": 15000,
    "difficulty_level": "advanced",
    "expiration_date": "08/08/2021 23:59",
    "progress": "completed",
    "developer": {
      "name": "Filipe Ramos",
      "email": "filipe43@gmail.com",
      "birthdate": "01/01/1998"
    }
  }
]
```

​
### <font color="purple"> GET </font> Contractor jobs

​

```json
freeladev.com/api/contractors/jobs?progress=None&page=1&per_page=2

```

<font color="caramel"> _Request_ </font>
​

```json
[
  {
    "progress": "completed",
  }
]
```

