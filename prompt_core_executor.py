import json
import os
import random
from time import time
from unicodedata import category
from langchain.chat_models import ChatOpenAI
from langchain import OpenAI, LLMChain
from langchain.prompts import PromptTemplate

from session import Session, PromptModel, PromptCollection
from prompt_lib .few_shot_prompt import FewShotPrompt
from prompt_lib.chat_summary_prompt import ChatSummaryPrompt
from prompt_lib.context_question_answering_prompt import ContextQuestionAnsweringPrompt
from prompt_lib.language_detection_prompt import LanguageDetectionPrompt
from prompt_lib.sentiment_analysis_prompt import SentimentAnalysisPrompt
from prompt_lib.summarization_prompt import SummarizationPrompt
from prompt_lib.topic_classification_prompt import TopicClassificationPrompt
from prompt_lib.translation_prompt import TranslationPrompt
from prompt_lib.zero_shot_prompt import ZeroShotPrompt
from validations import check_profanity, topic_check, num_tokens_from_string


class PromptCoreExecutor:
    def __init__(self, template_name, input_params: dict, model_name: str = "gpt-3.5-turbo"):

        self.template_name = template_name
        self.input_params = input_params
        self.model_name: str = model_name

        self.llm_response: str = None
        self.response_time: float = 0
        self.executable: bool = False
        self.metrics = {}
        self.prompt_query = None

    def generate_prompt_query(self) -> str:
        """generate : To generate user selected prompt with provided inputs

        Args:
            template_name (str): Name of the template that user wants to generate
            input_params (dict): all the input parameters required for generating prompt
        Returns:
            str: Prompt selected by the user with inputs loaded in prompt
        """
        prompt_query = eval(self.template_name)(
        ).generate_prompt(self.input_params)
        self.prompt_query = prompt_query
        return prompt_query

    def execute(self, input_prompt: str) -> str:
        """execute - executing the prompt with Open AI GPT models

        Args:
            input_prompt (str): prompt template that has to be executed by LLM
            model_name (str, optional): name of LLM model(currently supporting openai models only) to execute prompt. Defaults to "gpt-3.5-turbo".

        Returns:
            str: response from LLM model for the prompt provided.
        """
        start_time = time()
        prompt = PromptTemplate(template=input_prompt, input_variables=[])
        llm = ChatOpenAI(model_name=self.model_name, temperature=0,
                         openai_api_key=os.environ['OPENAI_API_KEY'])
        chatgpt_chain = LLMChain(llm=llm, prompt=prompt, verbose=False)
        self.llm_response = chatgpt_chain.predict()
        end_time = time()
        self.response_time = end_time - start_time

    def calculate_metrics(self):
        self.metrics['profanity'] = check_profanity(self.llm_response)
        if self.template_name == "TopicClassificationPrompt":
            self.metrics['predicted_available_topic'] = topic_check(
                self.input_params['options'], self.llm_response)
        self.metrics['prompt_tokens'] = num_tokens_from_string(
            self.prompt_query, "cl100k_base")