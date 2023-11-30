from dotenv import load_dotenv
load_dotenv()

import os
import comet_ml

from openai import OpenAI
client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')

comet_ml.init(api_key=os.environ["COMET_ML_API_KEY"],project_name="comet-example-langchain")

serpapi_key = os.environ['SERPAPI_KEY']

from langchain.agents import initialize_agent, load_tools
from langchain.callbacks import CometCallbackHandler, StdOutCallbackHandler
from langchain.callbacks.base import CallbackManager
from langchain.llms import OpenAI

comet_callback = CometCallbackHandler(
    project_name="langchain-example",
    complexity_metrics=True,
    stream_logs=True,
    tags=["agent"],
)
manager = CallbackManager([StdOutCallbackHandler(), comet_callback])

llm = OpenAI(temperature=0.9, callback_manager=manager, verbose=True)
tools = load_tools(["serpapi"], llm=llm, callback_manager=manager)

agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    callback_manager=manager,
    verbose=True,
)

agent.run(
    "What's the population of the country of the team that won the last soccer match between Real Madrid and Chelsea?"
)

comet_callback.flush_tracker(agent, finish=True)