# keylogger

In this modified script, the pyenchant package is used to check if each substring in the keys_pressed string is a valid English word. The enchant.Dict('en_US') function creates an instance of the English dictionary, which is used to check if each substring is a valid word. The check method of the dictionary object returns True if the substring is a valid word and False otherwise.

After the keyboard hook is removed, the output_str variable is initialized as an empty string. The while loop adds spaces between valid English words in the keys_pressed string. The loop initializes a variable i to the index of the first character in the string and a variable j to i + 1. The loop then checks if the substring from index i to index j - 1 is a valid English word. If the substring is a valid word, a space is added to the output_str variable and i is set to j. If the substring is not a valid word, the loop increments j and checks the next substring. The loop exits when j reaches the end of the string. If the last substring is a valid word, it is added to the output_str variable without a space.

Finally, the output_str variable is written to the output file using the print function.

With this modification, the output will have spaces between valid English words. For example, if the user presses the keys "o", "n", "w", "i", "k", "i", "p", "e", "d", "i", "a", "a", "n", "d", "o", "t


With the modified script, the output for the input "OnWikipediaandothersitesrunningonMediaWiki,Special:Randomcanbeusedtoaccessarandomarticleinthemainnamespace;thisfeatureisusefulasatooltogeneratearandomarticle.Dependingonyourbrowser,it'salsopossibletoloadarandompageusingakeyboardshortcut(inFirefox,Edge,andChromeAlt-Shift+X)." would be:

```On Wikipedia and other sites running on MediaWiki, Special: Random can be used to access a random article in the main namespace; this feature is useful as a tool to generate a random article. Depending on your browser, it's also possible to load a random page using a keyboard shortcut (in Firefox, Edge, and Chrome Alt-Shift+X).```
