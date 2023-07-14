import os
import json
import pandas as pd
from time import time
from prompt_core_executor import PromptCoreExecutor
from session import Session, PromptModel, PromptCollection
from session_maintenance import SessionMaintenance
from prompt_maintenance import PromptMaintenance
from prompt_core_executor import PromptCoreExecutor
from gradio_ui import display_output

class SmartPrompt:
    def __init__(self):
        self.promptmodel=None
        self.promptmaintenance=None
        self.session_descriptor=None
        self.input_prompt=None
        self.executor=None
        self.prompt_input_parameters=None
        self.prompt_template=None
        self.session_metadata=None
        
    def create_session(self,name,description,offline_storage_location):
        """create_session : Creating a session with name, description and location for storing the metadata

        Args:
            name (_type_): Name of the session
            description (_type_): Description of the session
            offline_storage_location (_type_): a folder location for storing the metadata related to session
        """        
        self.session_descriptor = Session(name,description,offline_storage_location)
        self.session_metadata=SessionMaintenance(self.session_descriptor)
        self.session_metadata.create()
        
    
    def create_new_prompt(self,name:str,description:str):
        """create_new_prompt : Create a completly new prompt which is not udpated version to existing one.

        Args:
            name (_type_): Name of the prompt
            description (_type_): description of the prompt
        """
        self.promptmodel=None
        self.promptmaintenance=None
        self.input_prompt=None
        self.executor=None
        self.prompt_input_parameters=None
        self.prompt_template=None
        self.promptmodel = PromptModel(name,description)
        return self.promptmodel.prompt_id
    
    def update_exisitng_prompt(self):
        """create_new_prompt : Create a completly new prompt which is not udpated version to existing one.

        Args:
            name (_type_): Name of the prompt
            description (_type_): description of the prompt
        """
        self.input_prompt=None
        self.prompt_input_parameters=None
        self.prompt_template=None
        return self.promptmodel.prompt_id
    
    def generate_prompt_query(self,prompt_template:str,prompt_input_parameters:dict,openai_model="gpt-3.5-turbo")->str:
        """generate_prompt_query : generating a prompt from template user selected and with user provided inputs

        Args:
            prompt_template (str): select any default prompt template from the library.
            prompt_input_parameters (dict): dictionary of all the input parameters
            openai_model (str, optional): OpenAI model on which prompt has to be executed. Defaults to "gpt-3.5-turbo".
        Returns:
            str: Preview of prompttext to be executed
        """
        self.prompt_input_parameters=prompt_input_parameters
        self.prompt_template=prompt_template
        self.executor = PromptCoreExecutor(prompt_template, input_params=prompt_input_parameters, model_name=openai_model)
        self.input_prompt = self.executor.generate_prompt_query()

        return self.input_prompt
    
    def update_input_prompt_query(self,new_prompt_text:str)->None:
        """update_input_prompt : to update the prompt generated by template as required by user.

        Args:
            new_prompt_text (str): new prompt modifed as per user requirement.
        """        
        self.input_prompt = new_prompt_text
        
    def save_prompt(self):
        """save_prompt : save the prompt, respone and metrics.
        """
        self.session_descriptor.registry=[i for n, i in enumerate(self.session_descriptor.registry) if i not in self.session_descriptor.registry[n + 1:]]
        self.session_metadata.Save()
        return "session saved successfully"
    
    def execute_prompt(self):
        """execute_prompt : execute the prompt on OpenAI LLM model and generate response and metrics
        Returns:
            str: response generated by OpenAI prompt.
        """     
        prompt_metadata = PromptMaintenance()   
        self.executor.execute(self.input_prompt)
        self.executor.prompt_query=self.input_prompt
        self.executor.calculate_metrics()
        newprompt = PromptCollection(self.input_prompt, version=0)
        newprompt.prompt_template = self.prompt_template
        newprompt.output = self.executor.llm_response
        newprompt.metrics = self.executor.metrics
        newprompt.executable = self.executor.executable
        newprompt.response_time = self.executor.response_time
        
        newprompt.version = prompt_metadata.get_version_number(self.promptmodel)
        self.promptmodel.collection.append(newprompt)

        self.session_descriptor.registry.append(self.promptmodel)
        
        return self.executor.llm_response

    def view_report(self):
        """view_report : view report of all the prompts created in the session along with output and other metrics
        """
        display_output(self.session_descriptor.offline_folder_path+self.session_descriptor.session_id+".json")
    
    def display_prompt_templates(self):
        """display_prompt_templates : display all prompt templates available as part of library
        """        
        templates = pd.read_csv("./prompt_lib/prompt_lib_description.csv")
        print(templates)
        return templates
        