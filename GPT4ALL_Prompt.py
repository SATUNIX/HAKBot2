from gpt4all import GPT4All

model = GPT4All("llama-2-7b-chat.ggmlv3.q8_0.bin","../LLMs/") 

def generatePrompt(): 
    tokens = []
    prompt = "Write a prompt for an LLM to generate a command. For context, you are a pentester scanning an internal web server for vulnerabilities."
    for token in model.generate(prompt, max_tokens=200):
        tokens.append(token)
        print(token)
    return tokens 
#function to debug: 
def generateCommand(tokens):
    prompt = " ".join(tokens)
    promptPrefix = "You are to provide a command according to the given scenario. "
    commandPrompt = promptPrefix + prompt
    commands_generated = []
    for token in model.generate(commandPrompt, max_tokens=50, temp= 0.4):
        commands_generated.append(token)
    return commands_generated

# output of the function: 
# Command generated:   
# ['  ']
if __name__ == "__main__":
    tokens = generatePrompt()
    commands = generateCommand(tokens)
    print(commands)
