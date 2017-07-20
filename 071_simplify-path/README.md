b'<div class="question-description">\n<p><p>Given an absolute path for a file (Unix-style), simplify it.</p>\n<p>For example,<br/>\n<b>path</b> = <code>"/home/"</code>, =&gt; <code>"/home"</code><br/>\n<b>path</b> = <code>"/a/./b/../../c/"</code>, =&gt; <code>"/c"</code><br/>\n</p>\n<p class="showspoilers"><a href="#" onclick="showSpoilers(this); return false;">click to show corner cases.</a></p>\n<div class="spoilers"><b>Corner Cases:</b>\n<p>\n<ul>\n<li>Did you consider the case where <b>path</b> = <code>"/../"</code>?<br/>\r\nIn this case, you should return <code>"/"</code>.</li>\n<li>Another corner case is the path might contain multiple slashes <code>\'/\'</code> together, such as <code>"/home//foo/"</code>.<br/>\r\nIn this case, you should ignore redundant slashes and return <code>"/home/foo"</code>.</li>\n</ul></p>\n</div></p>\n</div>'