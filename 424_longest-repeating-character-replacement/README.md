b'<div class="question-description">\n<p><p>Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most <i>k</i> times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.</p>\n<p><b>Note:</b><br/>\r\nBoth the string\'s length and <i>k</i> will not exceed 10<sup>4</sup>.\r\n</p>\n<p>\n<b>Example 1:</b>\n<pre>\r\n<b>Input:</b>\r\ns = "ABAB", k = 2\r\n\r\n<b>Output:</b>\r\n4\r\n\r\n<b>Explanation:</b>\r\nReplace the two \'A\'s with two \'B\'s or vice versa.\r\n</pre>\n</p>\n<p>\n<b>Example 2:</b>\n<pre>\r\n<b>Input:</b>\r\ns = "AABABBA", k = 1\r\n\r\n<b>Output:</b>\r\n4\r\n\r\n<b>Explanation:</b>\r\nReplace the one \'A\' in the middle with \'B\' and form "AABBBBA".\r\nThe substring "BBBB" has the longest repeating letters, which is 4.\r\n</pre>\n</p></p>\n</div>'