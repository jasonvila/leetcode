b'<div class="question-description">\n<p><p>Given the running logs of <b>n</b> functions that are executed in a nonpreemptive single threaded CPU, find the exclusive time of these functions. </p>\n<p>Each function has a unique id, start from <b>0</b> to <b>n-1</b>. A function may be called recursively or by another function.</p>\n<p>A log is a string has this format : <code>function_id:start_or_end:timestamp</code>. For example, <code>"0:start:0"</code> means function 0 starts from the very beginning of time 0. <code>"0:end:0"</code> means function 0 ends to the very end of time 0. </p>\n<p>Exclusive time of a function is defined as the time spent within this function, the time spent by calling other functions should not be considered as this function\'s exclusive time. You should return the exclusive time of each function sorted by their function id.</p>\n<p><b>Example 1:</b><br/>\n<pre>\r\n<b>Input:</b>\r\nn = 2\r\nlogs = \r\n["0:start:0",\r\n "1:start:2",\r\n "1:end:5",\r\n "0:end:6"]\r\n<b>Output:</b>[3, 4]\r\n<b>Explanation:</b>\r\nFunction 0 starts at time 0, then it executes 2 units of time and reaches the end of time 1. \r\nNow function 0 <b>calls function 1</b>, function 1 starts at time 2, executes 4 units of time and end at time 5.\r\nFunction 0 is running again at time 6, and also end at the time 6, thus executes 1 unit of time. \r\nSo function 0 totally execute 2 + 1 = 3 units of time, and function 1 totally execute 4 units of time.\r\n</pre>\n</p>\n<p><b>Note:</b><br/>\n<ol>\n<li>Input logs will be sorted by timestamp, NOT log id.</li>\n<li>Your output should be sorted by function id, which means the 0th element of your output corresponds to the exclusive time of function 0.</li>\n<li>Two functions won\'t start or end at the same time.</li>\n<li>Functions could be called recursively, and will always end.</li>\n<li>1 &lt;= n &lt;= 100</li>\n</ol>\n</p></p>\n</div>'