class FewShotPrompt:
    """FewShotPrompt - prompting can be used as a technique to enable in-context learning where we provide demonstrations in the prompt to steer the model to better performance.
    """
    @staticmethod
    def generate_prompt(input_params: dict) -> str:
        """generate_prompt - generating the prompt that will be executed by LLM model and can be customized as per user need.

            Args:
                input_params (dict): dictinary of all required input parameters. Below are input_parameters :
                + persona - a natural language portrayal of a specific individual 
                + audience - to whom we are providing response
                + max_length - maximum umber of words allowed in response
                + query - user query for which response is expected
                + context -  Format for context - Question, Thought, Tool, Tool Input, Observation.

            Returns:
                str: generated prompt that will be excuted by LLM model mentioned.
        """
        template = """You are a {persona} and your audience are {audience}.
                    Create a concise and informative answer (no more than {max_length} words) for a given question. Let's think step by step.
                    To answer questions, you'll need to go through multiple steps involving step-by-step thinking and selecting appropriate inputs; tools will respond with observations. When you are ready for a final answer, respond with the `Final Answer:`
                    Examples:
                    ##
                    {context}
                    ##
                    Question: {query}; 
                    """
        template = template.format(**input_params)
        
        return template