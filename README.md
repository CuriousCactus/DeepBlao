# DeepBlao
A rules-aware digital board for the East African board game Bao, written in Python

## The board

- The board is used by clicking on a hole with two or more 'beans' to pick up the bean and 'sow' them.
- Right-click to move right, left-click to move left.

## Rules

Adapted from http://www.gamecabinet.com/rules/Bao2.html

```
         Player 2
(2)(2)(2)(2)(2)(2)(2)(2) outer
(2)(2)(2)[2](2)(2)(2)(2) inner
~~~~~~~~~~~~~~~~~~~~~~~~
(2)(2)(2)(2)[2](2)(2)(2) inner
(2)(2)(2)(2)(2)(2)(2)(2) outer
         Player 1
```



The board (bao) contains four rows of eight holes.

The opening position is shown in Figure 1. Sixty-four seeds are used, with two per hole.

The first player is chosen by lot. In subsequent games the winner of the previous game plays first.

Each player owns and 'sows' (moves) seeds only around the two nearest rows of holes. The objective is to leave the opponent with an empty inner row. Players take alternate moves.

One 'turn' or 'move' may consist of several 'lifts' and 'sowings', and possibly of several captures. A move starts by the player lifting the seeds in one hole and sowing them one by one into the subsequent holes, moving either in a clockwise or anti-clockwise direction, as desired.

There are three possible results of this initial sowing:

- the last seed falls in an occupied inner-row hole and seeds are captured ("eaten") from the adversary's inner-row hole immediately opposite.
- the last seed falls in an occupied hole in the outer row, or one in the inner row opposite which no seeds are available for capture. In this case all the seeds in that last hole (including the newcomer) are lifted and sown on (a 'relay') in the same direction;
- the last seed falls in an empty hole and the move peters out (the player "sleeps") and play passes to the opponent;
A move of the first kind is called mtaji. The other two are known as takata.

Captured seeds are sown along the player's inner row starting at the end-hole (kichwa) in the same direction as the previous sowing. Thus if the move leading up to the capture was anti-clockwise the captured seeds will be sown in starting at the anti-clockwise kichwa (see Figure 1).

However, if the capture is from the first, second, seventh or eighth hole of the inner row (called kimbi) the captured seeds are sown in from the nearest end-hole. This may mean that the direction of sowing is reversed. No change of direction is made when making a 'relay' (not a capture) from a kimbi hole.

During a mtaji, every subsequent 'relay' may occasion a capture if the circumstances described above recur.

A 'singleton' cannot be lifted and sown on. A player left only with 'singletons' to move has thus lost the game.

Fifteen is the highest number of seeds that can be lifted to begin a mtaji move. Any higher number of seeds can only be lifted for a takata move or, when a previous sowing ends there, for a subsequent relay of the same move, whether takata or mtaji.

Each move can be defined as mtaji or takata before it is played. If no initial lift endangers any of the adversary's seeds then takata is the only possibility. At no point subsequently during the same takata will a capture occur - moves ending in occupied holes cause a further relay, whether there are seeds in the opposite hole or not.

A takata move is allowed only if no mtaji is available. If several mtaji possibilities exist, any may be chosen.

No takata move may be made from an outer-row hole if an alternative takata move is possible from the inner row. However, a mtaji move may begin from either row subject to the limits on the number of seeds involved.

All seeds in the outer row are safe, captures only occur from inner-row holes.

A player loses the game when their inner row has no seeds.

A takata move from an end hole which is the only occupied inner row hole, if played back - across the players outer row, results in immediate defeat. The rationale is that the inner row is empty (even if the lone hole contains more than 8 seeds and so would eventually have reached back round onto the inner row).
