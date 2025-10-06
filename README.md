# Idle-Breakout-Code-Generator
Idle Breakout is a game that allows you to import and export your save data. This save data is entirely stored on the code it gives you when you press "export".

When decoded from base64, the output looks like this:

1,24,0,0,0,0,0,0,0,0,0,1,1,0,0,999999,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,

Here are what the different numbers mean:

{level},{money},{gold},{gold_claim},0,0,0,0,0,0,0,0,0,0,{Unkown number},{Large number},0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,{black_bricks},0,0,0,{boss_level},{skill_points},0,0,0,

level: Level.

money: Money.

gold: Amount of gold you have.

gold_claim: How much gold you should claim on prestige.

black_bricks: Number of Black Brick Points you have.

boss_level: What level boss you will fight.

skill_points: Number of skill points you have, used to buy skills.

Unkown number: The only floating point number on this list. Seems to stay the same even when clearing data. 

Large number: A large number, was 999999 for me.
