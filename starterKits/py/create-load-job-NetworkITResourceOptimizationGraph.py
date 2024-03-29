#!/usr/bin/env python
# coding: utf-8

# # 1 - TigerGraph Schema Refresh Job
# 
# This script is used to automatically refresh the Stanza TigerGraph instance on TGCloud
# The steps included are:
#     
#     1. Create empty graph - drop if exists
#     2. Create schema change job
#     3. Create load jobs
#     4. Run load jobs
# 


# FETCH PACKAGES
import subprocess
import sys

import pyTigerGraph as tg

# ### 1.3.2 - Setup Connection to TGCloud
# 
# Access to TGCloud is thru REST API, and a combo of token & username/pw authentication

#User definied parameters
host = "http://localhost"
username = "tigergraph_user"
password = "tigergraph_pw" 

conn = tg.TigerGraphConnection(host=host, username=username, password=password)

# Create load jobs

print(conn.gsql('''
   
GRANT DATA_SOURCE tg_s3_data_source TO GRAPH NetworkITResourceOptimizationGraph

USE GRAPH NetworkITResourceOptimizationGraph

BEGIN
CREATE LOADING JOB NetworkITResourceOptimizationGraph_load_job FOR GRAPH NetworkITResourceOptimizationGraph {

LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/LUN.tsv\'}" TO VERTEX LUN VALUES ($"primary_id", $"name", $"total_capacity", $"estimated_used") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/Pool.tsv\'}" TO VERTEX Pool VALUES ($"primary_id", $"name", $"raw_capacity", $"used_capacity", $"user_capacity", $"subscribed_capacity") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/Storage_Array.tsv\'}" TO VERTEX Storage_Array VALUES ($"primary_id", $"name", $"capacity", $"allocated", $"available", $"raw_capacity", $"raw_allocated", $"raw_available") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/Host_Server.tsv\'}" TO VERTEX Host_Server VALUES ($"primary_id", $"hid", $"name", $"status") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/Application.tsv\'}" TO VERTEX Application VALUES ($"primary_id", $"short_name", $"tier", $"weight") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/Service.tsv\'}" TO VERTEX Service VALUES ($"primary_id", $"name") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/Manager.tsv\'}" TO VERTEX Manager VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/Switch.tsv\'}" TO VERTEX Switch VALUES ($"primary_id", $"swtich_name") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/Warning.tsv\'}" TO VERTEX Warning VALUES ($"primary_id", $"event_type", $"warn_date") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/WanringType.tsv\'}" TO VERTEX WanringType VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/Alert_App.tsv\'}" TO EDGE Alert_App VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/AHA_Alert.tsv\'}" TO EDGE AHA_Alert VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/Pool_Lun.tsv\'}" TO EDGE Pool_Lun VALUES ($"from", $"to", $"goUpper") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/Array_Pool.tsv\'}" TO EDGE Array_Pool VALUES ($"from", $"to", $"goUpper") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/LUN_Server.tsv\'}" TO EDGE LUN_Server VALUES ($"from", $"to", $"goUpper") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/Server_App.tsv\'}" TO EDGE Server_App VALUES ($"from", $"to", $"goUpper") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/App_Service.tsv\'}" TO EDGE App_Service VALUES ($"from", $"to", $"goUpper") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/Service_Manager.tsv\'}" TO EDGE Service_Manager VALUES ($"from", $"to", $"goUpper") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/Pool_Array.tsv\'}" TO EDGE Pool_Array VALUES ($"from", $"to", $"goLower") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/LUN_Pool.tsv\'}" TO EDGE LUN_Pool VALUES ($"from", $"to", $"goLower") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/Server_LUN.tsv\'}" TO EDGE Server_LUN VALUES ($"from", $"to", $"goLower") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/App_Server.tsv\'}" TO EDGE App_Server VALUES ($"from", $"to", $"goLower") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/Service_App.tsv\'}" TO EDGE Service_App VALUES ($"from", $"to", $"goLower") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/Manager_Service.tsv\'}" TO EDGE Manager_Service VALUES ($"from", $"to", $"goLower") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/Switch_Host.tsv\'}" TO EDGE Switch_Host VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/Array_Switch.tsv\'}" TO EDGE Array_Switch VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/NetworkITResourceOptimization/AppCall.tsv\'}" TO EDGE AppCall VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
}
''', options=[]))
