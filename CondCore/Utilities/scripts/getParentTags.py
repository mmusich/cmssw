#!/usr/bin/env python
from __future__ import print_function
#
# Author:   Marco MUSICH
#
# Usage:
# getParentTags.py -H <user defined payload hash>
#

"""
Example script to extract tags contiaining a given an hash
"""

__author__ = 'Marco Musich'
__copyright__ = 'Copyright 2021, CERN CMS'
__credits__ = ['Giacomo Govi', 'Salvatore Di Guida']
__license__ = 'Unknown'
__maintainer__ = 'Marco Musich'
__email__ = 'marco.musich@cern.ch'
__version__ = 1

import os
import sys
import optparse
import hashlib
import tarfile
import netrc
import getpass
import errno
import sqlite3
import json
import tempfile
import pprint
import subprocess
import CondCore.Utilities.conddblib as conddb
from prettytable import PrettyTable    

#####################################################################
def getCMSSWRelease( ):
#####################################################################
    CMSSW_VERSION='CMSSW_VERSION'
    if not os.environ.has_key(CMSSW_VERSION):
        print("\n CMSSW not properly set. Exiting")
        sys.exit(1)
    release = os.getenv(CMSSW_VERSION)
    return release

#####################################################################
def get_parent_tags(db, theHash):
#####################################################################

    db = db.replace("sqlite_file:", "").replace("sqlite:", "")
    db = db.replace("frontier://FrontierProd/CMS_CONDITIONS", "pro")
    db = db.replace("frontier://FrontierPrep/CMS_CONDITIONS", "dev")

    con = conddb.connect(url = conddb.make_url(db))
    session = con.session()
    IOV = session.get_dbtype(conddb.IOV)
    Tag = session.get_dbtype(conddb.Tag)

    query_result = session.query(IOV.tag_name).filter(IOV.payload_hash == theHash).all()
    tag_names = map(lambda entry : entry[0], query_result)
    
    listOfOccur=[]

    for tag in tag_names:
        synchro = session.query(Tag.synchronization).filter(Tag.name == tag).all()
        iovs = session.query(IOV.since).filter(IOV.tag_name == tag).filter(IOV.payload_hash == theHash).all()
        times = session.query(IOV.insertion_time).filter(IOV.tag_name == tag).filter(IOV.payload_hash == theHash).all()

        synchronization = [item[0] for item in synchro]
        listOfIOVs  = [item[0] for item in iovs]
        listOfTimes = [str(item[0]) for item in times]
        
        for iEntry in range(0,len(listOfIOVs)):                                
            listOfOccur.append({"tag": tag,
                                "synchronization" : synchronization[0],
                                "since" : listOfIOVs[iEntry] ,
                                "insertion_time" : listOfTimes[iEntry] })

    return listOfOccur


#####################################################################
if __name__ == '__main__':
    parser = optparse.OptionParser(usage =
                                   'Usage: %prog [options] <file> [<file> ...]\n'
                                   )

    parser.add_option('-H', '--hash',
                      dest = 'hash',
                      default = "b0e2bc7e4947817d99324ff20f8c3238d06c46fb",
                      help = 'payload hash to check',
                      )

    parser.add_option('-D', '--db',
                      dest = 'connectionString',
                      default = "frontier://FrontierProd/CMS_CONDITIONS",
                      help = 'Database type to inspect',
                      )

    (options, arguments) = parser.parse_args()
    
    theRelease = getCMSSWRelease()
    print("- Getting conddblib from release",theRelease)
    print("- Searching in",options.connectionString)

    tags = get_parent_tags(options.connectionString,options.hash) 

    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(tags)
    #print tags
    #for tag in tags:
    #    print(tag)
    #print(head)

    t = PrettyTable(['hash', 'since','tag','synch','insertion time'])
    for element in tags:
        t.add_row([options.hash,element['since'],element['tag'],element['synchronization'],element['insertion_time']])

    print(t)

#eof
