b'<div class="question-description">\n<p><p>Given the root of a binary tree, then value <code>v</code> and depth <code>d</code>, you need to add a row of nodes with value <code>v</code> at the given depth <code>d</code>. The root node is at depth 1. </p>\n<p>The adding rule is: given a positive integer depth <code>d</code>, for each NOT null tree nodes <code>N</code> in depth <code>d-1</code>, create two tree nodes with value <code>v</code> as <code>N\'s</code> left subtree root and right subtree root. And <code>N\'s</code> <b>original left subtree</b> should be the left subtree of the new left subtree root, its <b>original right subtree</b> should be the right subtree of the new right subtree root. If depth <code>d</code> is 1 that means there is no depth d-1 at all, then create a tree node with value <b>v</b> as the new root of the whole original tree, and the original tree is the new root\'s left subtree.</p>\n<p><b>Example 1:</b><br/>\n<pre>\r\n<b>Input:</b> \r\nA binary tree as following:\r\n       4\r\n     /   \\\r\n    2     6\r\n   / \\   / \r\n  3   1 5   \r\n\r\n<b>v = 1</b>\r\n\r\n<b>d = 2</b>\r\n\r\n<b>Output:</b> \r\n       4\r\n      / \\\r\n     1   1\r\n    /     \\\r\n   2       6\r\n  / \\     / \r\n 3   1   5   \r\n\r\n</pre>\n</p>\n<p><b>Example 2:</b><br/>\n<pre>\r\n<b>Input:</b> \r\nA binary tree as following:\r\n      4\r\n     /   \r\n    2    \r\n   / \\   \r\n  3   1    \r\n\r\n<b>v = 1</b>\r\n\r\n<b>d = 3</b>\r\n\r\n<b>Output:</b> \r\n      4\r\n     /   \r\n    2\r\n   / \\    \r\n  1   1\r\n /     \\  \r\n3       1\r\n</pre>\n</p>\n<p><b>Note:</b><br/>\n<ol>\n<li>The given d is in range [1, maximum depth of the given tree + 1].</li>\n<li>The given binary tree has at least one tree node.</li>\n</ol>\n</p></p>\n</div>'