# Wordle Solver
## Introduction
In 2022, a word game by the name of “Wordle” gained widespread popularity. The game challenges the player to guess a five-lettered word within six attempts by repeatedly reducing the sample space of possible words based on the information returned in each attempt. This project uses concepts of information theory to solve the game. 

<b>Inspiration - 3Blue1Brown (https://www.youtube.com/watch?v=v68zYyaEmEA&t=708s) - All code is my own.</b>

The system works on the basic principles of information theory applied with the knowledge of computer science to find the game solution. Wordle has a list of 2309 five-lettered words from which the solution is randomly chosen. Each word is equally likely to be the solution. The objective is to reduce the sample space of possible words from 2309 words to a single word within six attempts using the information received from the game on each attempt. The ideal strategy is to select a word that reduces the sample space by the highest factor. For this, we associate a quantity called ‘Entropy’ with each word which, in simple terms, is the measure of average information given by a word. The term information quantifies the extent of reduction of the sample space.

The entropy of a random variable is the average level of "information" inherent to the variable's possible outcomes. Given a discrete random variable $X$, which takes values in the alphabet $\chi\$ and is distributed according to $p: \chi \rightarrow[0,1]:$

$H(X)=-\sum_{x \in \chi} p(x) \cdot \log p(x)$

For each word, there are 35 possible permutations of colors (green, yellow,’ and gray). $-p(x) \cdot \log p(x)$ is calculated for all $3^3$ permutations where $x$ is a particular permutation of colors, $p(x)$ gives the probability of getting $x$ and is given by

$p(x)=\frac{\text { no. of words satisfying } x}{\text { no. of words in the sample space }}$

and $-\log p(x)$ gives the bits of information associated with getting $x$. For every attempt, entropy is calculated for and associated with each word in the sample space, and the word with the highest entropy is selected. If there are multiple words with equal entropies, then one of them is randomly selected. This process is repeated for each attempt by reducing the sample space based on the information received from the last attempt until the correct solution is found. 

For the first attempt, since the sample space is large, the calculation for the entropy of each word takes some time. Therefore, entropy calculation for the first attempt is not carried out during the time of execution of the main script. Instead, data for entropy associated with each word is retrieved from a binary file that has been generated by another script.

- main.py - This is the main source code responsible for automatically generating Wordle games and implementing the above-mentioned procedure for finding solutions. It takes as input, from the user, the number of games to be played and solves for that many randomly generated games, it also displays the success rate in the end. It gives real-time graphical output through a pygame window.
                  
- bot_vr1.py - This script allows the user to solve for any Wordle game. Using this script, one can solve the online Wordle as well. The user has to input the word entered in the game and the colour combination received as a list - 0 for grey, 'green' for green, and 'yellow' for yellow (Enter a list of 5 # if the combination received is all grey). It shows the valid words ordered by their entropy values. The user should choose the word with the highest entropy value for the next move.

- wordle.py - Exact replication of the Wordle game. 

- initial_entropy_calc.py - For generating the entropy data required for the first attempt. first_attempt_data.dat has been generated by this script.

- wordle_words.txt - Contains the list of words from which the solution is chosen.

- possible_words.txt - Contains all possible five-lettered words. (Source- https://github.com/3b1b/videos/blob/master/_2022/wordle/data/possible_words.txt)

- first_attempt_data.dat - Entropy data for the first attempt. Generated by initial_entropy_calc.py. (Binary File)
  
- first_attempt_data.dat - Entropy data for the first attempt. Generated by initial_entropy_calc.py. (Readable Text File)

- demo - folder containing demos and results.

### Postscript 
- I did this project quite early in my programming journey. If I had to do this again, I will try to minimise the number of for loops and use numpy arrays for faster computation. 

- Also, I will incorporate more advanced methodology of solving the puzzle to make it more robust. As of now, it relies on the list of wordle words (~2300). I would like it to work on all possible 5-lettered words (~13000, most of these are very obscure) and still be able to give similar performance. This can be done by utilising the frequency of these words. This will be the next step in this project. 
    
    


