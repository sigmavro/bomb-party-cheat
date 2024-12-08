# bomb-party-cheat
horrible(best) cheat for the game bomb party on [jklm.fun](https://jklm.fun)
(warning, may bug)

# how to download!!!
1. download the .py file(you MUST have [python](https://python.org)) installed, [download is here](https://github.com/sigmavro/bomb-party-cheat/archive/refs/heads/main.zip)
2. go into your cmd and type ``` pip install pynput pyperclip pyautogui ```
4. run the python file(no its not malware, its unobfuscated you can check)
# how to use
1. go into ANY bomb party lobby.
2. click F2 while your mouse is hovering over the chat area
3. hover your mouse over the prompt when its your turn and click f4
4. then the script should go mouse your mouse to the chat box, open it, find a random word from the wordlist.txt file, type it in with a very fast speed(not instant bc thats really easy to get cheat accused and its literally like copy and paste speed) then it clicks enter and your goated
# additonal features
1. if you want to type words in chat, click f9 over the chat bar where you type msgs, then hover over the prompt and it should type a word in the chat area
2. typing speed config is where it says interval=0.07, change it to what ever you want or delete if you want instant typing

# warning
the script makes your keyboard REALLY delayed im pretty sure(unless thats js me), so dont use it if your not playing bomb party
# credit
uhh me bc i coded this bs in python(took 3 minutes 🤑)


# malware accusations
since people think everything is malware, you can check the sourcecode
1. the imports are for modules needed for the cheat
2. the on_press() function checks all pressed keys, if its either f2, f4, f8, or f9, it will do the respective feature
3. the on release function is lowkey for no reason i js added it bc thats one of the args in the listener function, it checks for esc and if you press esc the script closes.
4. ```with Listener(on_press=on_press, on_release=on_release) as listener: listener.join() ``` is the listener for the keys pressed.
5. yuhhh not malware!!
6. (ps, for some reason wd hates me so everything i make gets detected as malware if your REALLY scared this is malware, dont use it or check the source manually, you can open it in vscode and if you dont got vscode you can deaduzz open it in notepad)
