
import dateutil.parser as dp
import datetime
import json
import os
from environs import Env
from collections import OrderedDict

experiment_id = "5485db4e-b714-4b20-9531-6cfe79fe8ffe"
experiment_name = "fake-experiment"
aml_run_details = {
        "runId": "afbd49e5-0acd-4534-9368-a8bd4e163783",
        "startTimeUtc": "2020-08-04T15:50:36.186Z",
        "endTimeUtc": "2020-08-04T15:55:58.349Z",
        "status": "Completed",
        "properties": {
            "azureml.runsource": "azureml.PipelineRun"
        }
    }

exec_time_ms=0 #initializing to zero

env = Env()
env.read_env() #to allow reading from .env file

# converting ISO 8601 datetime format to epoch timestamp in milliseconds
def iso8601_to_epoch_ms(time_in_iso8601_format):
    t=time_in_iso8601_format
    parsed_t=dp.parse(t)
    t_in_seconds=parsed_t.timestamp()
    final_t=int(t_in_seconds*(1000))
    return final_t

# get the filename from filepath        
def get_dataset_name(filepath):
    file_name = os.path.basename(filepath)
    final_fname=os.path.splitext(file_name)[0]
    return final_fname

def map_to_app_insight_entry(aml_run_details,experiment_id,experiment_name,env):
    
    exp_dict=dict([('experimentId', experiment_id), ('experimentName', experiment_name)]) ##creating a new dictionary
    env_dict = env.dict("dict") ## retrieving dict from .env file
    
    ##calling iso8601_to_epoch_ms() function
    startTimeUtc=iso8601_to_epoch_ms(aml_run_details.get("startTimeUtc")) 
    assert startTimeUtc==1596556236186, "Called with unexpected value."
    
    endTimeUtc=iso8601_to_epoch_ms(aml_run_details.get("endTimeUtc"))
    assert endTimeUtc==1596556558349,"Called with unexpected value."
    
    if not AssertionError:
        exec_time_ms=(endTimeUtc-startTimeUtc) 
        runid=aml_run_details.get("runId")
        status1=aml_run_details.get("status")
        prop=aml_run_details.get("properties")
        new_prop=prop.get("azureml.runsource")
        
        aml_dict=dict(start_time_utc_ms=startTimeUtc,end_time_utc_ms=endTimeUtc,execution_time_ms=exec_time_ms,status=status1,run_type=new_prop,run_id=runid)
        
        ##Merging 3 dictionaries using **kwargs. When we apply ** to a dictionary, then it expands the contents as collection of key-value pairs
        res = {**env_dict,**exp_dict,**aml_dict}
        
        ##Convert python object to json object.
        new_res=json.dumps(res,indent=4)
        return new_res
    
    elif AssertionError:
        print("Called with unexpected value.")
        exit