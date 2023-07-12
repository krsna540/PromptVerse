import os
import json
from time import time
from prompt_core_executor import PromptCoreExecutor
from old_code.helper_objects import PromptModel
from session import Session, PromptModel, PromptCollection
from session_maintenance import SessionMaintenance
from prompt_maintenance import PromptMaintenance
from prompt_core_executor import PromptCoreExecutor


def execute_prompt_metrics(template_name, input_params, model_name):
    executor = PromptCoreExecutor(
        template_name, input_params=input_params, model_name=model_name)
    input_prompt = executor.generate_prompt_query()
    executor.dummy_execute(input_prompt)
    executor.calculate_metrics()

    newprompt = PromptCollection(input_prompt, version=0)
    newprompt.prompt_template = template_name
    newprompt.output = executor.llm_response
    newprompt.metrics = executor.metrics
    newprompt.executable = executor.executable
    newprompt.response_time = executor.response_time
    return newprompt


if __name__ == "__main__":
    os.environ["OPENAI_API_KEY"] = ""
    descriptor = Session("sample", "sample description", "storage/")
    # --------------------
    model = PromptModel(
        "UserGreet", "to greet user with hi/hello/good morning etc")
    prompt_metadata = PromptMaintenance()

    input_params = {}
    input_params['options'] = "['sports','weather','movies']"
    input_params['query'] = """it is raining outside"""

    prompt_obj = execute_prompt_metrics(
        "TopicClassificationPrompt", input_params=input_params, model_name="gpt-3.5-turbo")
    prompt_obj.version = prompt_metadata.get_version_number(model)
    model.collection.append(prompt_obj)
    # -----------------------------------------------------
    input_params = {}
    input_params['options'] = "['sports','weather','movies']"
    input_params['query'] = """film is bad"""

    prompt_obj = execute_prompt_metrics(
        "TopicClassificationPrompt", input_params=input_params, model_name="gpt-3.5-turbo")
    prompt_obj.version = prompt_metadata.get_version_number(model)
    model.collection.append(prompt_obj)
    # -----------------------------------------------------
    model2 = PromptModel(
        "ConversationCloser", "to close user conversation")
    input_params = {}
    input_params['query'] = """film is bad"""
    prompt_obj = execute_prompt_metrics(
        "SentimentAnalysisPrompt", input_params=input_params, model_name="gpt-3.5-turbo")
    prompt_obj.version = prompt_metadata.get_version_number(model2)
    model2.collection.append(prompt_obj)
    # -----------------------------------------------------
    descriptor.registry.append(model)
    descriptor.registry.append(model2)
    s_m = SessionMaintenance(descriptor)
    s_m.create()