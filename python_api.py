# coding:utf-8 Copy Right Atelier UEDA © 2018 -
#
### An Example of FaunaDB python api
# 
# refer https://docs.fauna.com/fauna/current/tutorials/crud_examples
#
# © Dr. Takeyuki UEDA
#
###
import os
from faunadb.client import FaunaClient
from faunadb.objects import Ref
from faunadb import query as q

client = FaunaClient(secret=os.environ['FAUNADB_SECRET'])

# CRUD examples

## Databases

### Create a database
client.query(q.create_database({ "name": "annuvin" }))

### Paginate all databases
client.query(q.paginate(q.databases()))

### Get a database
client.query(q.get(q.database("annuvin")))

### Rename a database
client.query(q.update(q.database("annuvin"), { "name": "llyr" }))

### Annotate a database
client.query(
  q.update(q.database("llyr"), { "data": { "env": "test" } }))

### Delete a database
client.query(q.delete(q.database("llyr")))

## Keys
client.query(q.create_database({ "name": "caledonia" }))

### Create a key
ref = client.query(
  q.create_key(
    { "database": q.database("caledonia"), "role": "server" }))

### Paginate all keys
client.query(q.paginate(q.keys()))

### Get a key
#client.query(q.get(q.ref(q.keys(), "243725029947212288")))
client.query(q.get(q.ref(q.keys(), ref["ref"].id())))

### Delete a key
#client.query(q.delete(q.ref(q.keys(), "243725029947212288")))
client.query(q.delete(q.ref(q.keys(), ref["ref"].id())))

client.query(q.delete(q.database("caledonia")))

## Collections

### Create a collection
client.query(q.create_collection({ "name": "spells" }))

### Paginate all collections
client.query(q.paginate(q.collections()))

### Get a collection
client.query(q.get(q.collection("spells")))

### Rename a collection
client.query(
  q.update(
    q.collection("spells"), { "name": "dilapidated_huts" }))

### Delete a collection
client.query(q.delete(q.collection("dilapidated_huts")))

### Create a document in a collection
client.query(q.create_collection({ "name": "spells" }))
client.query(
  q.create(
    q.collection("spells"), { "data": { "name": "Fire Beak", "element": ["air", "fire"] } }))
client.query(q.delete(q.collection("spells")))

