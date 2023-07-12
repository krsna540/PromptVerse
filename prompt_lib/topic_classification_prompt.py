class TopicClassificationPrompt:
    """TopicClassificationPrompt - Classify the given query into categories
    """
    @staticmethod
    def generate_prompt(input_params: dict) -> str:
        """generate_prompt - generating the prompt that will be executed by LLM model and can be customized as per user need.

        Args:
            input_params (dict): dictinary of all required input parameters. Below are input_parameters :
             + query - user query for which response is expected
             + options - list of categories

        Returns:
            str: generated prompt that will be excuted by LLM model mentioned.
        """
        template = """Categories: {options}; 
                    What category best describes: {query}; 
                    Answer:
                   """
        template = template.replace("{query}", input_params["query"])
        template = template.replace("{options}", input_params["options"])
        return template