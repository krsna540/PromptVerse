class ZeroShotPrompt:
    """ZeroShotPrompt - In natural language processing models, 
    zero-shot prompting means providing a prompt that is not part of the training data to the model, 
    but the model can generate a result that you desire.
    """
    @staticmethod
    def generate_prompt(input_params: dict) -> str:
        """generate_prompt - generating the prompt that will be executed by LLM model and can be customized as per user need.

        Args:
            input_params (dict): dictinary of all required input parameters. Below are input_parameters :
             + persona - a natural language portrayal of a specific individual 
             + audience - to whom we are providing response
             + query - user query for which response is expected
             + max_length - maximum number of words

        Returns:
            str: generated prompt that will be excuted by LLM model mentioned.
        """

        template = """You are a {persona} and your audience are {audience}.
                     Create a concise and informative answer (no more than {max_length} words) for a given question 
                      {query} 
                   """
        template = template.replace("{persona}", input_params["persona"])
        template = template.replace("{audience}", input_params["audience"])
        template = template.replace("{max_length}", input_params["max_length"])
        template = template.replace("{query}", input_params["query"])
        return template