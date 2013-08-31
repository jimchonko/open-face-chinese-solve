# test if a hand is misset 
def test_misset(hand):
	import eval_hand
	top=eval_hand.eval_hand(hand[0])
	middle=eval_hand.eval_hand(hand[1])
	bottom=eval_hand.eval_hand(hand[2])
	if top[2]<=middle[2]<=bottom[2]:
		misset_flag=0
	else:
		misset_flag=1
		
	return misset_flag