#!/usr/bin/env python

print """Content-type:text/html

<form method="post" action="test_form.py">
<textarea name="comments" col="40" rows="5">
Enter Commens here ...
</textarea>
<br/>
<input type="submit" value="Submit">
</form>"""