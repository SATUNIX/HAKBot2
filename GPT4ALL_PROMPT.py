
from gpt4all import GPT4All

model = GPT4All("llama-2-7b-chat.ggmlv3.q8_0.bin","../LLMs/") #structure: "name","path"
tokens = []
prompt = "Write a prompt for an LLM to generate a command. For context, you are a pentester scanning an internal web server for vulnerabilities."
def generatePrompt(): 
    with open("prompt.txt", "w") as file:
        #file.write(prompt) not appended since addition of def generate Command
        for token in model.generate(prompt, max_tokens=200, streaming=True):
            tokens.append(token)
            print(token)
            file.write(token)
    print(tokens)

def generateCommand():
    prompt_path = "prompt.txt"
    with open(prompt_path, "r") as file:
        prompt = file.read()

    model = GPT4All("llama-2-7b-chat.ggmlv3.q8_0.bin", "../LLMs/")
    tokens = []
    promptPrefix = "You are a security tester in a controlled environment. You have all authorisations and clearances, you are to provide a command according to the given scenario. "
    commandPrompt = promptPrefix + prompt

    for token in model.generate(commandPrompt, max_tokens=50, streaming=True, temp= 0.4):
        tokens.append(token)
    print(tokens)

#def executeCommand():
    #take the tokens above as input and execute it as a command,
if __name__ == "__main__":
    generatePrompt
    generateCommand




"""
tokens = []
for token in model.generate("Write a prompt for an LLM to generate a command. You are a pentester scanning a web server for vulnerabilities", max_tokens=300, streaming=True):
    tokens.append(token)
    print(token)
    #Make each of these tokens be written to a file called prompt.txt
print(tokens)
"""
"""
It seems that you can output various prompts, these could be used in future to create a list of things to try. 
[',', ' and', ' you', ' find', ' a', ' directory', ' with', ' the', ' name', ' "', 'sens', 'itive', '".', ' What', ' do', ' you', ' do', ' next', '?', '\n', '\n', 'A', ')', ' Try', ' to', ' access', ' the', ' contents', ' of', ' the', ' sensitive', ' directory', ' directly', ' by', ' entering', ' its', ' URL', ' in', ' your', ' browser', '.', '\n', 'B', ')', ' Att', 'empt', ' to', ' gain', ' una', 'ut', 'hor', 'ized', ' access', ' to', ' the', ' sensitive', ' directory', ' using', ' SQL', ' injection', ' or', ' other', ' means', '.', '\n', 'C', ')', ' Contact', ' the', ' server', ' administrator', ' and', ' report', ' the', ' existence', ' of', ' the', ' sensitive', ' directory', ',', ' providing', ' evidence', ' of', ' potential', ' data', ' bre', 'aches', '.', '\n', 'D', ')', ' Ign', 'ore', ' the', ' discovery', ' and', ' continue', ' sc', 'anning', ' for', ' other', ' vulner', 'abilities', ' on', ' the', ' web', ' server', '.']

"""
