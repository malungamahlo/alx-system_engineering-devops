
stmortem: Farm Product Review - Internal Server Error
Issue Summary:
The Farm Product Review (FPR) staging environment experienced a critical issue on Friday, May 10th, 2024, from 14:30 PST to 16:00 PST (2 hours). During this time, users attempting to register or submit product reviews encountered a generic "Internal Server Error" message. No portion of the live environment was affected.
Timeline:
14:30 PST: An engineer monitoring the staging environment receives alerts indicating a significant increase in error logs from the Django application.
14:35 PST: The engineer investigates the error logs and discovers a surge in "KeyError: 'user'" errors originating from the user registration and product review submission functionalities.
14:40 PST: Initial assumption is a database connection issue. The engineer checks the database server health and confirms normal operation.
14:45 PST - 15:15 PST: The engineer investigates the Django application code, focusing on user authentication and session management. No apparent errors are found.
15:15 PST: The decision is made to escalate the issue to the full development team for a broader investigation.
15:30 PST: During a team meeting, a developer suggests checking recent code commits related to user management functionalities.
15:45 PST: Code review reveals a recently merged pull request that inadvertently introduced a typo in a variable name within the user model serializer. This typo prevented the user object from being correctly retrieved during registration and review submission.
15:50 PST: The development team reverts the problematic pull request on the staging environment.
16:00 PST: The staging environment is confirmed to be functioning normally. User registration and review submission functionalities work as expected.
Root Cause and Resolution:
The root cause of the outage was a typographical error introduced in a recently merged pull request. The typo was present in a variable name within the user model serializer, preventing the user object from being fetched during user registration and product review submission. This resulted in the "KeyError: 'user'" errors and the subsequent "Internal Server Error" messages displayed to users.
The issue was resolved by reverting the problematic pull request on the staging environment. This restored the original, functional code and allowed user registration and review submission to proceed normally.
Corrective and Preventative Measures:
Improve code review practices: Implement a more rigorous code review process to catch potential errors before merging pull requests.
Enforce code formatting and linting: Utilize code formatting tools and linters to automatically detect and flag potential issues like typos and naming inconsistencies.
Increase automated testing coverage: Expand unit and integration tests to cover user registration and review submission functionalities more comprehensively.
Invest in developer education: Conduct training sessions on common coding errors and best practices for secure development.


