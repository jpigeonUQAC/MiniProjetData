# Mini-projet Python

## Auteurs - PIGJ10119809, Pigeon, Jérome

## Compatibilité 
Compatible avec Python 3.13

## Utilisation 
Ce logiciel a été codé sous Python.<br>
Voici le lien pour télécharger la version de Python : <br>https://www.python.org/downloads/<br>
Les librairies nécessaires sont Pandas, Numpy, Plotly.express, Seaborn et Matplotlib. Si vous utiliser Jupyter Notebook, les commandes pour installées ces dépendances sont déjà incluses et vous n'avez qu'à exécuter la première cellule. Sinon vous pouvez ignorer la première cellule Jupyter.<br>
Si vous désirez utiliser le fichier Python Streamlit, vous devrez vous assurer d'avoir la librairie Streamlit d'installées avec le terminal Windows.<br>
Ce programme a été testé sur Windows 10 sous le logiciel Anaconda Jupyter pour le fichier Notebook.
-----------
Instruction Notebook : Pour ouvrir le fichier notebook, ouvrez d'abord l'application Anaconda, puis Jupyter Notebook. Puis sélectionnez le Notebook.ipynb dans le dossier présent.<br>
Pour exécuter le code, il vous suffit d'appuyer sur "Run cells" avec le bouton Play. Cette commande exécutera toutes les cellules de code un par un et vous affichera le résultat du code de la cellule.<br>
Le code est programmé de cette manière : Installation des dépendances, chargement du fichier csv, nettoyage des données (mettre les noms uniforms es première lettre majuscule, retirer les doubles, mettre les montants négatifs en positif, retirer les noms d'hopitaux en double et affecter les dates comme valeur en format date).<br>
Par la suite, le programme commence par faire une analyse des patients : age, genre et type sanguin. Le programme effectura aussi des graphique pour représenter les fréquences et les proportions, mais aussi faire des analyses entre les autres données. Certaines conclusions apparaitront en commentaire du code.<br>
Une fois cette analyse faite, une analyse des données hospitalière est fait par le meme processus.<br>
Ensuite, une analyse financière selon les cout des patients est effectuée.<br>
Enfin, nous terminons avec quelques données statistiques générales résumant certains points vus précédemment et nous terminons, enfin, sur une analyse rapide des cas abnormaux.
<br>
Instruction Streamlit : Pour ouvrir le fichier Python Streamlit, ouvrez le terminal et inscrivez "Streamlit run Streamlit.py". Ceci vous ouvrira une page sur votre navigateur web.<br>
Le fichier Streamlit ouvrira, comme mentionné plus tot, une page sur votre navigateur web. Cette page sera composée d'une section à gauche permettant de sélectionner une donnée à visualisé en forme graphique. Ces données sont directement tirées du fichier notebook. Une fois le bouton appuyé, les données appaitrons sur l'écran principale au centre.<br>
Le dernier bouton permet de visualiser certaines statistiques générales sur l'ensemble des données.<br>
-----------
Information pertinante : Les data brutes sont toujours accessibles. Une copy du DataFrame a été fait au début pour conserver l'intégrité des données. De plus, j'ai décidé de ne pas faire un nettoyage plus approfondit des noms d'hopitaux pour éviter de supprimer des noms similaires qui ne sont pas associés ensembles. Le nettoyage, à ce niveau, ce fait seulement lorsque les noms d'hopitaux continnent les memes mots, mais pas dans le meme ordre (exemple LLC Smith et Smith LLC).<br>
Pour le nettoyage, j'ai aussi convertit les montants négatifs en montants positifs pour garder les données. Il s'agit assurément d'une erreure d'entrée, car il est impossible de facturer négativement une personne.<br>
Enfin, au niveau du nettoyage, j'ai décidé de simplement éliminer les lignes qui contenaient exactement les meme données. Ce ménage est fait au début de toutes les autres pour éviter de supprimer des données que j'ai modifiées et qui deviendraient similaires..<br>
