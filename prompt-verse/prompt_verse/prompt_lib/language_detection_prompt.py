class LanguageDetectionPrompt:
    """LanguageDetectionPrompt - In natural language processing models, Language detection prompting means detcting language based on inputs provided and responding with language name
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
        template = """Detect the language in the following context and answer with the name of the language. 
                    Context: {query}; 
                    Answer:
                   """
        template = template.format(**input_params)
        
        return template