import gradio as gr
import pandas as pd
import joblib
from generate_report import generate_session_json

inputs =gr.Dataframe(generate_session_json("storage/040dbfef52614992a6b64f21cf248763.json"))
def Prompt_registry(prompts):
    pass  
gr.Interface(fn =Prompt_registry, inputs = inputs, outputs = None).launch()