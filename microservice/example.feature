Feature: test API

  Scenario Outline: Test a GET/POST/PUT/DELETE request
    Given the API at the URL "http://0.0.0.0:8000"
    When I send a signed <method> request to the "<path>" path
    Then status code <status> should be returned
    Examples:
      |method |path       |status|
      |GET    |/api/user  |200   |
      |POST   |/api/user  |201   |
      |PUT    |/api/user/1|200   |
      |DELETE |/api/user/1|204   |
