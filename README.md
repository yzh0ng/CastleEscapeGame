# CastleEscapeGame

#### the player’s experience
The player enters their nom-du-guerre
Player is told that they are in the "Grand Foyer" of the house and that there are
3 doors, 1 to the "Study" on the left, 1 to a "Documents" room straight ahead, and
1 to a "Movies" room on the right.
A "Grand Foyer" is drawn ( – a box with the label "Grand Foyer") with 3 doors,🐢
one each on the left, right, and back walls, labeled "S", "D", and "M". (The doors
can be simple, like just sections of wall drawn in green or something.)
The player is then told that the front door to the Foyer has closed and locked! The
goal of the game is find a way to escape! Don’t forget to tell your player they are
trapped, and you can draw the Front Door as a red bit of wall.
Now you have the first part of a diagram of the mansion!
The player is asked to choose a door to step though.
The player enters the chosen room! The room can be spooky or whatever you want
(like: `print("Oh, {player_name}, you just felt an evil presence pass through
you!")` or whatever.
The map diagram is updated, and the player is told what’s in the room depending on
which room they went into:
* in the Study, there is a pen and paper on one table, and a pen, a calculator and
a ledger on another.
* in the Documents room, there are two documents: a Will and a Car Title
* in the Movie room, there are two movies: Family Vacation and Watch Me Now
If your player enters the
* Movie room, they are told that the door back to the Foyer has closed and locked –
so, red door to (not) get back to the Foyer! Suggest that they watch a movie. If
they choose Watch Me Now, give them the magic phrase to escape! If they choose
Family Vacation, give them an incorrect phrase. Either way, rush them through a
secret passage to the Study! Update your diagram; you can indicate the secret
passage on the diagram however you wish.
* Study, *_if they enter it from the Movie room_*, they are told that the room to
the Foyer is locked, and they must type what the movie told them to escape! Let
them type their input, and let them out if they type the phrase from the Watch Me
Now movie, and tell them they lost if they type the phrase from the Family Vacation
movie. Either way, the game is over.
* Study, _if they enter it from the Foyer_, they are only told the contents of the
room. They cannot escape if they enter the study from the Foyer; they must go back
to the Foyer the way they came, and the game continues.
