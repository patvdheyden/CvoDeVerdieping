import re

text = "<html><head><title>List of persons with ids</title>\
</head><body>\
<p><id>123123123</id><name>Groucho Marx</name>\
<p><id>123123124</id><name>Harpo Marx</name>\
<p><id>123123125</id><name>Chico Marx</name>\
<randomcrap>Etaoin<id>Shrdlu</id>qwerty</name></randomcrap>\
<nocrap><p><id>123123126</id><name>Zeppo Marx</name></nocrap>\
<address>Chicago</address>\
<morerandomcrap><id>999999999</id>nonametobeseen!\
</morerandomcrap>\
<p><id>123123127</id><name>Gummo Marx</name>\
<note>Look him up on <a href=\"http://www.google.com\">\
Google.</a></note>\
</body></html>"