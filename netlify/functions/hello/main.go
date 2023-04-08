package main

import (
  "github.com/aws/aws-lambda-go/events"
  "github.com/aws/aws-lambda-go/lambda"
)

func handler(request events.APIGatewayProxyRequest) (*events.APIGatewayProxyResponse, error) {
  return &events.APIGatewayProxyResponse{
    StatusCode:        200,
    Body:              "Redeploying latest episode",
  }, nil
}

func main() {
  lambda.Start(handler)
}