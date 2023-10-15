# Using API

Basic uses of the api.

# Problem Model
Currently can only create and get instances of the Problem Model, the model has 3 fields problem_id, statement, and content. It's mostly been used for testing. 

## Create Problem
If using powershell run command
```
Invoke-RestMethod -Uri http://localhost:5000/problem -Method POST -Headers @{"Content-Type" = "application/json"} -Body '{"statement": "Sample statement.", "content": "Sample Problem Explanation"}'
{"problem_id": 1, "statement": "Sample statement.", "": "Sample Problem Explanation"}
```
If using terminal use curl command
```
curl -X POST -H "Content-Type: application/json" -d '{"statement": "Sample Problem", "content": "Sample Problem Content"}' http://localhost:5000/problem
```

## Get Problems

Run command 
```
curl http://localhost:5000/problems
```