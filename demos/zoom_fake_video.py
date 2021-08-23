# JWT is from Zoom
import jwt
import requests
import json
from time import time

API_KEY = "M6_R9yGdSbanSS7lYMUKJA"
API_SECRET = "f9hS05Rz4N94F6Ar3D0hFOwQk0xN5syPGaDK"

# create a function to generate a token 
# using the pyjwt library
def generateToken():
    token = jwt.encode(
        
        # Create a payload of the token containing:
        # API Key & expiration time
        {'iss': API_KEY, 'exp': time() + 5000},
          
        # Secret used to generate token signature
        API_SECRET,

        # Specify the hashing algorithm
        algorithm = 'HS256'
    )
    return token