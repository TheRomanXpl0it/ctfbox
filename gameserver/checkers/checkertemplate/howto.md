# Creating your own checker

To create your own checker you might want to start by copying the template `chekertemplate.py`, as well as the `checklib.py` inside a folder named after your service.

```
your_service/
├── chekertemplate.py
└── checklib.py
```

Each checker must implement three functions which cover the basics of interacting with the service:
- Check SLA
- Put flag
- Get flag

Try to cover as many cases as possible with your checker script, maybe call at random one of two/three functions which interact with the service, to hide the checker behaviour as best as you can.

To post flag ids and make them visible all you need to do is call the function 
```py 
checklib.post_flag_id(flag_id=flag_id)
```
 
and pass a dictionary to it containing the flag_id you wish to share.

While interacting with the service you might want to pay close attention to errors and differences from the behaviour you are expecting and notify the status of the service accordingly, currently there are three statuses to chose from:

- OK
- DOWN
- ERROR

Notify the infrastructore with the error you see fit.

When ending your interaction remember to close the connection or the session as it may put the infrastructure to strain.

## Testing the checker

The checker expects some data from the environment variables to work properly, to run it therefore you must call it like this:
```sh
SERVICE=service-name ACTION=CHECK_SLA|PUT_FLAG|GET_FLAG TEAM_ID=0-9+ FLAG=ABCDEFGHI (32 characters long) python3 checker.py
```

You can change the comand line accordingly to the action you're performing, for example checksla does not need the `$FLAG` var.