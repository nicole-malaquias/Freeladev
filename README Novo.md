## <font size="7">**FreelaDev**</font>

​

## <font size="6">Routes</font>



# Base Routes

### <font color="gree"> POST </font> Login (Developer and Contractor) | TESTADA

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


<font color="yellow"> _Response_ </font>
​

```json
{
  "acess_token": "SnwWei31203kj"
}
```

​


### <font color="purple"> GET </font> List of jobs that don't have a developer assigned to it | TESTADA

​

```json
freeladev.com/api
```

<font color="yellow"> _Response_ </font>

```json
{
    "name": "job 111",
    "description": "Emprego legal",
    "price": 3000.0,
    "difficulty_level": "begine",
    "expiration_date": "Fri, 12 Nov 2021 00:00:00 GMT",
    "progress": null,
    "developer": null,
    "contractor": {
      "name": "user 333",
      "email": "333@gmail.com",
      "cnpj": "48.118.183/7788-88"
    }
  }
```


# Contractor routes


### <font color="purple"> GET </font> List of contractors | TESTADA

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


### <font color="gree"> POST </font> Contractor's signup | TESTADA

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


### <font color="purple"> GET </font> Contractor's information | TESTADA

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
### <font color="orange"> PATCH </font> Update contractor's information | TESTADA

​

```json
freeladev.com/api/contractor/update
```

​
Body json can contain:
"<font color="lightblue">name</font>",
"<font color="lightblue">email</font>" and/or
"<font color="lightblue">cnpj</font>"
​\
<font color="caramel"> _Request_ </font>
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

### <font color="red"> DELETE </font> Delete Contractor | TESTADA

​

```json
freeladev.com/api/contractor/delete
```

<font color="yellow"> _Response_ </font>
​

```json
NO CONTENT, 204
```



### <font color="purple"> GET </font> Contractor jobs | TESTADA

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
  },
  {
    "name": "SpaceBlog",
    "description": "a website about astronomy",
    "price": 3000,
    "difficulty_level": "beginner",
    "expiration_date": "12/12/2021 23:59",
    "progress": "ongoing",
    "developer": {
      "name": "Filipe Ramos",
      "email": "filipe43@gmail.com",
      "birthdate": "01/01/1998"
    }
  }
]
```


​
### <font color="purple"> GET </font> Contractor jobs Query Params | TESTADA

​

```json
freeladev.com/api/contractors/jobs/progress?progress=None&page=1&per_page=1


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



​


# Developers routes

### <font color="purple"> GET </font> List of developers | TESTADA

​

```json
freeladev.com/api/developers
```

```json
{
  "name": "Vitor Menezes",
  "email": "menezes.vitor@mail.com",
  "birthdate": "17/10/1990"
}
```

### <font color="purple"> GET </font> Get profile info | TESTADA

​

```json
freeladev.com/api/developers/profile
```

```json
{
  "name": "Vitor Menezes",
  "email": "menezes.vitor@mail.com",
  "birthdate": "17/10/1990"
}
```

​
### <font color="green"> POST </font> Developer's signup | TESTADA

​

```json
freeladev.com/api/developers/signup
```

<font color="caramel"> _Request_ </font>
​

```json
{
"name": "Eduardo Cunha",
"email": "educu@mail.com",
"password": "Nino2016*#",
"birthdate": "01/01/2012",
"technologies": [{"name": "python"}, {"name": "javascript"}]
}
```

​
<font color="yellow"> _Response_ </font>
​

```json
{
  "name": "Eduardo Cunha",
  "email": "educu@mail.com",
  "birthdate": "01/01/2012",
  "technologies": [
    "python",
    "javascript"
  ]
}
```


### <font color="orange"> PATCH </font> Update developer information | TESTADA

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

<font color="caramel"> _Request_ </font>

```json
{
  "technologies": [{"name": "python"}, {"name": "javascript"}]
}
```

​
<font color="yellow"> _Response_ </font>
​

```json
{
  "name": "Kevin Gomes",
  "email": "kevin@mail.com",
  "birthdate": "01/01/2012",
  "technologies": [
    {
      "name": "Python"
    },
    {
      "name": "Javascript"
    }
  ]
}
```

if you want to patch the technologies list you need to request all the previous technologies along with the new one or any modification



### <font color="red"> DELETE </font> Delete Developer | TESTADA

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
### <font color="purple"> GET </font> Developer jobs | ROTA NÃO EXISTE

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
    "contractor": {"name": "Thiago Almeida" "email": "thiagoi43@gmail.com", "cnpj": "10.332.532/0002-09"}
  },
  {
    "name": "SpaceBlog",
    "description": "a website about astronomy",
    "price": 3000,
    "difficulty_level": "beginner",
    "expiration_date": "12/12/2021 23:59",
    "progress": "ongoing",
    "contractor": {"name": "Thiago Almeida" "email": "thiagoi43@gmail.com", "cnpj": "13.339.532/0001-09"}
  }
]
```

# Jobs

​

### <font color="gree"> POST </font> Create a job | TESTADA

​

```json
freeladev.com/api/job/create
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
    "progress": null,
    "developer": null
​
}
```

### <font color="purple"> GET </font> Get job by Tech

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

If it's a developer using the route it'll also return:
​

```json
{
  "contractor_name": "Thiago Camargo",
  "contractor_email": "tiago54@gmail.com",
  "contractor_cnpj": "47.812.481/0001-02"
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



### <font color="red"> Delete </font> Delete a job

​

```json
freeladev.com/api/job/delete/<job_id>
```

​
<font color="yellow"> _Response_ </font>
​

```json
NO CONTENT, 204
```

​