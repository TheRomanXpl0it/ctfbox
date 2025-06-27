#!/usr/bin/env python3

import random
import string
import requests
import checklib
import pwn

data = checklib.get_data()
action = data['action']
service_addr = data['host']

def check_sla():
    try:
        pass
    except Exception as e:
        checklib.quit(checklib.Status.ERROR, 'A meaningful error message',e)
    checklib.quit(checklib.Status.OK)

def put_flag():
    flag = data['flag']
    try:
        # interact with the service to put the flag, 
        # at some point some information about the flag needed to retrieve it come up
        # to save them and ensure everything works save the flag data using this function
        # please not that the flag data and flag ids are not the same thing
        # while flag ids are public and can be used to retrieve the flag data,
        # flag data is private and should not be shared with the players
        meaningful_data = {
            "password" : "example_password"
        }
        checklib.save_flag_data(flag=flag,data=meaningful_data)

        # to post flag ids use this function
        flag_id = {
            "username" : "flag_id_username"
        }
        checklib.post_flag_id(flag_id=flag_id)
    except Exception as e:
        checklib.quit(checklib.Status.ERROR, 'Unable to put flag', e)
    checklib.quit(checklib.Status.OK)
    


def get_flag():
    flag = data['flag']

    try:
        # retrieve the flag data stored before
        flag_data = checklib.get_flag_data(flag)
        password = flag_data['password']
        
        # check the real flag by interacting with the service
        # and compare it with the one provided, if they are different, call checklib.quit with Status.DOWN
        
    except Exception as e:
            checklib.quit(checklib.Status.DOWN, 'Unable to retrieve flag data', e)

    checklib.quit(checklib.Status.OK)


def main():
    try:
        if action == checklib.Action.CHECK_SLA.name:
            check_sla()
        elif action == checklib.Action.PUT_FLAG.name:
            put_flag()
        elif action == checklib.Action.GET_FLAG.name:
            get_flag()
    except (requests.RequestException, requests.HTTPError) as e:
        checklib.quit(checklib.Status.DOWN, 'Request error', str(e))
    except KeyError:
        checklib.quit(checklib.Status.ERROR, 'Unexpected response', str(e))


if __name__ == "__main__":
    main()