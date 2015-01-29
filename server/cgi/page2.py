#!/usr/bin/env python

import cgi

form = cgi.FieldStorage()
name = form.getvalue('name')
family = form.getvalue('family')


print "Content-type:text/html"
print
print "<html><head><title>Page2</title></head>"
print "<body><div><label> Name:  %s</label><br/> <label> Family: %s</label><br/></div>" %(name, family)
print """
<div>

<form method=\"post\" action=\"page1.py\">
<span><label> Birth Date: <input type=\"text\" name=\"birthdate\" /></label></span>
<span><label> Main Hobby: <input type=\"text\" name=\"hobby\" /></label></span>
<br/>
<input type=\"submit\" value=\"Submit\">
</div>
</body>
</html>"""