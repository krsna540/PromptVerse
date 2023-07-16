import os
import json
import gc
import uuid
import datetime
import tempfile
import errno
import pandas as pd


class PromptMaintenance:
    """PromptMaintenance- to store complete information about a prompt and encapsulation of prompt collections
    """

    def __init__(self):
        # self.pmodel = pmodel
        pass

    def templates_library(self) -> str:
        """base_template_library - To display all kinds of prompting templates available and descriptions associated wiht them
        Returns:
            str: Prompt templates and descriptions
        """
        templates = pd.read_csv("prompt_lib/prompt_lib_descriptions.csv")
        print(templates)
        return templates

    def generate(self, template_name: str, input_params: dict) -> str:
        """generate : To generate user selected prompt with provided inputs

        Args:
            template_name (str): Name of the template that user wants to generate
            input_params (dict): all the input parameters required for generating prompt
        Returns:
            str: Prompt selected by the user with inputs loaded in prompt
        """
        response = eval(template_name)().generate_prompt(input_params)
        return response

    def get_version_number(self, pmodel):
        old_version = 0
        for ele in pmodel.collection:
            if old_version < ele.version:
                old_version = ele.version
        return old_version+1