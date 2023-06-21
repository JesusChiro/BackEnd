# import {useState} from 'react'
from requests import get

response = get("https://jsonplaceholder.typicode.com/todos/1")

print(response.json())
