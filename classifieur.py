#! python3
# -*- coding: utf-8 -*-
string="!/usr/bin/ env python"
nom = "Murphy Eoin"
import math
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
	def setCat(self,cat):
		self.cat=cat
	def getCoords(self):
		return self.coords
	def distance(self, other):
		somme=0
		for (x,y) in zip(self.coords,other.coords):
			somme+=(x-y)**2
		return math.sqrt(somme)
	def knn(self, k, listeInstances):
		liste=[]
		distances=[]
		indice=0
		maxDistance=0
		maxIndice=0
		for element in listeInstances:
			distanceEntre=self.distance(element)
			"""
			For first k elements just place them in the list
			For remaining elements: decide if they are closer than
			the furthest neighbour in the list and then
			recalculate the furthest neighbour
			"""
			if indice<k:
				liste.append(element)
				distances.append(distanceEntre)
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
						if distances[i]>maxDistance:
							maxIndice=i
							maxDistance=distances[i]
		return liste		
		
def main():
	allInstances=read_instances("orangeTest.txt")
	print(str(allInstances[0]))
	predict(allInstances[:9],allInstances[10:])
	classif=eval_classif(allInstances[:9],allInstances[10:])
	print(str(classif)+"% classified correctly")
def most_common(listInstances):
	catsEtFreqs={}
	for element in listInstances:
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
	with open(filename) as stream:
		for line in stream:
			elements=line.split()
			#for element in elements:
			#	#print(element)
			cat=elements[0]
			coords=[]
			for c in elements[1:]:
				coords.append(float(c))
			nextInstance=Instance(cat,coords)
			liste.append(nextInstance)		
	return liste		
	
def predict(listInstancesConnues,listInstancesInconnues):
    for instance in listInstancesInconnues:
        instance.setCat(classify_instance(10,instance,listInstancesConnues))
        listInstancesConnues.append(instance)
			
def eval_classif(ref_instances,pred_instances):
	correct=0
	incorrect=0
	for r in ref_instances:
		for p in pred_instances:
			if(r.getCoords()==p.getCoords()):
				if(str(r)==str(p)):
					correct+=1
				else:
					incorrect+=1
	total=correct+incorrect
	return (correct/total)*100	
		
		
"""Cette condition s'assure de n'appeler la fonction main
que lorsque le programme est appelé directement,
et non lorsqu'il est importé."""
if __name__ == "__main__":
	main()
