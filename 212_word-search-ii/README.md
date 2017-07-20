b'<div class="question-description">\n<p><p>\r\nGiven a 2D board and a list of words from the dictionary, find all words in the board.\r\n</p>\n<p>\r\nEach word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.\r\n</p>\n<p>\r\nFor example,<br/>\r\nGiven <b>words</b> = <code>["oath","pea","eat","rain"]</code> and <b>board</b> = \r\n<pre>\r\n[\r\n  [\'<span style="color:#d70">o</span>\',\'<span style="color:#d70">a</span>\',\'a\',\'n\'],\r\n  [\'e\',\'<span style="color:#d30">t</span>\',\'<span style="color:#d00">a</span>\',\'<span style="color:#d00">e</span>\'],\r\n  [\'i\',\'<span style="color:#d70">h</span>\',\'k\',\'r\'],\r\n  [\'i\',\'f\',\'l\',\'v\']\r\n]\r\n</pre>\r\n\r\nReturn <code>["eat","oath"]</code>.\r\n</p>\n<p>\n<b>Note:</b><br/>\r\nYou may assume that all inputs are consist of lowercase letters <code>a-z</code>.\r\n</p>\n<p class="showspoilers"><a href="#" onclick="showSpoilers(this); return false;">click to show hint.</a></p>\n<div class="spoilers"><p>You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?</p>\n<p>If the current candidate does not exist in all words\' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: <a href="https://leetcode.com/problems/implement-trie-prefix-tree/">Implement Trie (Prefix Tree)</a> first.</p>\n</div></p>\n</div>'