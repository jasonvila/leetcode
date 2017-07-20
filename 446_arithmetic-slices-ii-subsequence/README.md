b'<div class="question-description">\n<p><p>A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.</p>\n<p>For example, these are arithmetic sequences:</p>\n<pre>1, 3, 5, 7, 9\r\n7, 7, 7, 7\r\n3, -1, -5, -9</pre>\n<p>The following sequence is not arithmetic.</p> <pre>1, 1, 2, 5, 7</pre>\n<br/>\n<p>A zero-indexed array A consisting of N numbers is given. A <b>subsequence</b> slice of that array is any sequence of integers (P<sub>0</sub>, P<sub>1</sub>, ..., P<sub>k</sub>) such that 0 \xe2\x89\xa4 P<sub>0</sub> &lt; P<sub>1</sub> &lt; ... &lt; P<sub>k</sub> &lt; N.</p>\n<p>A <b>subsequence</b> slice (P<sub>0</sub>, P<sub>1</sub>, ..., P<sub>k</sub>) of array A is called arithmetic if the sequence A[P<sub>0</sub>], A[P<sub>1</sub>], ..., A[P<sub>k-1</sub>], A[P<sub>k</sub>] is arithmetic. In particular, this means that k \xe2\x89\xa5 2.</p>\n<p>The function should return the number of arithmetic subsequence slices in the array A. </p>\n<p>The input contains N integers. Every integer is in the range of -2<sup>31</sup> and 2<sup>31</sup>-1 and 0 \xe2\x89\xa4 N \xe2\x89\xa4 1000. The output is guaranteed to be less than 2<sup>31</sup>-1.</p>\n<br/>\n<p><b>Example:</b>\n<pre>\r\n<b>Input:</b> [2, 4, 6, 8, 10]\r\n\r\n<b>Output:</b> 7\r\n\r\n<b>Explanation:</b>\r\nAll arithmetic subsequence slices are:\r\n[2,4,6]\r\n[4,6,8]\r\n[6,8,10]\r\n[2,4,6,8]\r\n[4,6,8,10]\r\n[2,4,6,8,10]\r\n[2,6,10]\r\n</pre>\n</p></p>\n</div>'