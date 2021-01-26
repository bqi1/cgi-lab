import os
import sys
import templates
import secret
import time
u_query = "username="
p_query = "&password="

# From Mosiur at https://stackoverflow.com/questions/20898394/how-to-read-cookie-in-python at 2021-01-26
if "HTTP_COOKIE" in os.environ:
    cookies = os.environ["HTTP_COOKIE"].split('; ')
    if "secret=true" in cookies:
        print(templates.secret_page(secret.username,secret.password))

posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
if posted_bytes:
    posted = sys.stdin.read(int(posted_bytes))
    # Report the values of the POSTed data in the HTML
    # print("Content-Type: text/html")
    # print()
    # print(f"<p> POSTED: <pre>")
    # print(posted)
    # print("</pre></p>")
    # Modify to set a cookie if the login is correct

    username = posted[len(u_query):posted.find(p_query)]
    password = posted[posted.find(p_query)+len(p_query):]
    if username == secret.username and password == secret.password:
        print(f"Set-Cookie: secret=true")
        print(templates.secret_page(secret.username,secret.password))
    else:
        print(f"Set-Cookie: secret=false")