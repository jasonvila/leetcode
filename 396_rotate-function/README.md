b'<div class="question-description">\n<p><p>\r\nGiven an array of integers <code>A</code> and let <i>n</i> to be its length.\r\n</p>\n<p>\r\nAssume <code>B<sub>k</sub></code> to be an array obtained by rotating the array <code>A</code> <i>k</i> positions clock-wise, we define a "rotation function" <code>F</code> on <code>A</code> as follow:\r\n</p>\n<p>\n<code>F(k) = 0 * B<sub>k</sub>[0] + 1 * B<sub>k</sub>[1] + ... + (n-1) * B<sub>k</sub>[n-1]</code>.</p>\n<p>Calculate the maximum value of <code>F(0), F(1), ..., F(n-1)</code>. \r\n</p>\n<p><b>Note:</b><br/>\n<i>n</i> is guaranteed to be less than 10<sup>5</sup>.\r\n</p>\n<p><b>Example:</b>\n<pre>\r\nA = [4, 3, 2, 6]\r\n\r\nF(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25\r\nF(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16\r\nF(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23\r\nF(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26\r\n\r\nSo the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.\r\n</pre>\n</p></p>\n</div>'