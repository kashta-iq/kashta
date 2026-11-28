# كشتة: شغل محفوظ ينتظر أمر كاظم (لا ينزل قبل ما يكول)

Branch `pending` = main + everything below. Merge into main only when he says "عدل".

## 1. أحجار لودو جديدة (مسواة بالكود، commits on this branch)
- 10 looks in LPC (index.html): smile, zakh, crown, yaqut, neonx, micro, elem, orrery, scarab, cosmos.
- Files: cards/lp/<key>_<r|g|y|b>.webp (cut by _pending/cut.py from ludo-pieces-src/set1..10).
- Each player keeps his own colour (red player = 4 red pieces of the chosen look).
- Claude-artifact copy gets them through stkpack.js (artifact is at 511/512 files: never add files, pack them).

## 2. لوحتين لودو جديدة (ludo-boards/)
- board_marble.jpg, board_gold.jpg: to add as extra board skins, same 15x15 layout as NGIMG.ludo_board.
- Check grid alignment against the original before adding; fix small shifts.
- Board size stays as it is (he decided not to enlarge it).

## 3. لعبة «زلابية» (match-3, like Candy Crush) — zalabia/
- sweets.jpg (6 pieces: zalabia, baklava, kleicha, mann al-sama, date, dihina), bg_shop.jpg, icon.jpg.
- Special pieces (striped, glowing, colour bomb) made in code from the 6.

## 4. لعبة «دعبلة» (marble shooter, like Zuma) — da3bala/
- marbles.jpg (6: red green yellow blue purple white), special_date_bomb.jpg (date = pushes chain back, bomb = blast),
  lion_shooter.jpg (top-down Lion of Babylon, the shooter), icon.jpg,
  backgrounds: bg_rasheed, bg_samarra, bg_marshes, bg_babylon.

## Agreed rules for both new games
- Levels + friends' leaderboard + live online challenge (both).
- 50 levels each.
- 5 lives like Candy Crush (wait, or pay كشتات to refill).
- Win gives a few كشتات by stars (about 10–30).
- Style: cartoon pieces, luxurious frames/backgrounds.
- Every 10 levels a boss = one of the friends (bosses/boss1..5.jpg, cartoon armour portraits).
