# JUET-Past-Year-s-Papers
The dreaded T1, T2, and T3 examination's papers come here to die.
<br><i>Please star this repository ⭐</i>
## About ⚡:
Up until 2012, our university folks used to maintain an archive of all the exam papers that were held all year around. That's not the case anymore. A week before each exam, I have seen students spending a majority of their time anxiously hunting for previous year's papers from their seniors. However, one couldn't easily get their hands these papers and the students who did, would only circulate it amongst their group, and increasing chances of scorng better.

That is when I thought of creating this repository to solve these problems. It will not only put all the past year's papers at your disposal but would also level the playing field for all.
## What you'll get here 🤑:
- Anytime, anywhere and unlimited access to all the T1, T2, T3 papers from several years.
- Learn to make open source contributions (optional, more about this in the next section).
- Via your open source contributions, you can improve your github profile (get badges, increase pull request count and more).

## How you can give back 🤝🏻: 
### <i>Please star the repository</i> ⭐. <br> <br>
This idea and repository can only thrive with the help of the community. I can only do so much myself and once I pass out, it will be upto the college students to maintain it. I urge and request everyone to contribute to this repo with the papers you have at present so that we can keep it up and running for our upcoming juniors.

## How to contribute (☞ﾟヮﾟ)☞ :

Some of the stuff below might seem like technical jargon to newbies. So, just bear and follow the steps clearly to make your pull request.  
1. You have a question paper and are willing to contribute. 
2. Make a single PDF file of all the pages.
3. File naming scheme: <i> <Exam_Name>  <Acronym_of_Subject></i>
<br>Eg: For a T1 examination paper of Data Structures, file name would be <i>T1_DS.pdf</i>
4. Fork this repository.
   <br> Steps 5-14 are commands that have to be run on Git Bash.
5. Clone the repository by running:
   ```
   git clone <url_of_your_fork>
   ``` 
7. Change the directory to "JUET-Past-Year-s-Papers" by running:
   ```
   cd JUET-Past-Year-s-Papers
   ``` 
9. Add a new upstream repo that will be synced with the fork. Run :
    ```
   git remote add upstream https://github.com/VinayakRaoDikshit/JUET-Past-Year-s-Papers.git
    ```
11. Create a new branch on your local and switch to it using:
    ```
    git checkout -b <branch_name>
    ```
13. Add your PDF file to the appropriate folder. Question papers in this repo are arranged in folders which follow a specific hierarchy as shown below. If you're creating a new folder, make sure it sticks to the guidelines.
    <br> Branches can be in the set : {CSE, ECE, ME, CE, CHE}
    <br> Exam names can be in the set: {T1, T2, T3}
    <br> Semesters can be in the range: [Sem I, Sem VIII]
    <br> Batch names can be of the form: "Batch 20-24", "Batch 21-25", "Batch 22-26" etc.
    <br><br><img  align ="middle" height=200 src="Images/three.png" alt="folder hierarchy"> 
15. Add your file to the staging area by running :
    ```
    git add -A
    ```
16. Commit your changes by running :
    ```
     git commit -m "your commit message"
    ```
17. Push your branch to the remote repository :
    ```
    git push origin <branch_name>:<branch_name>
    ```
18. Set up tracking for the new branch. Run:
    ```
    git branch -u origin/<branch_name>
    ```
19. Create a pull request on Github.

<br> Here are all the steps mentioned above, in action:<br><br>
<img width=75% src="Images/One.png" alt="Step guide" align="middle">
<br><br>
<img width=75% src="Images/Two.png" alt="Step guide">




