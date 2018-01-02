# TSP-by-Particle-Swarm-Optimization
solve the TSP-52 problem by PSO
  
language: python(without pypy)  
  
benchline1: order1 crossover update method + update by neighbor best  
more about order1 crossover, see http://www.rubicite.com/Tutorials/GeneticAlgorithms/CrossoverOperators/Order1CrossoverOperator.aspx  
benchline2: origin crossover update method + update by 0.05 probability global best 0.95 neighbor best
  
main method: origin crossover update method + update by neighbor best  
origin crossover example:  
parent1 : 7 1 6 2 12 5 8 11 3 9 4 10  (good performance one)  
parent2 : 1 2 3 4 5 6 7 8 9 10 11 12  (random one)  
  
step 1: randomly choose 2 neighbor point of parent2(random one), and find the two points in parent1  
parent1 : 7 1 6 2 12 5 **8** 11 3 **9** 4 10  (good performance one)  
parent2 : 1 2 <del>3</del> 4 5 6 7 **8** **9** 10 <del>11</del> 12  (random one)  
  
step 2: insert the segment 8 11 3 9 into parent2  
new one : 1 2 4 5 6 7 **8** **11** **3** **9** 10 12  
  
  
performance:  
52 points tsp  

    main method:  
        about 10-12 seconds time used  
        56% global best result probability(in 50 test)  
    benchline1:  
        about 40 seconds time used  
        10% global best result probability(in 10 test)  
    benchline2:  
        about 9-12 seconds time used  
        7660.053970815396 best result(in 10 test) (global best 7544.365901904086)  
        
130 points tsp  

    main method:  
        about 200 seconds time used  
        6207.716767727842 best result(in 10 test) (global best 6110.86094968039)  
    benchline1:  
        about 17 mins time used  
        7059.734730861017 (1 test)  
    benchline2:  
        about 140 seconds time used  
        7889.851624633513 (1 test)  

