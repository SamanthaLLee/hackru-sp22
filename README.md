# RU Scheduled?

## Inspiration

The SAS Core Curriculum is a set of requirements all Rutgers SAS students must fulfill through a variety of courses across departments. As SAS students ourselves, we're familiar with the struggle of piecing together a cohesive schedule that satisfies as many cores as possible while balancing professor preferences and trying not to overload on credits. That's where RU Scheduled? comes into play.

## What it does

RU Scheduled? allows users to select the core requirements they have yet to fulfill. The web app will generate a list of class combinations that satisfy the cores specified based on Course Schedule Planner. Then, a user can select a combination and view course details and professor ratings from Rate My Professor.

## How we built it

We used Python to pull all currently offered courses and their details using the [Rutgers Course API](https://davidparsons.io/Rutgers-Course-API/). Each class that did not fulfill a core was filtered out of the list, and the remaining courses were serialized to avoid having to call the API each time the site is rendered. Using instructor details from the API, we additionally pulled Rate My Professor ratings from with the [RMP API](https://pypi.org/project/RateMyProfessorAPI/).

With all the data stored, we created a frontend using Bootstrap and Flask to display the best combination of courses at the user's request. 

## Challenges we ran into

- Flask is easy to use, but also not
- APIs don't work the way you want them to, sometimes

## What we learned

For a few of our past projects, we had wanted to develop web apps with Python backends but never got around to learning how to use Flask. For this project, we finally got around to it and realized how simple the linking process is. We're very proud of that!

## What's next for RU Scheduled?

There are a few features we did not have time to implement that would greatly improve user experience. 
1. Adding a status (open/closed) to each course's sections
2. Implementing scheduling conflict detection to only display schedules that do not have courses with time conflicts
3. Linking the department synopsis for each course if the link exists. Otherwise, we would link the course's department course catalog.
