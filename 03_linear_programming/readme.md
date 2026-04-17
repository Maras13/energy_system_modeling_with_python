
<img width="611" height="1109" alt="Screenshot 2026-04-17 at 15 36 24" src="https://github.com/user-attachments/assets/c9b9111b-0608-4ee5-8012-ca2dda6a9cc1" />



<img width="570" height="641" alt="Screenshot 2026-04-17 at 15 36 40" src="https://github.com/user-attachments/assets/fe5fc231-1e63-43f8-af59-642695eada85" />



<img width="593" height="813" alt="Screenshot 2026-04-17 at 15 37 00" src="https://github.com/user-attachments/assets/bae09839-c1ae-42d7-ab57-0c5c9e382e4a" />




<img width="595" height="766" alt="Screenshot 2026-04-17 at 15 37 15" src="https://github.com/user-attachments/assets/f25263f0-eef1-44fd-a1e7-62b8445179dd" />


<img width="593" height="895" alt="Screenshot 2026-04-17 at 15 37 34" src="https://github.com/user-attachments/assets/274319e6-c601-4710-baa5-7cbc88872d66" />


<img width="607" height="921" alt="Screenshot 2026-04-17 at 15 37 51" src="https://github.com/user-attachments/assets/ab3f4155-7fed-4852-82a5-12b5afc45f1b" />


<img width="567" height="342" alt="Screenshot 2026-04-17 at 15 38 09" src="https://github.com/user-attachments/assets/48679c49-b67e-4225-a3ed-791c1dfa1abd" />




The core pedagogical idea is build the same model four times, each time more complex:
Week 1 is entirely pen-and-paper. Students solve a 2-plant dispatch LP by drawing the feasible region on graph paper and finding the optimal corner. This is crucial — if they can't see what the solver is doing geometrically, the code in Week 2 will feel like a black box. The key insight here is that every LP concept maps directly to an energy system concept: variables are generation levels, the objective is total cost, constraints are physical limits.
Week 2 translates that same problem into Linopy code. The big reveal is that students run their LP dispatch and their Module 2 merit_order_dispatch() side by side — the results are identical. This shows that the merit order was secretly solving an LP all along. With Linopy, you can create optimization models within Python that consist of decision variables, constraints, and optimization objectives, then solve using a variety of commercial and open-source solvers Fneum. HiGHS is the recommended solver — free, fast, and installs with a single pip command.
Week 3 is where LP pulls ahead of the merit order. Students extend to 24 hours and add two things the greedy approach can't handle: ramp rate limits (coal can't jump from 0 to full output in one hour) and battery storage (charge during cheap hours, discharge during expensive ones). The crucial concept is shadow prices — the dual value of each hour's demand constraint is the electricity price, derived mathematically rather than from the merit-order heuristic.
Week 4 teaches students to use the model rather than just build it. They run sensitivity analysis: what happens to costs, prices, and emissions when you add 5 GW of solar? Remove lignite? Double battery capacity? The exercise ends with a 1-page policy brief — forcing students to translate optimization results into actionable insights.
