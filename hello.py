#!/usr/bin/env python3

#list(os.environ.keys()) for question 1
# we did curl localhost:8080/hello.py while cgi_server was running to get output
# on our browser, go to localhost:8080/hello.py
import os
import json
import templates
import sys
# Content-Type: text/plain is plaintext
# can add headers before blank line

# Serve environment back as JSON.
# print('Content-type: application/json') # Displays on web page. Tells webserver that data sent is json
# print() # blank line needed
# print(json.dumps(dict(os.environ),indent=2))

# Report values of query parameters in HTML
# print("Content-Type: text/html")
# print()
# print("""
# <!doctype html>
# <html>
# <body>
# """)
# print(f"<p> QUERY_STRING={os.environ['QUERY_STRING']}</p>")
# print("<ul>")
# # em is for emphasis, not exactly italics/bold/etc.
# for parameter in os.environ['QUERY_STRING'].split('&'):
#     (name, value) = parameter.split('=')
#     print(f"<li><em>{name}</em> = {value}</li>")
# print("</ul>")
# print("""</body>
# </html>
# """)


# Report the user’s browser in the HTML
# print("Content-Type: text/html")
# print()
# print("""
# <!doctype html>
# <html>
# <body>
# """)
# print(f"<p>{os.environ.get('HTTP_USER_AGENT',0)}</p>")
# print("""</body>
# </html>
# """)



# contain a login form that POSTs to itself. report the values of the POSTed data in the HTML.
print(templates.login_page())



# # Inspect Page Source to see what is printed from code
# # HTTP_USER_AGENT is for Question 3
# #Remember to cite your sources. Say which site, which date accessed, and which author
# # QUERY_STRING for question 2 http://localhost:8080/hello.py?sponsor=raycon 
# # http://localhost:8080/hello.py?sponsor=raycon&canadians=getnone
# print("""
# <!doctype html>
# <html>
# <body>
# <h1>HELLO I AM HTML</h1>
# """)