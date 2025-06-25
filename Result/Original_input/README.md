📥 Original_input Kya Hai?
Ye woh original user input hota hai jo aap ne Runner.run() ya run_sync() ko diya tha.

⚙️ SDK ne aapka input internally process karne se pehle as-it-is preserve kiya hota hai.

💡 Example

result = Runner.run_sync(agent, input="Tell me about space.")
print(result.input)
Output:

"Tell me about space."
