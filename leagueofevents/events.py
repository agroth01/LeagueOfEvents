from collections import defaultdict

subscribers = defaultdict(list)

def register_event(event_type, callback):
    subscribers[event_type].append(callback)

def call_event(event_type, data=None):
    if event_type in subscribers:
        for function in subscribers[event_type]:
            if (data == None):
                function()
            else:
                try:
                    function(data)
                except TypeError:
                    raise Exception(event_type + " has a return value.")
