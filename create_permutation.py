# creates hand permutations 

def create_permutation(permutations, available_cards):
	import copy
	
	n_original_permutations=len(permutations)
	#print('number of existing permutations: ', n_original_permutations)
	
	new_permutations = copy.deepcopy(permutations)
	
	# loop through all hands in existing set of permutations
	for hand in permutations:

		# sort hand
		hand[0].sort()
		hand[1].sort()
		hand[2].sort()
		
		hand[0].reverse()
		hand[1].reverse()
		hand[2].reverse()
	
		# the card can be placed in the top , middle, or bottom
		# calculate all permutations 
		place = ['top','middle','bottom']
		
		n_top=len(list(filter(('').__ne__, hand[0])))
		n_middle=len(list(filter(('').__ne__, hand[1])))
		n_bottom=len(list(filter(('').__ne__, hand[2])))
				
		top_ind=0;
		middle_ind=0;
		bottom_ind=0;
			
		for card in available_cards:			
					
			new_top=copy.deepcopy(hand[0])
			new_middle=copy.deepcopy(hand[1])
			new_bottom=copy.deepcopy(hand[2])
			
			if n_top<3:
				top_ind=1
				new_top[n_top]=card
				#print(new_top)
			
			if n_middle<5:
				middle_ind=1
				new_middle[n_middle]=card
				#print(new_middle)
			
			if n_bottom<5:
				bottom_ind=1
				new_bottom[n_bottom]=card
				#print(new_bottom)
			
			if top_ind==1:
				new_permutations.append([new_top,hand[1],hand[2]])
			if middle_ind==1:
				new_permutations.append([hand[0],new_middle,hand[2]])
			if bottom_ind==1:
				new_permutations.append([hand[0],hand[1],new_bottom])
			
	# remove existing hand from permutations
	del new_permutations[0:n_original_permutations]
	#print('new permutations: ',new_permutations[0])
	#print('new permutations: ',new_permutations[-1])
	#print('number of permutations: ',len(new_permutations))
	
	return new_permutations
	