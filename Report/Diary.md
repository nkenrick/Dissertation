# Project Diary

## First Term 

**26 & 27/09/2022**

- Added work to project plan. More reading done on agents.

**28/09/2022** 
- Added all work done over summer from personal github to project GitLab. Worked more on project plan. 

**29/09/2022** - Worked on project plan.

**03/10/2022**
 - Reading on search algorithms

**04/10/2022** 
- Updated maze generation to allow cycles to occur (due to findings from reading seems this is a much better way of doing it).

**06/10/2022** 
- Had meeting with supervisor and acted on feedback 

**10/10/2022** 
- Used TDD to write and test my BFS algorithm 

**11/10/2022** 
- Finshed visualization for BFS agent

**14/10/2022** 
- Reading and implimentation of graph visulaization for BFS

**20/10/2022** 
- Start writing about search algorithms and wrok done so far

**21/10/2022** 
- Continued writing report. Wrote and visualised Depth first search

**24/10/2022** 
- Wrote more in depth backround theory in report. 

**31/10/2022** 
- Began experiments on search algorithms that have been done. Saved mazes used on these tests as they will need to stay the same for all coming experiments.

**1 & 2/11/2022** 
- Started working on uniform cost search. so far works on returning the correct shortest distance to node, however i have yet implimented a prority queue 
so could make it more efficient. Also does not return any useful information that can be applied to and agent/ or that and agent can use.

**7/11/2022** 
- Worked on visualisation for UCS, this is now done. Ran into problem where nodes were stored but i did not store the path to them, making the visualistion bad as is was not clear the path the agent was taking. Made changes to my graph rep file to make the path to each node now stored.

**14/11/2022**
- Finished all coding needed in UWBranch and merged back. Wrote another test in report and started writing abstract properly

**15/11/2022**
- Thought of new ways to experiment with the algorithms in order to write about them in report, made changes to code to do this. Actual testing needs to be done on same machine as previous experiments.

**17/11/2022** 
- Worked on repoort. Added appendicies. Started looking ahead at informed searches.

**24-27/11/2022** 
- Began work on presentation. Reacted to feedback given in latest meeting. Improved introduction, added history and examples. 

## Christmas holidays 
- Refactored code to get rid of dead code. Put all searches in classes and changed the way that an agent is instansiated. This will hep with future agent and search implimentations. The agent now calls the search rather than being passed one, this is more accurate to how agents should behave and is clearer to use.

## Term Two
**11/01/23** 
- Began writing and researching informed searches to get a good understanding on how they work before I attempt to create one.

**16/01/23** 
- Built on code used for uniform cost searh to hety A star search. I ran into a problem where i previously hadnt commented my code well enough making it difficult to undersand so I added comments in. I also had the realisation that using a linked list may have been easier, as i thought before.

**18/01/23** 
- Created branch refactor in an attempt to turn graph into a linked list representation, i was able to do alot in a linked list format. Howver when i tried to manipulate this for my search algorithms I quickly realised this is actually alot less ideal and the dictionary representation I have is simpler and good way to do it.

**23/01/23** 
- Ran into problem with A* when trying to add multiple goals, was able to fix this by changing:
  - How the agent passes the graph to the search 
  - How the graph algorithm identifies nodes
                
**24/01/23 - 3/02/23** 
- Worked on getting tests correct. I realised that the results I initally had were incorrect as the UCS had thr same problem as the informed searches where is didnt register the goal as a node andtherefore never found it meansing it finshed instantly. First A* tests done/underway.

**06-10/02/23** 
- Worked on algorithm to traverse entire maze. Tried chinese postman - Too many computations wouldn't work on larger mazes. Tried dikstra - wrong strategy works like BFS not what i was after. In the end it chooses the closest node to it at each point, meaning at the end it has to back track a little but not alot. Most optimal
algorithm I was able to impliment that happpens in an acceptable time frame.

**14/02/23** 
- Ran all tests (took 30 hours to run). Used these results to plot graphs and explained them in report.

**18-21/02/23**
- Worked on reflex agents. Currently the 'player agent' is able to collect all goals and finish without being caught by the 'enemy agent'. Im order to get this to work I had to edit the maze generation to have no dead ends, this makes it look less like a traditional maze, but is still a maze non the less. Inspiration for this idea was based on how pac-man looks. I also had several attepts at breaking deadlocks. 
  
**23/02/23**
-Implimented min max algorithm for player agent. Had to do alot of reading and had several attempts at getting the correct values out of the evaluation function oin order for the agent to work properly.

**25/02/23**
- Added pruning to player agent - simply added if statement which was easier then i was fearing :) after this worked i added the minmax algorithm with pruning to the enemy agent. It only calls this algorithm when it is in 'chase' mode.

**March**
- March was spent finishing up the report - acting on feedback. Also implemented reinforcement learning.