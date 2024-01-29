<section class="clearfix"></section>

---
# API Test Run Report


||**Date**||Jan 29, 2024 16:54||
||**Duration**||727ms||
||**Framework**||<span class="testflows-logo"></span> [<span class="logo-test">Test</span><span class="logo-flows">Flows</span>] 2.0.240111.1210833||


## Summary
<div class="chart"><div class="c100 p62 green"><span>62.5%</span><span class="title">OK</span><div class="slice"><div class="bar"></div><div class="fill"></div></div></div>
<div class="c100 p37 red"><span>37.5%</span><span class="title">Fail</span><div class="slice"><div class="bar"></div><div class="fill"></div></div></div>
</div>

## Statistics
<span></span> | Units | <span class="result result-ok">OK</span> | <span class="result result-fail">Fail</span>
--- | --- | --- | ---
Modules | <center>1</center> |  | <center>1</center>
Features | <center>1</center> |  | <center>1</center>
Scenarios | <center>6</center> | <center>5</center> | <center>1</center>
Steps | <center>28</center> | <center>27</center> | <center>1</center>



## Fails
<table class="stripped danger">
<thead><tr><th><span style="display: block; min-width: 20vw;">Test Name</span></th><th><span style="display: block; min-width: 90px;">Result</span></th><th>Message</th></tr></thead>
<tbody>
<tr><td>/API</td><td><span class="result result-fail">Fail</span>  727ms</td><td><div style="max-width: 30vw; overflow-x: auto;"><pre>AssertionError
Traceback (most recent call last):
  File "/home/nur/Downloads/Telegram Desktop/QA/send_data/tests/api_tests/regression.py", line 18, in <module>
    regression()
  File "/home/nur/Downloads/Telegram Desktop/QA/send_data/tests/api_tests/regression.py", line 14, in regression
    Feature(run=load("websocket_tests.websocket_scenarios", test="websocket_scenarios"))
  File "/home/nur/Downloads/Telegram Desktop/QA/send_data/tests/api_tests/websocket_tests/websocket_scenarios.py", line 234, in websocket_scenarios
    Scenario(run=scenario, flags=TE)
  File "/home/nur/Downloads/Telegram Desktop/QA/send_data/tests/api_tests/websocket_tests/websocket_scenarios.py", line 228, in unauthorized_user_cannot_view_others_package
    assert get_user_two_package_data_response.status_code >= 400
AssertionError</pre></div></td></tr>
<tr><td>/API/websocket scenarios</td><td><span class="result result-fail">Fail</span>  717ms</td><td><div style="max-width: 30vw; overflow-x: auto;"><pre>AssertionError
Traceback (most recent call last):
  File "/home/nur/Downloads/Telegram Desktop/QA/send_data/tests/api_tests/regression.py", line 18, in <module>
    regression()
  File "/home/nur/Downloads/Telegram Desktop/QA/send_data/tests/api_tests/regression.py", line 14, in regression
    Feature(run=load("websocket_tests.websocket_scenarios", test="websocket_scenarios"))
  File "/home/nur/Downloads/Telegram Desktop/QA/send_data/tests/api_tests/websocket_tests/websocket_scenarios.py", line 234, in websocket_scenarios
    Scenario(run=scenario, flags=TE)
  File "/home/nur/Downloads/Telegram Desktop/QA/send_data/tests/api_tests/websocket_tests/websocket_scenarios.py", line 228, in unauthorized_user_cannot_view_others_package
    assert get_user_two_package_data_response.status_code >= 400
AssertionError</pre></div></td></tr>
<tr><td>/API/websocket scenarios/unauthorized user cannot view others package</td><td><span class="result result-fail">Fail</span>  324ms</td><td><div style="max-width: 30vw; overflow-x: auto;"><pre>AssertionError
Traceback (most recent call last):
  File "/home/nur/Downloads/Telegram Desktop/QA/send_data/tests/api_tests/regression.py", line 18, in <module>
    regression()
  File "/home/nur/Downloads/Telegram Desktop/QA/send_data/tests/api_tests/regression.py", line 14, in regression
    Feature(run=load("websocket_tests.websocket_scenarios", test="websocket_scenarios"))
  File "/home/nur/Downloads/Telegram Desktop/QA/send_data/tests/api_tests/websocket_tests/websocket_scenarios.py", line 234, in websocket_scenarios
    Scenario(run=scenario, flags=TE)
  File "/home/nur/Downloads/Telegram Desktop/QA/send_data/tests/api_tests/websocket_tests/websocket_scenarios.py", line 228, in unauthorized_user_cannot_view_others_package
    assert get_user_two_package_data_response.status_code >= 400
AssertionError</pre></div></td></tr>
<tbody>
</table>

## Results
Test Name | Result | <span style="display: block; min-width: 100px;">Duration</span>
--- | --- | --- 
/API | <span class="result result-fail">Fail</span> | 727ms
/API/websocket scenarios | <span class="result result-fail">Fail</span> | 717ms
/API/websocket scenarios/authorized user can send package | <span class="result result-ok">OK</span> | 344ms
/API/websocket scenarios/authorized user can view specific package | <span class="result result-ok">OK</span> | 18ms
/API/websocket scenarios/invalid package data returns validation error | <span class="result result-ok">OK</span> | 12ms
/API/websocket scenarios/unauthorized user cannot send package | <span class="result result-ok">OK</span> | 3ms
/API/websocket scenarios/unauthorized user cannot view others package | <span class="result result-fail">Fail</span> | 324ms
/API/websocket scenarios/valid package data is successfully saved | <span class="result result-ok">OK</span> | 12ms


---
Generated by <span class="testflows-logo"></span> [<span class="logo-test">Test</span><span class="logo-flows">Flows</span>] Open-Source Test Framework v2.0.240111.1210833

[<span class="logo-test">Test</span><span class="logo-flows">Flows</span>]: https://testflows.com
