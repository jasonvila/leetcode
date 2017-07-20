b'<div class="question-description">\n<p><p>\r\nClone an undirected graph. Each node in the graph contains a <code>label</code> and a list of its <code>neighbors</code>.\r\n</p>\n<div>\n<br/>\n<b>OJ\'s undirected graph serialization:</b>\n<p>\r\nNodes are labeled uniquely.\r\n</p>\r\n\r\nWe use <code>#</code> as a separator for each node, and <code>,</code> as a separator for node label and each neighbor of the node.\r\n</div></p>\n<p>\r\nAs an example, consider the serialized graph <code><font color="red">{<font color="black">0</font>,1,2#</font><font color="blue"><font color="black">1</font>,2#</font><font color="green"><font color="black">2</font>,2}</font></code>.\r\n</p>\n<p>\r\nThe graph has a total of three nodes, and therefore contains three parts as separated by <code>#</code>.\r\n<ol>\n<li>First node is labeled as <code><font color="black">0</font></code>. Connect node <code><font color="black">0</font></code> to both nodes <code><font color="red">1</font></code> and <code><font color="red">2</font></code>.</li>\n<li>Second node is labeled as <code><font color="black">1</font></code>. Connect node <code><font color="black">1</font></code> to node <code><font color="blue">2</font></code>.</li>\n<li>Third node is labeled as <code><font color="black">2</font></code>. Connect node <code><font color="black">2</font></code> to node <code><font color="green">2</font></code> (itself), thus forming a self-cycle.</li>\n</ol>\n</p>\n<p>\r\nVisually, the graph looks like the following:\r\n<pre>\r\n       1\r\n      / \\\r\n     /   \\\r\n    0 --- 2\r\n         / \\\r\n         \\_/\r\n</pre>\n</p>\n</div>'