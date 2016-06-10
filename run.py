#!/usr/bin/env python
import time
import sys
import os
import json

def main(args):
    if "timeout" in args:
        count = 1
        while True:
            #print "sleepin till i die (%s)" % count
            time.sleep(10)
            count += 1

    exit_code = 0
    if "pass" in args:
        exit_code = 0
        print "This task is going to pass."

    if "fail" in args:
        exit_code = 1
        print "This task is going to FAIL."

    if "results" in args:
        json_out = open('results.json', 'w')
        out_results = {
                "results":[
                    {
                        "status":"pass",
                        "test_file":"test_1",
                        "exit_code":0,
                        "elapsed":0.32200002670288086,
                        "start":1398782500.359,
                        "end":1398782500.681,
                        "url":"url1",
                        "raw_url":"rawurl1"
                        },
                    {
                        "status":"pass",
                        "test_file":"test_2",
                        "exit_code":0,
                        "elapsed":0.16000008583068848,
                        "start":1398782500.681,
                        "end":1398782500.841,
                        "url":"url2",
                        "raw_url":"rawurl2"
                        },
                    {
                        "status":"fail",
                        "test_file":"test_3",
                        "exit_code":0,
                        "elapsed":0.1679999828338623,
                        "start":1398782500.841,
                        "end":1398782501.009,
                        "url":"url3",
                        "raw_url":"rawurl3"
                        },
                    ]
                }
        json.dump(out_results, json_out)
    sys.exit(exit_code)

if __name__ == "__main__":
    main(sys.argv[1:])
