# Author: Stephen Sheridan
# Date: 14/03/2019

# Whois example output : as can be seen whois output format is not standardised

# Domain:                  itb.ie
# Registration Date:       11-January-1999
# Domain Name: yahoo.com
# Creation Date: 1995-01-18T00:00:00-0800
# domain:        BIT-EXCHANGER.RU
# created:       2016-07-04T15:30:24Z
# Domain name:
#         naturesaid.co.uk
#     Relevant dates:
#         Registered on: 25-Oct-1999

# NOTE: cannot grep with word "created" as it appears in more than one place in whois info

import subprocess
from datetime  import *
from domain_tests import *
import dateutil.parser as p

#url1 = "itb.ie"
url1 = "night-fever.it"

def getDaysAlive(url):
    """
    Uses whois and grep to return number of days a domain has been alive based
    on the created/registered date.

    Parameters:
    argument1 (String): domain to check

    Returns:
    int: -1 No match from whois - domain does not exist
         -2 whois didn't return what we expected - no reg date
         -3 there was a problem parsing a valid date from the whois data

    Note1: This function is dependant on whois and grep being available form the command line
    Note2: This function is also dependant on the dateutil library: pip install py-dateutil
   """
    # Use grep to strip out the part of the output that we need
    grep_filter = " | grep -E \"Registration Date|Registered on|Creation Date|created:|Created:|Registration Time:|No match for domain\""

    # Call the whois and pipe the output to grep
    whois_data = subprocess.Popen("whois " + url + grep_filter, shell=True, stdout=subprocess.PIPE).stdout.read()

    # whois could not find a match for the domain - doesn't exist
    if ("No match for domain" in whois_data):
        return -1

    # Split the output based on carriage returns (each line of output from grep)
    whois_data = whois_data.strip().split('\n')

    # Only one date entry found - should be two ?? (Server followed by creation date of domain)
    if (len(whois_data) == 1):
        return -2

    # Try to parse a datetime object out of the string
    # NOTE: we are assuming that the last entry in the list returned from whois and grep
    # will be the actual registration/creation data of the domain in question: whois_data[-1]
    try:
        # Fingers crossed we get a valid date out of the string
        reg_date =  p.parse(whois_data[-1].lower(), fuzzy=True)
    except:
        return -3

    # Get datetime stamp based on NOW!
    today = datetime.today()
    # Timezone and no timezones can cause problems when comparing
    # Strip timezone info from each datetime object (not a very good idea - fudge!!)
    today = today.replace(tzinfo=None)
    reg_date = reg_date.replace(tzinfo=None)
    # Return the days alive (Diff between dates)
    return today - reg_date


# Test the function with a list of domain names ...........
failed = []
for domain in test_domains:
    days_alive = getDaysAlive(domain)
    if (days_alive == -1):
        failed.append(domain)
    print domain + " days alive = " + str(getDaysAlive(domain))

print "No. of domain names tested: " + str(len(test_domains))
print "No. of failures: " + len(failures)
