try:
    5/0
except:
    print("error")
    
try: 
    5/0
except Exception as e:
    print("exception ", type(e), ":", e.args)

try:
    5/0
finally:
    print("oops, just before we run into an exception.")