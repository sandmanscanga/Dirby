#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# import threading
import argparse
import requests

""" TODO: Divide jobs by number of concurrent threads. """


def parse_url():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-u", "--url", metavar="url",
        type=str, required=False,
        help="specify target base url"
    )
    args = parser.parse_args()
    return args.url


def main():
    baseurl = parse_url()
    baseurl = f"{baseurl}/" if baseurl[-1] != "/" else baseurl
    filename = "/home/adam/Wordlists/Directories/small.txt"
    with open(filename, "r") as f:
        words = f.read().strip().split("\n")
    pads = " "*20
    for word in words:
        url = baseurl + word
        r = requests.get(url)
        if r.status_code != 404:
            print(f"[+] {r.status_code} -> {url}{pads}")
        else:
            print(f"[-] {url}{pads}", end="\r")



if __name__ == "__main__":
    main()
