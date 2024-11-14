import math

def nombres_premiers(N):
  """
  Génère tous les nombres premiers inférieurs ou égaux à N.

  Args:
    N: Un entier naturel.

  Returns:
    Une liste contenant tous les nombres premiers inférieurs ou égaux à N.
  """

  premiers = []
  #	Boucle externe: Itère sur tous les nombres de 2 à N.
  for nombre in range(2, N+1):
    est_premier = True
    #	Boucle interne: Itère sur tous les diviseurs potentiels jusqu'à la racine carrée du nombre.
    for diviseur in range(2, int(math.sqrt(nombre))+1):
      """
        Test de primalité: Si un diviseur est trouvé, le nombre n'est pas premier.
        Ajout à la liste: Si aucun diviseur n'est trouvé, le nombre est ajouté à la liste des nombres premiers.

      """
      if nombre % diviseur == 0:
        est_premier = False
        break
    if est_premier:
      premiers.append(nombre)
  return premiers
# Exemple d'utilisation :
"""
cete ligne permet de rentrer le nombre de N,
et print de permet d'affichier les nombres premiers en sorties
"""
resultat = nombres_premiers(150)
print(resultat)

