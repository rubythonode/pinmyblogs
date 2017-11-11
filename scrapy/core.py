from __future__ import print_function

import re
import urllib2


def core(url=None):
    details={}
    details['domain_name']=url

    details['title']="Not-Defined"

    if (url is not None):

        match=re.search(r'(https?\:\/\/){1,}', url, re.M)

        if (match):
            domain=url.split("://")
            domain=domain[1:]
            domain=domain[0]
            # print (domain)
            domain=domain.split("/")
            if domain:
                domain_name=domain[0]
                # print (domain_name)
                details['domain_name']=domain_name
                try:
                    hdr={
                        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                        'Accept-Encoding': 'none',
                        'Accept-Language': 'en-US,en;q=0.8',
                        'Connection': 'keep-alive'}
                    page=urllib2.Request(url, headers=hdr)
                    page=urllib2.urlopen(page)
                    page=page.read()
                    if (r'<title>') and (r'</title>') in page:
                        page=page.split("<title>")
                        page=page[1].split("</title>")
                        if (page):
                            details['title']=page[0].strip()
                            print(details['title'])
                except  Exception, e:
                    pass
                    print("Error" + e.message)
                    # else:

                    # print("Not contains the http | https")
        # print(details)
        return details
