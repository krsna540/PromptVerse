class SentimentAnalysisPrompt:
    """SentimentAnalysisPrompt - Provide the sentiment (positive, negative or neutral) of a set of documents
    """
    @staticmethod
    def generate_prompt(input_params: dict) -> str:
        """generate_prompt - generating the prompt that will be executed by LLM model and can be customized as per user need.

            Args:
                input_params (dict): dictinary of all required input parameters. Below are input_parameters :
                + query - user query for which response is expected

            Returns:
                str: generated prompt that will be excuted by LLM model mentioned.
        """
        template = """Please give a sentiment for this context. 
                    Answer with positive, negative or neutral. 
                    Context: {query}; 
                    Answer:
                    """
        template = template.format(**input_params)
        
        return template