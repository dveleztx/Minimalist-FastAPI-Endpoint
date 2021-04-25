#!/usr/bin/python3
###############################################################################
# Script      : main.py
# Author      : David Velez
# Date        : 04/25/2021
# Description : First FastAPI Implementation
###############################################################################

# Imports
import fastapi
import uvicorn
from typing import Optional

api = fastapi.FastAPI()


def main():
    print_header()
    uvicorn.run(api, port=8000, host='127.0.0.1')


def print_header():
    print("-" * 25)
    print("    First FastAPI App")
    print("-" * 25)
    print()


@api.get('/')
def index():
    body = "<html>" \
           "<body style='padding: 10px;'>" \
           "<h1>Welcome to the API</h1>" \
           "<div>" \
           "Try it: <a href='/api/calculate?x=7&y=11'>/api/calculate?x=7&y=11</a>" \
           "</div>" \
           "</body>" \
           "</html>"

    return fastapi.responses.HTMLResponse(content=body)


@api.get('/api/calculate')
def calculate(x: int, y: int, z: Optional[int] = None):
    # x and y are required, but z is not, but it is an option
    result = x + y

    # WARNING: Passing a zero will cause an issue! So use FastAPI Response handler!
    if z is not None and z == 0:
        # return fastapi.Response(content='{ "error": "ERROR: Z cannot be zero."}',
        #                         media_type="application/json",
        #                         status_code=400)

        # FastAPI alternative and better way of handling JSON responses rather than the above way
        return fastapi.responses.JSONResponse(content={"error": "ERROR: Z cannot be zero."},
                                              status_code=400)

    if z is not None:
        result /= z

    return {
        'x': x,
        'y': y,
        'z': z,
        'value': result
    }


# Invoke main
if __name__ == '__main__':
    main()
