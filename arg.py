#!/usr/bin/python3

def my_fct(*arg, **kwargs):
    print("{} - {}".format(args, kwargs))

my_fct()
my_fct("Best")
my_fcf("Best", 89)
my_fct(name="Best")

