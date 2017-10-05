# Go Fish Tutorial
Trying my hand at writing a tutorial that teaches students about basic data
structures and how to use them.

## Pseudocode
Basic rules of Go Fish:

- Each player gets 5 cards to start.
- If you get 4 of a kind, those cards are removed from your hand and you get a
point
- Your goal is to get 4 of a kind by asking other players for a given rank
(ex.: King, 10, 5, Ace, etc.)
- If they have a card with that rank, they must give all cards of that rank to
you. If they don't have it, you have to "go fish" and draw a card from the deck.
- If you are successful, you can ask again until you have to go fish.

### Generating a deck of cards
Typing out the deck of cards individually is a huge pain, so let's generate it
procedurally!

Here's what we know about a standard deck of cards:
- There are 4 suits (hearts, diamonds, spades, clubs)
- There are numbered ranks from 2-10, 'royal' ranks from Jack-Ace
- We need to generate cards from each suit, for each of the ranks
