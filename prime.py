"""
A simple service that responds with whether an input (post) is
prime or not.
Usage::
./web-server.py [port]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "num=4" http://localhost
"""


from math import factorial
from flask import Flask,request,json,Response
app = Flask(__name__)


def is_prime(num):
    if num > 1: 
        for i in range(2, num//2):
            if (num % i) == 0:
                return False
        else:
            return True
    return False


def sum_primes(num):
    sum = 0
    while (num > 1):
        if is_prime(num):
            sum = sum+num
        num = num - 1
    return sum


@app.route("/")
def hello():
    return "Server successfully started!"

@app.route("/factorial")
def get_factorial():
    try:
        num = int(request.args.get('num'))
    except TypeError:
        data = {'status':422, 'errormsg': 'Parameter  Not Found'}
    except ValueError:
        data = {'status':422, 'errormsg': 'Parameter Error'}
    else:
        if num>=0:
            data = {
                'status':200,
                'number': num,
                'factorial': factorial(num),
                'msg': 'The factorial of %d is %d' %(num, factorial(num))
            }
        else:
            data = {'status':422, 'errormsg': 'Parameter num should grater than or equal to zreo'}
    return Response(json.dumps(data), mimetype='application/json')



@app.route("/sumprime")
def detect_prime():
    try:
        num = int(request.args.get('num'))
    except TypeError:
        data = {'status':422, 'errormsg': 'Parameter  Not Found'}
    except ValueError:
        data = {'status':422, 'errormsg': 'Parameter Error'}
    else:
        if num>=0:
            data = {
                'status':200,
                'number': num,
                'sumprimes': sum_primes(num),
                'msg':'The sum of all primes less than %d is %d' % (num, sum_primes(num))
            }
        else:
            data = {'status':422, 'errormsg': 'Parameter num should grater than or equal to zreo'}
        
    return Response(json.dumps(data), mimetype='application/json')


@app.route("/isprime")
def api_is_prime():
    try:
        num = int(request.args.get('num'))
    except TypeError:
        data = {'status':422, 'errormsg': 'Parameter  Not Found'}
    except ValueError:
        data = {'status':422, 'errormsg': 'Parameter Error'}
    else:
        if num>=0:
            data = {
                'status':200,
                'number': num,
                'is_prime': is_prime(num),
                'msg': str(num)+ ' is a prime number' if is_prime(num) else str(num)+ ' is a not prime number' 
            }
        else:
            data = {'status':422, 'errormsg': 'Parameter num should grater than or equal to zreo'}
    return Response(json.dumps(data), mimetype='application/json')


app.run()