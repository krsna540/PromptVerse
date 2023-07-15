class ChatSummaryPrompt:
    """ChatSummaryPrompt -  Conversational summary to condense the chat history
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
        template = """Condense the following chat transcript by shortening and summarizing the content 
                    without losing important information:
                    {query}
                    Condensed Transcript:
                    """
        template = template.replace("{query}", input_params["query"])
        return template