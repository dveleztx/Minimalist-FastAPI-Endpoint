#!/usr/bin/python3
###############################################################################
# Script      : main.py
# Author      : David Velez
# Date        : 04/25/2021
# Description : First FastAPI Implementation
###############################################################################

# Import
import fastapi
import uvicorn

api = fastapi.FastAPI()


def main():
    print_header()
    calculate()
    uvicorn.run(api, port=8000, host='127.0.0.1')


def print_header():
    print("-" * 25)
    print("    First FastAPI App")
    print("-" * 25)
    print()


@api.get('/api/calculate')
def calculate():
    value = 2 + 2

    return {
        'value': value
    }


# Invoke main
if __name__ == '__main__':
    main()
