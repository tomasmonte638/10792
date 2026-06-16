{
      "predicates": [
        { "method": "GET", "path": "/api/marcas" }
      ],
      "responses": [{
        "statusCode": 200,
        "headers": { "Content-Type": "application/json" },
        "body": {
          "marcas": ["Toyota", "Audi", "Ford", "Volvo", "Honda", "BMW"]
        }
      }]
    }