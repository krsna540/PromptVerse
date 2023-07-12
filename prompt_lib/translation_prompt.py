class TranslationPrompt:
    """TranslationPrompt -  Prompt to accept a target_language and translate each text provided to this target language.
    """
    @staticmethod
    def generate_prompt(input_params: dict) -> str:
        """generate_prompt - generating the prompt that will be executed by LLM model and can be customized as per user need.

            Args:
                input_params (dict): dictinary of all required input parameters. Below are input_parameters :
                + query - user query for which response is expected
                + target_language -  Target language for translation

            Returns:
                str: generated prompt that will be excuted by LLM model mentioned.
        """
        template = """Translate the following context to {target_language}. Context: {query}; 
                    Translation:
                    """
        template = template.replace(
            "{target_language}", input_params["target_language"])
        template = template.replace("{query}", input_params["query"])
        return template