# Package: PromptVerse

## Description
The PromptVerse package is designed to enhance the capabilities of developers in writing prompts, logging them, and providing a prompt registry. It offers a comprehensive list of prompt templates, allowing developers to provide input parameters and queries to generate prompts effortlessly. The package also includes offline storage in JSON format and provides features for logging, organizing, evaluating, and experimenting with prompts. With the ability to iterate through multiple prompt iterations, developers can compare experiments and metrics. Additionally, the package emphasizes minimal code requirements and provides a built-in UI display for all prompts created during a session.

## Features

### Prompt Registry
The PromptVerse package includes a prompt registry feature that acts as a centralized repository for storing and managing prompts. Developers can register prompts, assign relevant metadata, and easily access prompts from a single location. The prompt registry facilitates prompt discovery, version control, and promotes reusability among developers.

### Complete List of Prompt Templates
The package provides a comprehensive list of prompt templates that cover a wide range of use cases. Developers only need to provide input parameters and queries to generate prompts using these templates. This feature streamlines the prompt writing process, saving developers time and effort.

### Offline Storage in JSON Format
PromptVerse offers offline storage capabilities using JSON format. Developers can store prompts and related data locally, enabling easy retrieval and manipulation without an internet connection. The JSON format ensures a structured representation of prompt information.

### Logging
The package includes a logging feature that enables developers to log prompts and associated actions. Logging helps track the execution flow, identify errors, and monitor the performance of prompts. The logged information can be used for debugging and analysis purposes.

### Organize and Evaluate Prompts
Developers can efficiently organize and evaluate prompts using the PromptVerse package. It provides functionalities to categorize prompts based on different criteria such as tags, topics, or complexity levels. This organization helps in better management and retrieval of prompts. Additionally, developers can evaluate prompt effectiveness and performance by conducting experiments and comparing the results.

### Iterative Prompt Development and Comparison
The PromptVerse package allows developers to iterate through multiple prompt iterations. Developers can experiment with different prompt formulations, configurations, or parameters. They can compare the results of these experiments, along with associated metrics, to determine the most effective prompt for a given scenario.

### Minimal Code
The PromptVerse package emphasizes minimal code requirements. It provides a set of pre-defined functions and utilities that abstract complex operations, reducing the amount of code developers need to write. This allows developers to focus on the prompt logic and functionality rather than dealing with implementation details.

### UI Display of Prompt Session
The package includes a built-in UI display that shows all the prompts created during a session. This feature provides a convenient way for developers to review and interact with prompts, ensuring a seamless prompt development experience.

## Getting Started

### Installation
To install the PromptVerse package, follow these steps:



### Usage

```
import os
from src.prompt_verse import PromptVerse


if __name__ == "__main__":
    os.environ["OPENAI_API_KEY"] = "" # provide your openai key here
    sp=PromptVerse()
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
     


```


## Support and Feedback
If you have any questions, issues, or feedback regarding the PromptVerse package, please reach out to our support team at [support email or forum link]. We value your input and strive to provide timely assistance.