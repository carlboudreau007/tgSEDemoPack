#!/usr/bin/env python

# # 1 - TigerGraph Schema Refresh Job
# 
# These scripts are used to automatically refresh the a TigerGraph instance on TGCloud (or EC2)

# FETCH PACKAGES
import sys
import pyTigerGraph as tg

# ### 1.3.2 - Setup Connection to TGCloud
# Access to TGCloud is thru REST API, and a combo of token & username/pw authentication

#User definied parameters
host = "http://localhost"
username = "tigergraph_user"
password = "tigergraph_pw"  

## create connection
conn = tg.TigerGraphConnection(host=host, username=username, password=password)

# ### 1.4.1 - Create Schema

# DEFINE / CREATE ALL EDGES AND VERTICES 
conn.gsql(''' 
USE GLOBAL
DROP GRAPH SocialNetGraph

CREATE GRAPH SocialNetGraph()
USE GRAPH SocialNetGraph

CREATE SCHEMA_CHANGE JOB SocialNetGraph_change_job FOR GRAPH SocialNetGraph {

ADD VERTEX BusRide(PRIMARY_ID event_id STRING, eventDate UINT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX TrainRide(PRIMARY_ID event_id STRING, eventDate UINT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Flight(PRIMARY_ID event_id STRING, eventDate UINT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX FundsTransfer(PRIMARY_ID bank_transfer_id STRING, amount FLOAT, transferEvent STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX PhoneCall(PRIMARY_ID phone_call_id STRING, eventDate UINT, callLength UINT, callType STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Person(PRIMARY_ID id_card_no STRING, fullName STRING, dob STRING, email STRING, gender STRING, ethic_group STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX HotelStay(PRIMARY_ID eventId STRING, eventDate UINT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Phone(PRIMARY_ID phoneNumber STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true";
ADD VERTEX BankAccount(PRIMARY_ID accountId STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX CaseReport(PRIMARY_ID caseId STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Address(PRIMARY_ID addr_id STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD UNDIRECTED EDGE hasCaseReport(FROM Person, TO CaseReport);
ADD UNDIRECTED EDGE hasFundsTransfer(FROM BankAccount, TO FundsTransfer);
ADD UNDIRECTED EDGE hasHotelStay(FROM Person, TO HotelStay);
ADD UNDIRECTED EDGE hasBusRide(FROM Person, TO BusRide);
ADD UNDIRECTED EDGE hasFlight(FROM Person, TO Flight);
ADD UNDIRECTED EDGE hasPhone(FROM Person, TO Phone);
ADD UNDIRECTED EDGE hasTrainRide(FROM Person, TO TrainRide);
ADD UNDIRECTED EDGE hasBankAccount(FROM Person, TO BankAccount);
ADD UNDIRECTED EDGE hasHomeAddress(FROM Person, TO Address);
ADD UNDIRECTED EDGE hasPhoneCall(FROM Phone, TO PhoneCall);
}

RUN SCHEMA_CHANGE JOB SocialNetGraph_change_job
DROP JOB SocialNetGraph_change_job
''', options=[])
