# optimize placement of new card to maximize bonus points with no other players
from deck import *

def single_place_card(hand, used_cards, card):
	import copy
	import calc_points
	import create_permutation
	
	# define the penalty for misstep and bonus for fantasyland
	n_pts_misset=-10
	n_pts_fantasy=10
	
	original_hand = copy.deepcopy(hand)
	
	# the card can be placed in the top , middle, or bottom
	# calculate all permutations 
	place = ['top','middle','bottom']
	
	n_top=len(list(filter(('').__ne__, hand[0])))
	n_middle=len(list(filter(('').__ne__, hand[1])))
	n_bottom=len(list(filter(('').__ne__, hand[2])))
	
	top_ind=0;
	middle_ind=0;
	bottom_ind=0;
	
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
	
	permute=copy.deepcopy([hand])
	#print(permute)
	
	if top_ind==1:
		permute.append([new_top,hand[1],hand[2]])
	if middle_ind==1:
		permute.append([hand[0],new_middle,hand[2]])
	if bottom_ind==1:
		permute.append([hand[0],hand[1],new_bottom])
	
	#print('length of permute: ',len(permute))
	#print('permute: ',permute)
	#print('length of last: ',len(permute[-1]))
	
	# remove existing hand from permutations
	del permute[0]
	#print('after remove original hand state: ',permute)
	
	# determine remaining cards in deck
	unavailable_cards = [list(filter(('').__ne__, hand[0])), list(filter(('').__ne__, hand[1])), list(filter(('').__ne__, hand[2])), used_cards, [card]]
	
	available_cards = copy.deepcopy(deck)
	
	for x in unavailable_cards:
		for y in x:
			available_cards = list(filter((y).__ne__, available_cards))
	
	print('unavailable cards: ', unavailable_cards)
	print('available cards: ', available_cards)
	
	n_available_cards = len(available_cards)
	print('number of available cards: ', n_available_cards)
	
	# loops to create full set of permutations
	n_remaining_draw = 13-(n_top+n_middle+n_bottom+1)
	print('number of remaining cards to draw: ', n_remaining_draw)
	
	final_permutations=create_permutation.create_permutation(permute, available_cards)
	
	print('end of first permutation', len(final_permutations))
	
	
	static2=copy.deepcopy(final_permutations)
	
	if n_remaining_draw>=2:
		count=0
		print('start second loop')
		for hand2 in static2:
			count=count+1
			
			#print('loop number: ', count)
			#print('this is hand for second loop: ', hand2)
				
			# determine remaining cards in deck
			unavailable_cards = [list(filter(('').__ne__, hand2[0])), list(filter(('').__ne__, hand2[1])), list(filter(('').__ne__, hand2[2])), used_cards, [card]]
			
			available_cards = copy.deepcopy(deck)
			
			for x in unavailable_cards:
				for y in x:
					available_cards = list(filter((y).__ne__, available_cards))
			
			#print('unavailable cards: ', unavailable_cards)
			#print('available cards: ', available_cards)
			
			n_available_cards = len(available_cards)
			#print('number of available cards: ', n_available_cards)
				
			final_permutations.extend(create_permutation.create_permutation([hand2], available_cards))
	
		del final_permutations[0:len(static2)]
		print('number of permutations: ', len(final_permutations))
		print('finished creating permutations')
	
	static3=copy.deepcopy(final_permutations)
	
	if n_remaining_draw>=3:
		count=0
		print('start third loop')
		for hand3 in static3:
			count=count+1
			
			#print('loop number: ', count)
			#print('this is hand for third loop: ', hand3)
				
			# determine remaining cards in deck
			unavailable_cards = [list(filter(('').__ne__, hand3[0])), list(filter(('').__ne__, hand3[1])), list(filter(('').__ne__, hand3[2])), used_cards, [card]]
			
			available_cards = copy.deepcopy(deck)
			
			for x in unavailable_cards:
				for y in x:
					available_cards = list(filter((y).__ne__, available_cards))
			
			#print('unavailable cards: ', unavailable_cards)
			#print('available cards: ', available_cards)
			
			n_available_cards = len(available_cards)
			#print('number of available cards: ', n_available_cards)
				
			final_permutations.extend(create_permutation.create_permutation([hand3], available_cards))
	
		del final_permutations[0:len(static3)]
		print('number of permutations: ', len(final_permutations))
		print('finished creating permutations')
	
	
	
	
	# evaluate final hands of all permutations
	# count=0
	points=[-99]
	for hand in final_permutations:
		#count=count+1
		#print(count, hand)
		points.append(calc_points.calc_points(hand, n_pts_misset, n_pts_fantasy))
	
	del points[0]
	#print(points)
	
	# calculate expectation values
	# for each placement of the new card calculate the expected number of points 
	cnt_top=0
	cnt_middle=0
	cnt_bottom=0
	
	tot_top=0
	tot_middle=0
	tot_bottom=0
	

	count=0
	for hand in final_permutations:
	
		# calculate the expectation value for that placement
		if hand[0].count(card)>0:
			cnt_top=cnt_top+1
			tot_top=tot_top+points[count]
		elif hand[1].count(card)>0:
			cnt_middle=cnt_middle+1
			tot_middle=tot_middle+points[count]
		elif hand[2].count(card)>0:
			cnt_bottom=cnt_bottom+1
			tot_bottom=tot_bottom+points[count]
			
		count=count+1
	
	print('count top: ', cnt_top)
	
	if cnt_top>0:
		expected_top = tot_top/cnt_top
	else:
		expected_top = -99
	if cnt_middle>0:
		expected_middle = tot_middle/cnt_middle
	else:
		expected_middle = -99
	if cnt_bottom:
		expected_bottom = tot_bottom/cnt_bottom
	else:
		expected_bottom = -99
	
	print('expected top: ', expected_top)
	print('expected middle: ', expected_middle)
	print('expected bottom: ', expected_bottom)
	
	print('card: ', card)
	print('hand: ', original_hand)
	
	return permute
	