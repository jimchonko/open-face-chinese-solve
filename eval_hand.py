# evaluate the strength of a hand
# eval_hand.eval_hand(['as','ks','qs','js','ts'])
def eval_hand(hand):
	# sort hand
	hand.sort()

	# load collections module
	import collections
	
	# create list of card values
	values=[x[0].upper() for x in hand]
	#print(values)
	
	# create list of suits
	suits=[x[1].upper() for x in hand]
	#print(suits)
	
	# evaluate strength
	
	# duplicate card values
	value_cnt=collections.Counter(values)
	#print(value_cnt)
	
	# duplicate suit values
	suit_cnt=collections.Counter(suits)
	#print(suit_cnt)
	
	# determine the card value with the most duplicates
	primary_count=1
	primary_value=values[0]
	for card in values:
		if value_cnt[card]>primary_count:
			primary_value=card
			primary_count=value_cnt[card]
			
	#print(primary_value)
	#print(primary_count)
	
	# determine the card value with the second most duplicates

	secondary_values=list(filter((primary_value).__ne__, values))
	#print(secondary_values)
	
	secondary_value_cnt=collections.Counter(secondary_values)
	#print(secondary_value_cnt)
	
	secondary_count=1
	secondary_value=secondary_values[0]
	for secondary_card in secondary_values:
		if secondary_value_cnt[secondary_card]>secondary_count:
			secondary_value=secondary_card
			secondary_count=secondary_value_cnt[secondary_card]
			
	#print(secondary_value)
	#print(secondary_count)
	
	
	# determine the suit with the most duplicates
	suit_count=1
	for card in suits:
		if suit_cnt[card]==5:
			flush_ind=1
		else:
			flush_ind=0
			
	#print(flush_ind)
	
	
	# determine if there is a straight
	min_value=99
	max_value=0
		
	for card in values:
		if card=='2':
			num_value=1
		elif card=='3':
			num_value=2
		elif card=='4':
			num_value=3
		elif card=='5':
			num_value=4
		elif card=='6':
			num_value=5
		elif card=='7':
			num_value=6
		elif card=='8':
			num_value=7
		elif card=='9':
			num_value=8
		elif card=='T':
			num_value=9
		elif card=='J':
			num_value=10
		elif card=='Q':
			num_value=11
		elif card=='K':
			num_value=12
		elif card=='A':
			num_value=13
			
		if num_value>max_value:
			max_value=num_value
		if num_value<min_value:
			min_value=num_value
		
	if max_value-min_value==4:
		straight_ind=1
	else:
		straight_ind=0
				

	# determine the type of hand
	if straight_ind==1 and flush_ind==1 and len(hand)==5:
		type='straightflush'
	elif flush_ind==1 and len(hand)==5:
		type='flush'
	elif straight_ind==1 and len(hand)==5:
		type='straight'
	elif primary_count==4:
		type='quads'
	elif primary_count==3 and secondary_count==2:
		type='fullhouse'
	elif primary_count==3:
		type='set'
	elif primary_count==2 and secondary_count==2:
		type='twopair'
	elif primary_count==2:
		type='pair'
	else:
		type='highcard'
	
	# determine the value of the hand
	if type=='straightflush' or type=='flush' or type=='straight' or type=='highcard':
		value=max_value
	elif type=='quads' or type=='fullhouse' or type=='set' or type=='twopair' or type=='pair':
		if primary_value=='2':
			value=1
		elif primary_value=='3':
			value=2
		elif primary_value=='4':
			value=3
		elif primary_value=='5':
			value=4
		elif primary_value=='6':
			value=5
		elif primary_value=='7':
			value=6
		elif primary_value=='8':
			value=7
		elif primary_value=='9':
			value=8
		elif primary_value=='T':
			value=9
		elif primary_value=='J':
			value=10
		elif primary_value=='Q':
			value=11
		elif primary_value=='K':
			value=12
		elif primary_value=='A':
			value=13
		
		
	if type=='highcard':
		strength=value
	elif type=='pair':
		strength=value+13
	elif type=='twopair':
		strength=value+13*2
	elif type=='set':
		strength=value+13*3
	elif type=='straight':
		strength=value+13*4
	elif type=='flush':
		strength=value+13*5
	elif type=='fullhouse':
		strength=value+13*6
	elif type=='quads':
		strength=value+13*7
	elif type=='straightflush':
		strength=value+13*8
		
	return type, value, strength
	