#!/usr/bin/env python

import cgi

form = cgi.FieldStorage()
birthdate = form.getvalue('birthdate')
hobby = form.getvalue('hobby')

print "Content-type:text/html"
print
print "<html><head><title>Page1</title></head>"
print "<body><div><label> Birth Date:  %s</label><br/> <label> Main Hobby: %s</label><br/></div>" %(birthdate, hobby)
print """
<div>

<form method=\"post\" action=\"page2.py\">
<span><label> Name: <input type=\"text\" name=\"name\" /></label></span>
<span><label> Family: <input type=\"text" name=\"family\" /></label></span>
<br/>
<input type=\"submit\" value=\"Submit\">
</div>
</body>
</html>"""