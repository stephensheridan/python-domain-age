# python-domain-age
Python script that uses whois and grep to return the age of a domain name in days

Author: Stephen Sheridan
Date: 14/03/2019

Different whois server and locations will return data particularly the date of creation/registration in different formats. See examples below:

Example 1
Domain:                  itb.ie
Registration Date:       11-January-1999

Example 2
Domain Name: yahoo.com
Creation Date: 1995-01-18T00:00:00-0800

Example 3
domain:        BIT-EXCHANGER.RU
created:       2016-07-04T15:30:24Z

Example 4
Domain name:
        naturesaid.co.uk
    Relevant dates:
        Registered on: 25-Oct-1999

This makes finding and parsing creation/registraiton dates out of whois output difficult. This program takes a very naive approach to the problem and looks for a number of specific creation/registration keywords and then uses dateutil.parser to parse a date out of the whois string data.

NOTE: there may be more than one match from grep for a domain so this script assumes that the last entry in the data returned from whois will be the actual domain creation/registration date.
