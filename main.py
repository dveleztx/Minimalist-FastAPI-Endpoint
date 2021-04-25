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


@api.get('/api/calculate')
def calculate(x: int, y: int, z: Optional[int] = None):
    # x and y are required, but z is not, but it is an option
    result = x + y

    # WARNING: Passing a zero will cause an issue! So use FastAPI Response handler!
    if z == 0:
        return fastapi.Response(content='{ "error": "ERROR: Z cannot be zero."}',
                                media_type="application/json",
                                status_code=400)

    if z is not None:
        result /= z

    return {
        'value': result
    }


# Invoke main
if __name__ == '__main__':
    main()
