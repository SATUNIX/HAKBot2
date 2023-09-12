# AI_PWN / HAKBot2
Better, thanks to the new support for GGLMv3 and GGUF models. Alot of work to be done. Inspiration from pentestgpt. Goal of this project is to automate the user and execution side of PentestGPT. 
---


## Data flow overview 

1. Reasoning: Local LLM / Preferably an OpenAI API or HF - API 

2. Planning: Pentest GPT 

3. Parsing: Local LLM / GPT4ALL Prompt Generation using PentestGPT output

4. Code Execution: Python os execute / subproccessing 

## Explanations 

1. Think about the steps required and the neccesary tools to complete the job. 
2. Keep track of pentest progress 
3. Take the data from previous steps (1,2) and provide a single command to execute. 
4. Execute the command in python and return the tools print out. 

Recources: 
https://huggingface.co/TheBloke/Spicyboros-13B-2.2-GGUF/blob/main/spicyboros-13b-2.2.Q5_K_M.gguf
https://huggingface.co/TheBloke/Llama-2-7b-Chat-GPTQ
https://github.com/ggerganov/llama.cpp
