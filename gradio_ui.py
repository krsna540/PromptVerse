import gradio as gr
import pandas as pd
import joblib
from generate_report import generate_session_json


def SmartPromptRegistry(Prompts):
    return "fn="  

def display_output(filepath:str):
    session_info,df=generate_session_json(filepath)
    inputs =gr.Dataframe(df)
    with gr.Blocks() as demo:
        gr.Interface(fn=SmartPromptRegistry, inputs = inputs, outputs = None,title="Smart Prompt",description="Smart Prompt is a registry capable of logging prompts, autoversioning, calculating metrics.\n Below interface is Readonly")
        demo.launch(height="700px",width="500px")