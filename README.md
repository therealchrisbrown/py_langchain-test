# Testing for Langchain versus GPT

One big problem working with GPT-4 (or the previous models) is that it lacks to get realtime data. With the possibilities to use GPT-Builder or OpenAI Functions you can solve that specific problem quite well but there is more to it: OpenAI is quite opaque in its parameters. In other words, you simply cannot peek into the engine room.

## One possible Solution: Use Langchain

With the use of langchain (in combination with CometML to monitor every step and get a good feeling of the thinking process the system is taking) you can solve this problem and get realtime data. 

The presented solution in the Notebook shows the simple way.

## Used packages
1. Langchain
2. OpenAI
3. SERPAPI (https://serpapi.com)
4. CometML for Logging

Credits to Santiago on X.
