class SummarizationPrompt:
    """SummarizationPrompt -  Prompt to produce a summary for each document provided in query.
    """
    @staticmethod
    def generate_prompt(input_params: dict) -> str:
        """generate_prompt - generating the prompt that will be executed by LLM model and can be customized as per user need.

            Args:
                input_params (dict): dictinary of all required input parameters. Below are input_parameters :
                + query - user query for which summarization is expected

            Returns:
                str: generated prompt that will be excuted by LLM model mentioned.
        """
        template = """Summarize this document: {query} 
                      Summary:
                    """
        template = template.replace("{query}", input_params["query"])
        return template