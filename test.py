import winkler_jaro

"""Return approximate string comparator measure (between 0.0 and 1.0)

  DESCRIPTION:
 	Simple test of winkler_jaro string compare

    Implemented for Washington United for Marriage / Approve74.org
    Marriage Hero, who voted who hasn't

"""

print "Testing various string distance with Winkler Jaro"
print


string1="Josh Cohen"
string2="Joshua Cohen"
string3="Joshalot Cohen"
string4="Peter Smith"

print "{0} vs {1} = {2}".format(
	string1,string1,winkler_jaro.compare(string1,string1))
print "{0} vs {1} = {2}".format(
	string1,string2,winkler_jaro.compare(string1,string2))
print "{0} vs {1} = {2}".format(
	string1,string3,winkler_jaro.compare(string1,string3))
print "{0} vs {1} = {2}".format(
	string1,string4,winkler_jaro.compare(string1,string4))
