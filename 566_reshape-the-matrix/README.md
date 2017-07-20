b'<div class="question-description">\n<p><p>In MATLAB, there is a very useful function called \'reshape\', which can reshape a matrix into a new one with different size but keep its original data.\r\n</p>\n<p>\r\nYou\'re given a matrix represented by a two-dimensional array, and two <b>positive</b> integers <b>r</b> and <b>c</b> representing the <b>row</b> number and <b>column</b> number of the wanted reshaped matrix, respectively.</p>\n<p>The reshaped matrix need to be filled with all the elements of the original matrix in the same <b>row-traversing</b> order as they were.\r\n</p>\n<p>\r\nIf the \'reshape\' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.\r\n</p>\n<p><b>Example 1:</b><br/>\n<pre>\r\n<b>Input:</b> \r\nnums = \r\n[[1,2],\r\n [3,4]]\r\nr = 1, c = 4\r\n<b>Output:</b> \r\n[[1,2,3,4]]\r\n<b>Explanation:</b><br/>The <b>row-traversing</b> of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.\r\n</pre>\n</p>\n<p><b>Example 2:</b><br>\n<pre>\r\n<b>Input:</b> \r\nnums = \r\n[[1,2],\r\n [3,4]]\r\nr = 2, c = 4\r\n<b>Output:</b> \r\n[[1,2],\r\n [3,4]]\r\n<b>Explanation:</b><br/>There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.\r\n</pre>\n</br></p>\n<p><b>Note:</b><br/>\n<ol>\n<li>The height and width of the given matrix is in range [1, 100].</li>\n<li>The given r and c are all positive.</li>\n</ol>\n</p></p>\n</div>'