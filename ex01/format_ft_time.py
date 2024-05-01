import time 

t = time.time();
st = "{:e}".format(t);
day = time.strftime ("%h %d %Y");

print (f"Seconds since January 1, 1970: {t}  or {st} in scientific notation");
print (f"{day}");
