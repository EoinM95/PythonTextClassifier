#!/usr/bin/ env python
# -*- coding: utf-8 -*-
nom = "Murphy Eoin"
import Math
class Instance(object):

    def __init__(self, cat, coords) :
        """Constructeur de la classe.
        @param cat: a string
        @param coords: a tuple of floats
        """
        self.cat = cat
        self.coords = coords
	def __str__(self):
		return self.cat
	def distance(self, other):
		somme=0
		for (x,y) in zip(self.coords,other.coords):
			somme+=(x-y)**2
		return Math.sqrt(somme)
	def knn(self, k, listeInstances):
		liste=[]
		distances=[]
		indice=0
		maxDistance=0
		maxIndice=0
		for element in listeInstances:
			distanceEntre=distance(self, element)
			"""
			For first k elements just place them in the list
			For remaining elements: decide if they are closer than
			the furthest neighbour in the list and then
			recalculate the furthest neighbour
			"""
			if indice<k:
				liste[indice]=element
				distances[indice]=distanceEntre
				if distanceEntre>maxDistance:
					maxDistance=distanceEntre
					maxIndice=indice
				indice+=1
			else:
				if distanceEntre<maxDistance:
					liste[maxIndice]=element
					distances[maxIndice]=distanceEntre
					maxDistance=0
					maxIndice=0
					for i in range(0,k):
						if distance[i]>maxDistance:
							maxIndice=i
							maxDistance=distances[i]
		return liste		
				
def main():
    """Appelez vos fonctions depuis main()"""
def most_common(listInstances):
	catsEtFreqs={}
	for element in listInstance:
		if element.cat in catsEtFreqs:
			catsEtFreqs[element.cat]+=1
		else: 
			catsEtFreqs[element.cat]=1
	max=0
	maxKey=""
	for key in catsEtFreqs.keys():
		if catsEtFreqs[key]>max:
			max=catsEtFreqs[key]
			maxKey=key
	return maxKey

def classify_instance(k,instance,all_instances):
		plusProches=instance.knn(k,all_instances)
		return most_common(plusProches)

def read_instances(filename):
	liste=[]
	try:
		stream=open(filename)
		
		stream.close()
	except:
		print("Erreur de lecture")

		
"""Cette condition s'assure de n'appeler la fonction main
que lorsque le programme est appelé directement,
et non lorsqu'il est importé."""
if __name__ == "__main__":
    main()