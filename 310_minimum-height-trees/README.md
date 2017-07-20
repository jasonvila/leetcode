b'<div class="question-description">\n<p><p>\r\n    For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs).\r\n    Given such a graph, write a function to find all the MHTs and return a list of their root labels.\r\n</p>\n<p>\n<b>Format</b><br/>\r\n    The graph contains <code>n</code> nodes which are labeled from <code>0</code> to <code>n - 1</code>.\r\n    You will be given the number <code>n</code> and a list of undirected <code>edges</code> (each edge is a pair of labels).\r\n</p>\n<p> \r\nYou can assume that no duplicate edges will appear in <code>edges</code>. Since all edges are\r\n    undirected, <code>[0, 1]</code> is the same as <code>[1, 0]</code> and thus will not appear together in\r\n    <code>edges</code>.\r\n</p>\n<p>\n<b>Example 1:</b>\n</p>\n<p>\r\n    Given <code>n = 4</code>, <code>edges = [[1, 0], [1, 2], [1, 3]]</code>\n</p>\n<pre>\r\n        0\r\n        |\r\n        1\r\n       / \\\r\n      2   3\r\n</pre>\n<p>\r\n    return <code> [1]</code>\n</p>\n<p>\n<b>Example 2:</b>\n</p>\n<p>\r\n    Given <code>n = 6</code>, <code>edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]</code>\n</p>\n<pre>\r\n     0  1  2\r\n      \\ | /\r\n        3\r\n        |\r\n        4\r\n        |\r\n        5\r\n</pre>\n<p>\r\n    return <code> [3, 4]</code>\n</p>\n<p>\n<b>Note</b>:\r\n</p>\n<p>\r\n    (1) According to the <a href="https://en.wikipedia.org/wiki/Tree_(graph_theory)" target="_blank">definition\r\n    of tree on Wikipedia</a>: \xe2\x80\x9ca tree is an undirected graph in which any two vertices are connected by\r\n    <i>exactly</i> one path. In other words, any connected graph without simple cycles is a tree.\xe2\x80\x9d\r\n</p>\n<p>\r\n    (2) The height of a rooted tree is the number of edges on the longest downward path between the root and a\r\n    leaf.\r\n</p>\n<p><b>Credits:</b><br/>Special thanks to <a href="https://leetcode.com/discuss/user/dietpepsi">@dietpepsi</a> for adding this problem and creating all test cases.</p></p>\n</div>'