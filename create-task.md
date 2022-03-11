{% include navigation.html %}

Performance Task Idea: Memory Game

    My performance task centers around a memory game for our website.
    The page will be in the form of a pop-up that activates when a user first visits either one of the store pages.
        It will ask the user if they are interested in possibly earning a 25% discount on their first order.
        In order for the user to win this discount, they must complete the game, following the instructions.

How it works

    A user will interact with cards that are laid out on the screen.
    They will have only one chance to look at a card.
    They will then have a chance to click another card to see if the two cards match.

This picture can be used as reference; the black cards are ones that have yet to be unturned, while the white card shown has been turned around. -> In this situation, the user would have 1 try to match this white card to another white card from the unturned pool of cards.

    The user will then proceed to click a different card, hoping it to be a match
        If it is a match, then both cards will be flipped up, eliminating them from the possible matches.

The screen would look something like this if that were to happen.

    However, if the card is not a match, then they will both be turned upside down, and cannot be turned back up. The game is still able to function because the user is now aware of the locations of two possible matches.

This is what the front-end would look like if the user chose a card that was not a match. Red and white are both flipped cards, but are not the same, so they will be turned back down in a second to look like this:

The two cards would be flipped back over, and the user would have to try a different variation to get a match, without being able to turn over the cards that they have already chosen.

    This will be unique to our website because the red, white, and black boxes shown to model as an example will be replaced with pictures of tea and tee. This will help the user learn more about the tea and tee we have available while also having an opportunity to receive a discount.

Requirements
Requirements 	How I plan on meeting them
Use of List/Collection Types 	Using the database to access images in a random order
Input 	User input is done through the cards
Procedure 	Functions that take the input and produce an output as a result
Algorithm 	Iteration of image display, sequencing of image backs, and Javascript functions to flip images and match them
Calls to procedure 	Card calls to procedure based on input
Instruction for output 	Instructions on screen
Comments and Acknowledgements 	Present throughout the code
