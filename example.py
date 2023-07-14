import os
from smart_prompt import SmartPrompt


if __name__ == "__main__":
    os.environ["OPENAI_API_KEY"] = "" # provide your openai key here
    sp=SmartPrompt()
    template_df=sp.display_prompt_templates()
    
    sp.create_session(name="BlueAngel",description="New Session for BlueAngel Use case",offline_storage_location="storage/")
    prompt_id_1=sp.create_new_prompt(name="GreetUser",description="greeting user at begining of conversation")

    input_parameters={}
    input_parameters["persona"]="Nurse ChatBot"
    input_parameters["audience"]="Patient"
    input_parameters["query"]="Greet the person"
    input_parameters["max_length"]="10"

    generated_prompt=sp.generate_prompt_query(prompt_template="ZeroShotPrompt",prompt_input_parameters=input_parameters)

    llm_response=sp.execute_prompt()

    
    input_parameters={}
    input_parameters["persona"]="Nurse ChatBot"
    input_parameters["audience"]="Patient"
    input_parameters["query"]="Greet John"
    input_parameters["max_length"]="10"

    updated_prompt_id1=sp.update_exisitng_prompt()
    generated_prompt=sp.generate_prompt_query(prompt_template="ZeroShotPrompt",prompt_input_parameters=input_parameters)
    sp.update_input_prompt_query("Greet John Ryan")
    llm_response=sp.execute_prompt()
    
    #------------------------------------------------------------------------------------------------------------------
    
    prompt_id_2=sp.create_new_prompt(name="User Needs",description="asking user is doing today")

    input_parameters={}
    input_parameters["persona"]="Nurse ChatBot"
    input_parameters["audience"]="Patient"
    input_parameters["query"]="ask user how he is doing today and what can we do to help him"
    input_parameters["max_length"]="20"

    generated_prompt=sp.generate_prompt_query(prompt_template="ZeroShotPrompt",prompt_input_parameters=input_parameters)

    llm_response=sp.execute_prompt()

    print(sp.save_prompt())
    sp.view_report()
     