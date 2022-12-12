import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write a python program for rock, paper, scissors \n\nimport random\n# print(\"Let's Play Rock, Paper, Scissors\")\n\nplayer1 = input(\"[Player 1] Please choose Rock, Paper, Scissors: \")\n#Create a list of 3 items\noptions = [\"Rock\", \"Paper\", \"Scissors\"]\n\n#Generate a random choice\nplayer2 = random.choice(options)\n\n#Print out the variables\n# print(f\"Player 1 chose {player1} and Player 2 chose {player2}!\")\n\nif player1 == player2:\n    print(\"It's a tie!\")\nelif player1 == \"Rock\":\n    if player2 == \"Scissors\":\n        print(\"Player 1 wins!\")\n    else:\n        print(\"Player 2 wins!\")\nelif player1 == \"Paper\":\n    if player2 == \"Rock\":\n        print(\"Player 1 wins!\")\n    else:\n        print(\"Player 2 wins!\")\nelif player1 == \"Scissors\":\n    if player2 == \"Paper\":\n        print(\"Player 1 wins!\")\n    else:\n        print(\"Player 2 wins!\")",
  temperature=0.97,
  max_tokens=1097,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
