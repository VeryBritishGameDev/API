from chatgpt import talk_gpt

givenlanguage = input("Input Language ")
givendifficulty = input("Input Diffuculty ")
def pytalk(givenlanguage, givendifficulty):
    prompt = f"Generate a random programming challange, in this language: {givenlanguage} and this difficulty: {givendifficulty}"
    ##return talk_gpt(prompt)
    print(talk_gpt(prompt))
pytalk(givenlanguage, givendifficulty)
