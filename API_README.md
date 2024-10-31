# Transistor Database API Documentation

## Overview

This REST API allows users to interact with a database of transistors, enabling them to retrieve information and find equivalent transistors. The API serves up to 4000 transistors with various parameters to assist in the selection of suitable electronic components.

## Base URL

`https://api.amateurcraft.tech`

## Endpoints

### 1. **Get Transistor Information by Serial Number Pattern**
- **URL:** `/info/:sn`
- **Method:** `GET`
- **Description:** Retrieves information about transistors whose `Serial Number` matches the given pattern.
- **URL Parameters:**
  - `sn` (string): Starting pattern of the `Serial Number`.
- **Responses:**
  - **200 OK:** Returns a list of matching transistors or detailed information if only one match is found.
    - **Message:** Information or a prompt for a new request.
    - **Result:** Details of transistors in JSON format.
  - **404 Not Found:** No transistors match the pattern.
  - **500 Internal Server Error:** Server error during query execution.

### 2. **Get Transistor Information by ID**
- **URL:** `/info/id/:id`
- **Method:** `GET`
- **Description:** Retrieves information about a specific transistor by its `ID`.
- **URL Parameters:**
  - `id` (integer): The unique identifier of the transistor.
- **Responses:**
  - **200 OK:** Returns detailed information about the specified transistor.
    - **Message:** Information about the transistor.
    - **Result:** Transistor details in JSON format.
  - **400 Bad Request:** ID is not a numeric value.
  - **404 Not Found:** ID is out of valid range.
  - **500 Internal Server Error:** Server error during query execution.

### 3. **Find Equivalent Transistors by Serial Number Pattern**
- **URL:** `/equal/:sn`
- **Method:** `GET`
- **Description:** Finds equivalent transistors based on the given `Serial Number` pattern by comparing specific parameters.
- **URL Parameters:**
  - `sn` (string): Starting pattern of the `Serial Number`.
- **Responses:**
  - **200 OK:** Returns equivalent transistors or a prompt to specify an `ID` if there are multiple matches.
    - **Message:** Equivalent transistors found or no matches.
    - **Result:** List of equivalent transistors or a prompt for more specific input.
  - **404 Not Found:** No transistors match the given pattern.
  - **500 Internal Server Error:** Server error during query execution.

### 4. **Find Equivalent Transistors by ID**
- **URL:** `/equal/id/:id`
- **Method:** `GET`
- **Description:** Finds transistors equivalent to the specified transistor by `ID`, comparing parameters like `Material`, `Structure`, `Pc`, etc.
- **URL Parameters:**
  - `id` (integer): The unique identifier of the transistor.
- **Responses:**
  - **200 OK:** Returns equivalent transistors or a message if none are found.
    - **Message:** Equivalent transistors found or no matches.
    - **Result:** List of equivalent transistors in JSON format.
  - **400 Bad Request:** ID is not a numeric value.
  - **404 Not Found:** ID is out of valid range.
  - **500 Internal Server Error:** Server error during query execution.

## Error Handling

- **400 Bad Request:** Returned when the `ID` parameter is not numeric.
- **404 Not Found:** Returned when no matching records are found or when the `ID` is out of bounds.
- **500 Internal Server Error:** Indicates issues with the database query or server execution.

## Example Requests

### Get Transistor by Serial Number Pattern
**Request:**
```http
GET /info/2N
```
**Response:**
```json
{
  "message": "Too many similar names, new get request to /info/id/{ID of Specific Transistor}",
  "result": [
    { "ID": 1, "TransID": "2N3055" },
    { "ID": 2, "TransID": "2N2222" }
  ]
}
```

### Get Transistor by ID
**Request:**
```http
GET /info/id/123
```
**Response:**
```json
{
  "message": "Information on Transistor 2N3055",
  "result": [
    {
      "ID": 123,
      "TransID": "2N3055",
      "Material": "Si",
      "Structure": "NPN",
      "Pc": 115,
      "Vcb": 100,
      "Vce": 60,
      "Ic": 15,
      "Temp": 200,
      "Ft": 2.5,
      "Cc": 30,
      "Hfe": 20,
      "Package": "TO-3"
    }
  ]
}
```

### Find Equivalent Transistors by Serial Number Pattern
**Request:**
```http
GET /equal/2N
```
**Response:**
```json
{
  "message": "Equivalent Transistor(s) for 2N3055",
  "result": [
    {
      "ID": 124,
      "TransID": "MJ2955",
      "Material": "Si",
      "Structure": "PNP",
      "Pc": 115,
      "Vcb": 100,
      "Vce": 60,
      "Ic": 15,
      "Temp": 200,
      "Ft": 2.5,
      "Cc": 30,
      "Hfe": 20,
      "Package": "TO-3"
    }
  ]
}
```

### Find Equivalent Transistors by ID
**Request:**
```http
GET /equal/id/123
```
**Response:**
```json
{
  "message": "Equivalent Transistor(s) for 2N3055",
  "result": [
    {
      "ID": 124,
      "TransID": "MJ2955",
      "Material": "Si",
      "Structure": "PNP",
      "Pc": 115,
      "Vcb": 100,
      "Vce": 60,
      "Ic": 15,
      "Temp": 200,
      "Ft": 2.5,
      "Cc": 30,
      "Hfe": 20,
      "Package": "TO-3"
    }
  ]
}
```

## Notes

- For matching `Serial Number` patterns, use the starting characters of the `Serial Number`.
- Environment variables (`DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`) are used for database connection configuration.

--- 
