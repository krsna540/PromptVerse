import json
import pandas as pd


def generate_session_json(filename:str):
    with open(filename, 'r') as f:
        data = json.load(f)
    
    session_data={}
    session_data['session_id']=data['session_id']
    session_data['session_name']=data['name']
    session_data['created_timestamp']=data['created_timestamp']
    session_data['filename']=data['filename']

    ds=[]
    for prompt in data['registry']:
        prompt_dict={}
        prompt_dict['prompt_id']=prompt['prompt_id']
        prompt_dict['name']=prompt['name']
        prompt_dict['description']=prompt['description']
        prompt_dict['created_timestamp']=prompt['created_timestamp']
        for collection in prompt['collection']:
            data_dict={}
            data_dict.update(prompt_dict)
            data_dict['prompt_text']=collection['prompt_text']
            data_dict['created_timestamp']=collection['created_timestamp']
            data_dict['prompt_template']=collection['prompt_template']
            data_dict['version']=collection['version']
            data_dict['executable']=collection['executable']
            data_dict['output']=collection['output']
            data_dict['response_time']=collection['response_time']
            data_dict['profanity']=collection['metrics']['profanity']
            data_dict['prompt_tokens']=collection['metrics']['prompt_tokens']
            ds.append(data_dict)

    df = pd.DataFrame(ds)
    return session_data,df