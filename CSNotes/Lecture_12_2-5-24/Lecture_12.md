Software Development

- Assignments will evolve less into specific implementations and more into making stuff on our own to satisfy requirements.
- Applicable to real-life. Most jobs and work will just shove you into a codebase and require for things to be done.
- Software development is a team sport.

Weeks 6-9:

- Softawre development lifecycle
- Software design
- Software validation
- Software libraries

Software Development Lifecycle:

- Stakeholders need to be considered. The people who will use and pay for what you make.
- Specification- Requirements engineering, deciding the bounds of what needs to be completed before it's done.
- Design- Structuring the software before thinking of implementing/writing the code.
- Validation- Testing created software to ensure that it works and meets the requirements.
- Evolution- Updating, maintaining, and expanding on existing software.

Software Design:

- Useful book on software design: A Philosophy of Software Design (John Ousterhout)
- The goal of software design is to reduce complexity. 

Symptoms of Complexity:

- Cognitive load- How much a developer has to understand to work with a piece of code. Software should be designed for ease of reading, not for ease of writing, because your code will be read much more than it is written.
- Change amplification- Making sure that the code you write is not implemented too many times, as when reqirements are changed, every line of code will have to be changed. To solve this, you can put it into a function and make the changing much easier.
- Unknown unknowns- Things that you should've known, but had no way of knowing beforehand. For example, if you're implementing something and there's a special exception that's screwing with your code, but no one knows why there's a special exception there. This is why you need proper documentation.

Causes of Complexity:
- Dependencies- Code segments rely on other code segments.
- Obscurity- When code is poorly documented or has no obvious meaning.