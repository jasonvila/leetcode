b'<div class="question-description">\n<p><p>\r\nAccording to the <a href="https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life" target="_blank">Wikipedia\'s article</a>: "The <b>Game of Life</b>, also known simply as <b>Life</b>, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."\r\n</p>\n<p>\r\nGiven a <i>board</i> with <i>m</i> by <i>n</i> cells, each cell has an initial state <i>live</i> (1) or <i>dead</i> (0). Each cell interacts with its <a href="https://en.wikipedia.org/wiki/Moore_neighborhood" target="_blank">eight neighbors</a> (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):\r\n</p>\n<p>\n<ol>\n<li>Any live cell with fewer than two live neighbors dies, as if caused by under-population.</li>\n<li>Any live cell with two or three live neighbors lives on to the next generation.</li>\n<li>Any live cell with more than three live neighbors dies, as if by over-population..</li>\n<li>Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.</li>\n</ol>\n</p>\n<p>\r\nWrite a function to compute the next state (after one update) of the board given its current state.</p>\n<p>\n<b>Follow up</b>: <br/>\n<ol>\n<li>Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.</li>\n<li>In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?</li>\n</ol>\n</p>\n<p><b>Credits:</b><br>Special thanks to <a href="https://leetcode.com/discuss/user/jianchao.li.fighter">@jianchao.li.fighter</a> for adding this problem and creating all test cases.</br></p></p>\n</div>'