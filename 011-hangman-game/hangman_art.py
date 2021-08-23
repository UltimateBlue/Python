# create the hangman drawing variables
hangmanLogo = '''
 _
| |
| |_    __  _ _  _   __ _ _ __  __   __ _ _ __
| |_ \\ / __| | '_  \\/ _` | '_ \\/_ \\ / _` | '_ \\
| | | | (__| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__, _|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |
                    |___/
'''

hangmanShow = '''
  +---+
  |   |
      |
      |
      |
      |
==========
'''

indexes = [19,28,26,27,36,34]
parts = ['O', '\\','/','|', '\\','/']

# generate a random word
txt = 'Best known for his cerebral, often nonlinear, storytelling, acclaimed writer-director Christopher Nolan was born on July 30, 1970, in London, England. Over the course of 15 years of filmmaking, Nolan has gone from low-budget independent films to working on some of the biggest blockbusters ever made.\nAt 7 years old, Nolan began making short movies with his father\'s Super-8 camera. While studying English Literature at University College London, he shot 16-millimeter films at U.C.L.\'s film society, where he learned the guerrilla techniques he would later use to make his first feature, Following (1998), on a budget of around $6,000. The noir thriller was recognized at a number of international film festivals prior to its theatrical release and gained Nolan enough credibility that he was able to gather substantial financing for his next film.\nNolan\'s second film was Memento (2000), which he directed from his own screenplay based on a short story by his brother Jonathan. Starring Guy Pearce, the film brought Nolan numerous honors, including Academy Award and Golden Globe Award nominations for Best Original Screenplay. Nolan went on to direct the critically acclaimed psychological thriller, Insomnia (2002), starring Al Pacino, Robin Williams and Hilary Swank.\nThe turning point in Nolan\'s career occurred when he was awarded the chance to revive the Batman franchise in 2005. In Batman Begins (2005), Nolan brought a level of gravitas back to the iconic hero, and his gritty, modern interpretation was greeted with praise from fans and critics alike. Before moving on to a Batman sequel, Nolan directed, co-wrote, and produced the mystery thriller The Prestige (2006), starring Christian Bale and Hugh Jackman as magicians whose obsessive rivalry leads to tragedy and murder.\nIn 2008, Nolan directed, co-wrote, and produced The Dark Knight (2008) which went on to gross more than a billion dollars at the worldwide box office. Nolan was nominated for a Directors Guild of America (D.G.A.) Award, Writers Guild of America (W.G.A.) Award and Producers Guild of America (P.G.A.) Award, and the film also received eight Academy Award nominations.\nIn 2010, Nolan captivated audiences with the sci-fi thriller Inception (2010), which he directed and produced from his own original screenplay. The thought-provoking drama was a worldwide blockbuster, earning more than $800,000,000 and becoming one of the most discussed and debated films of the year. Among its many honors, Inception received four Academy Awards and eight nominations, including Best Picture and Best Screenplay. Nolan was recognized by his peers with D.G.A. and P.G.A. Award nominations, as well as a W.G.A. Award for his work on the film.'.lower()