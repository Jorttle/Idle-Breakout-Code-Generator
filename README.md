# Idle-Breakout-Code-Generator
Idle Breakout is a game that allows you to import and export your save data. This save data is entirely stored on the code it gives you when you press "export".

When decoded from base64, the output looks like this:

`1,24,0,0,0,0,0,0,0,0,0,1,1,0,0,999999,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,`

Here are what the different numbers mean:

`{level},{money},{gold},{gold_claim},0,0,0,0,0,0,0,0,0,0,{Unkown number},{Large number},0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,{Skills: 1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0 :End Skills},{black_bricks},0,0,0,{boss_level},{skill_points},0,0,0,`
# 

level: Level.

money: Money.

gold: Amount of gold you have.

gold_claim: How much gold you should claim on prestige.

black_bricks: Number of Black Brick Points you have.

boss_level: What level boss you will fight.

skill_points: Number of skill points you have, used to buy skills.

Unkown number: The only floating point number on this list. Seems to stay the same even when clearing data. 

Large number: A large number, was 999999 for me.

Skills: This represents what skills you have. 1's represent True and 0 represents False. I suspect the four ones in a row represent the chain of skills you get. I have not added function for this.

(These would be the first four 1's (1,1,1,1))

<img width="346" height="234" alt="Screenshot from 2025-10-05 18-23-56" src="https://github.com/user-attachments/assets/eb31ff8b-09ec-4912-8dca-6be0335eda9b" />



# How to import data

IMPORTANT: IMPORTING DATA WILL DELETE ALL YOUR PROGRESS!

Select the Settings icon in the top right corner

<img width="794" height="595" alt="image" src="https://github.com/user-attachments/assets/dfe713d5-68e6-40b3-84bb-e6c5fdb69621" />

Select the import button

<img width="794" height="595" alt="image(1)" src="https://github.com/user-attachments/assets/21afa54c-fe91-4ef8-b481-af1e33d7c60e" />

Paste your code into the text box that appears.

If a text box does not appear, try refreshing the page. If that doesn't work, idk what to tell you :(

# BE CARFUL WITH LEVEL NUMBER

Do not set the number too high or the game will turn black. One billion (1000000000) is generally safe, but it may be too much for weak computers.

# Example output

Money: 1000000000000000000000000000000000000000000000

Level: 10000

Gold: 1000000000000000000000000000000000000000000000

Gold on reset: 0

Black Bricks: 1000000000000000000000000000000000000000000000

Skill points: 100
 `MTAwMDAsMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMCwxMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwxMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwLDAsMCwwLDAsMTAwLDAsMCwwLA==`
