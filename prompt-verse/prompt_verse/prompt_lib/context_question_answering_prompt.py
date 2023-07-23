class ContextQuestionAnsweringPrompt:
    """ContextQuestionAnsweringPrompt -  Prompt to check whether a query can be answered with the provided context or not, reply will be "yes" or "no"
    """
    @staticmethod
    def generate_prompt(input_params: dict) -> str:
        """generate_prompt - generating the prompt that will be executed by LLM model and can be customized as per user need.

            Args:
                input_params (dict): dictinary of all required input parameters. Below are input_parameters :
                + query - user query for which response is expected
                + context -  Prior information to be considered for prompt

            Returns:
                str: generated prompt that will be excuted by LLM model mentioned.
        """
        template = """Does the following context contain the answer to the question?
                    Context: {context}; 
                    Question: {query}; 
                    Please answer yes or no! Answer:
                    """
        template = template.replace("{context}", input_params["context"])
        template = template.replace("{query}", input_params["query"])
        return template