{% include navigation.html %}

### Performance Task Idea: Memory Game
* My performance task centers around a memory game for our website.
* The page will be in the form of a pop-up that activates when a user first visits either one of the store pages.
* It will ask the user if they are interested in possibly earning a 25% discount on their first order.
* In order for the user to win this discount, they must complete the game, following the instructions.

### How it works
* A user will interact with cards that are laid out on the screen.
* They will have only one chance to look at a card.
* They will then have a chance to click another card to see if the two cards match.

![](https://github.com/NinjaBreadLord/super-duper-bassoons/blob/eae82b2c56a8afc362814301fecb3a2c71e3f3e8/static/assets/Jun/ex.png?raw=true)

This picture can be used as reference; the black cards are ones that have yet to be unturned, while the white card shown has been turned around. -> In this situation, the user would have 1 try to match this white card to another white card from the unturned pool of cards.

* The user will then proceed to click a different card, hoping it to be a match
    - If it is a match, then both cards will be flipped up, eliminating them from the possible matches.

![](https://github.com/NinjaBreadLord/super-duper-bassoons/blob/eae82b2c56a8afc362814301fecb3a2c71e3f3e8/static/assets/Jun/ex2.png?raw=true)

The screen would look something like this if that were to happen.

* However, if the card is not a match, then they will both be turned upside down, and cannot be turned back up. The game is still able to function because the user is now aware of the locations of two possible matches.

![](https://github.com/NinjaBreadLord/super-duper-bassoons/blob/eae82b2c56a8afc362814301fecb3a2c71e3f3e8/static/assets/Jun/ex3.png?raw=true)

This is what the front-end would look like if the user chose a card that was not a match. Red and white are both flipped cards, but are not the same, so they will be turned back down in a second to look like this:
![](https://github.com/NinjaBreadLord/super-duper-bassoons/blob/eae82b2c56a8afc362814301fecb3a2c71e3f3e8/static/assets/Jun/ex4.png?raw=true)

The two cards would be flipped back over, and the user would have to try a different variation to get a match, without being able to turn over the cards that they have already chosen.
