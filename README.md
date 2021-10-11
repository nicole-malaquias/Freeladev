## <font size="7">**FreelaDev**</font>

​

## <font size="6">Rotas</font>

​

# Listas

​

### <font color="purple"> GET </font> Lista de Jobs

​

```json
freeladev.com/api
```

<font color="yellow"> _Retorno_ </font>
​

```json
{
  "name": "SpaceBlog",
  "description": "um site sobre noticias do mundo espacial",
  "price": 3000,
  "difficulty_level": "beginner",
  "expiration_date": "12/12/2021 23:59",
  "progress": null,
  "contractor": "Pedro Musk"
}
```

### <font color="purple"> GET </font> Lista de Developers

​

```json
freeladev.com/api/developers
```

​
<font color="yellow"> _Retorno_ </font>
​

```json
{
  "name": "Vitor Menezes",
  "email": "menezes.vitor@mail.com",
  "birthdate": "17/10/1990"
}
```

​

### <font color="purple"> GET </font> Lista de Contractors

​

```json
freeladev.com/api/contractors
```

<font color="yellow"> _Retorno_ </font>
​

```json
{
  "name": "Pedro Musk",
  "email": "pedro.space@mail.com",
  "cnpj": "123.456.789/0000-00"
}
```

​

# Developer

### <font color="gree"> POST </font> Login (Developer e Contractor)

​

```json
freeladev.com/api/login
```

<font color="caramel"> Body </font>
​

```json
{
  "name": "Thiago Camargo",
  "password": "freela123"
}
```

​
<font color="yellow"> _Retorno_ </font>
​

```json
{
  "acess_token": "SnwWei31203kj"
}
```

​

### <font color="green"> POST </font> Signup do Developer

​

```json
freeladev.com/api/developer/signup
```

<font color="caramel"> Body </font>
​

```json
{
  "name": "Thiago Camargo",
  "email": "thiago.camargo@mail.com",
  "birthdate": "07/07/1998"
}
```

​
<font color="yellow"> _Retorno_ </font>
​

```json
{
  "name": "Thiago Camargo",
  "email": "thiago.camargo@mail.com",
  "birthdate": "07/07/1998"
}
```

### <font color="purple"> GET </font> Informações do Developer

​

```json
freeladev.com/api/developer/profile
```

<font color="yellow"> _Retorno_ </font>
​

```json
{
  "name": "Thiago Camargo",
  "email": "thiago.camargo@mail.com",
  "birthdate": "07/07/1998"
}
```

​

### <font color="orange"> PATCH </font> Atualizar informações do Developer

​

```json
freeladev.com/api/developer/update
```

​
Poderá conter
"<font color="lightblue">name</font>",
"<font color="lightblue">email</font>" e
"<font color="lightblue">birthdate</font>"
​
<font color="caramel"> Body </font>
​

```json
{
  "email": "thiago.camargo@mail.com.br"
}
```

​
<font color="yellow"> _Retorno_ </font>
​

```json
{
  "name": "Thiago Camargo",
  "email": "thiago.camargo@mail.com.br",
  "birthdate": "07/07/1998"
}
```

​

### <font color="red"> PATCH </font> Delete Developer

​

```json
freeladev.com/api/developer/delete
```

<font color="yellow"> _Retorno_ </font>
​

```json
NO CONTENT, 204
```

​

# Contractor

​

### <font color="gree"> POST </font> Signup do Contractor

​

```json
freeladev.com/api/contractor/signup
```

​
<font color="caramel"> Body </font>
​

```json
{
  "name": "Pedro Musk",
  "email": "pedro.space@mail.com",
  "cnpj": "123.456.789/0000-00"
}
```

​
<font color="yellow"> _Retorno_ </font>
​

```json
{
  "name": "Pedro Musk",
  "email": "pedro.space@mail.com",
  "cnpj": "123.456.789/0000-00"
}
```

### <font color="purple"> GET </font> Informações do Contractor

​

```json
freeladev.com/api/contractor/profile
```

<font color="yellow"> _Retorno_ </font>
​

```json
{
  "name": "Pedro Musk",
  "email": "pedro.space@mail.com",
  "cnpj": "123.456.789/0000-00"
}
```

​

### <font color="orange"> PATCH </font> Atualizar informações do Contractor

​

```json
freeladev.com/api/contractor/update
```

​
Body poderá conter
"<font color="lightblue">name</font>",
"<font color="lightblue">email</font>" e
"<font color="lightblue">cnpj</font>"
​
<font color="caramel"> Body </font>
​

```json
{
  "email": "pedro.space@mail.com.br"
}
```

​
<font color="yellow"> _Retorno_ </font>
​

```json
{
  "name": "Pedro Musk",
  "email": "pedro.space@mail.com.br",
  "cnpj": "123.456.789/0000-00"
}
```

​

### <font color="red"> PATCH </font> Delete Contractor

​

```json
freeladev.com/api/contractor/delete
```

<font color="yellow"> _Retorno_ </font>
​

```json
NO CONTENT, 204
```

​

# Jobs

​

### <font color="gree"> POST </font> Criar um Job

​

```json
freeladev.com/api/job/create
```

​
<font color="caramel"> Body </font>
​

```json
{
  "name": "SpaceBlog",
  "description": "um site sobre noticias do mundo espacial",
  "price": 3000,
  "difficulty_level": "beginner",
  "expiration_date": "12/12/2021 23:59"
}
```

​
<font color="yellow"> _Retorno_ </font>
​

```json
{
    "name": "SpaceBlog",
    "description": "um site sobre noticias do mundo espacial",
    "price": 3000,
    "difficulty_level": "beginner",
    "expiration_date": "12/12/2021 23:59",
    "progress": null
​
}
```

​

### <font color="purple"> GET </font> Informações do Job e ver seu Developer/Contractor

​

```json
freeladev.com/api/job/info/<job_id>
```

<font color="yellow"> _Retorno_ </font>
​

```json
{
  "name": "SpaceBlog",
  "description": "um site sobre noticias do mundo espacial",
  "price": 3000,
  "difficulty_level": "beginner",
  "expiration_date": "12/12/2021 23:59",
  "progress": "ongoing"
}
```

Caso for o Developer que estiver visualizando também terá
​

```json
{
  "contractor": "Pedro Musk"
}
```

​
Caso for o Contractor que estiver visualizando também terá
​

```json
{
  "developer": "Thiago Camargo"
}
```

​

### <font color="orange"> PATCH </font> Atualizar o Job

​

```json
freeladev.com/api/job/update/<job_id>
```

Body poderá conter
"<font color="lightblue">name</font>",
"<font color="lightblue">description</font>",
"<font color="lightblue">price</font>",
"<font color="lightblue">difficulty_level</font>",
"<font color="lightblue">expiration_date</font>" e
"<font color="lightblue">developer</font>"
​
<font color="caramel"> Body </font>
​

```json
{
  "developer": "Vitor Menezes"
}
```

​
<font color="yellow"> _Retorno_ </font>
​

```json
{
    "name": "SpaceBlog",
    "description": "um site sobre noticias do mundo espacial",
    "price": 3000,
    "difficulty_level": "beginner",
    "expiration_date": "12/12/2021 23:59",
    "progress": "ongoing",
    "developer": "Vitor Menezes"
​
}
```

​

### <font color="red"> Delete </font> Deletar o Job

​

```json
freeladev.com/api/job/delete/<job_id>
```

​
<font color="yellow"> _Retorno_ </font>
​

```json
NO CONTENT, 204
```

​

### <font color="purple"> GET </font> Trabalhos do Developer

​

```json
freeladev.com/api/contractor/jobs
```

​
<font color="yellow"> _Retorno_ </font>
​

```json
[
  {
    "name": "FishWorld",
    "description": "um site o mundo da pesca esportiva",
    "price": 4000,
    "difficulty_level": "beginner",
    "expiration_date": "06/06/2021 23:59",
    "progress": "completed",
    "developer": "Thiago Camargo"
  },
  {
    "name": "SpaceBlog",
    "description": "um site sobre noticias do mundo espacial",
    "price": 3000,
    "difficulty_level": "beginner",
    "expiration_date": "12/12/2021 23:59",
    "progress": "ongoing",
    "developer": "Thiago Camargo"
  }
]
```

​

### <font color="red"> Delete </font> Deletar o Job

​

```json
freeladev.com/api/job/delete/<job_id>
```

​
<font color="yellow"> _Retorno_ </font>
​

```json
NO CONTENT, 204
```

​

### <font color="purple"> GET </font> Trabalhos do Developer

​

```json
freeladev.com/api/developer/jobs
```

<font color="yellow"> _Retorno_ </font>
​

```json
[
  {
    "name": "FishWorld",
    "description": "um site com tudo sobre a pesca esportiva",
    "price": 4000,
    "difficulty_level": "begginer",
    "expiration_date": "06/06/2021 23:59",
    "progress": "completed",
    "developer": "Thiago Camargo"
  },
  {
    "name": "SpaceBlog",
    "description": "um site sobre noticias do mundo espacial",
    "price": 3000,
    "difficulty_level": "beginner",
    "expiration_date": "12/12/2021 23:59",
    "progress": "ongoing",
    "developer": "Thiago Camargo"
  }
]
```

​

### <font color="purple"> GET </font> Trabalhos do Contractor

​

```json
freeladev.com/api/contractor/jobs
```

<font color="yellow"> _Retorno_ </font>
​

```json
[
  {
    "name": "SpaceAtlas",
    "description": "um site com o mapa do céu",
    "price": 15000,
    "difficulty_level": "advanced",
    "expiration_date": "08/08/2021 23:59",
    "progress": "completed",
    "developer": "Filipe Ramos"
  },
  {
    "name": "SpaceBlog",
    "description": "um site sobre noticias do mundo espacial",
    "price": 3000,
    "difficulty_level": "beginner",
    "expiration_date": "12/12/2021 23:59",
    "progress": "ongoing",
    "developer": "Thiago Camargo"
  }
]
```

​
