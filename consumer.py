#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A script to create a consumer on Kong API

"""

import requests
import os


KONG_ADMIN_URL = os.environ.get('KONG_ADMIN_URL')
KONG_ADMIN_KEY = os.environ.get('KONG_ADMIN_KEY')
KONG_CONSUMER = os.environ.get('KONG_CONSUMER')
KONG_CONSUMER_CUSTOM_ID = os.environ.get("KONG_CONSUMER_CUSTOM_ID")
KONG_CONSUMER_API_KEY =  os.environ.get("KONG_CONSUMER_API_KEY")


def create_consumer():
    """
    Creates a consumer on Kong
    TODO: Add get or create functionality
    """
    if not KONG_ADMIN_URL or not KONG_CONSUMER or not KONG_ADMIN_KEY:
        raise Exception("Missing KONG_ADMIN_URL or KONG_CONSUMER")

    url = "{}/consumers/?apikey"
    resp = requests.post(
        url.format(KONG_ADMIN_URL),
        {
            "username": KONG_CONSUMER,
            "custom_id": KONG_CONSUMER_CUSTOM_ID
        },
        headers={
            "x-api-key": KONG_ADMIN_KEY
        } 
    )
    if resp.status_code != 201:
        raise Exception("Failed Creating Consumer")


def create_api_key():
    """
    Adds API Key To Consumer
    """
    if not KONG_ADMIN_URL or not KONG_CONSUMER or not KONG_ADMIN_KEY:
        raise Exception("Missing KONG_ADMIN_URL or KONG_CONSUMER")

    url = "{}/consumers/{}/key-auth"
    resp = requests.post(
        url.format(KONG_ADMIN_URL, KONG_CONSUMER),
        {
            "key": KONG_CONSUMER_API_KEY
        },
        headers={
            'x-api-key': KONG_ADMIN_KEY
        } 
    )
    if resp.status_code != 201:
        raise Exception("Failed Creating API KEY")


def main():
    create_consumer()
    create_api_key()


if __name__ == "__main__":
    main()
