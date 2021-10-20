
​

### <font color="purple"> GET </font> Information about a specific job

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


### <font color="orange"> PATCH </font> Update a job

​

```json
freeladev.com/api/job/update/<job_id>
```

Body json can contain:
"<font color="lightblue">name</font>",
"<font color="lightblue">description</font>",
"<font color="lightblue">price</font>",
"<font color="lightblue">difficulty\*level</font>",
"<font color="lightblue">expiration\*date</font>" e
"<font color="lightblue">developer*email</font>"
​
<font color="caramel"> \_Request* </font>
​

```json
{
  "developer_email": "vi32@gmail.com"
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
    "progress": "ongoing",
    "developer": {"name": "Filipe Ramos", "email": "filipe43@gmail.com", "birthdate": "01/01/1998"}

}
```

​
​
