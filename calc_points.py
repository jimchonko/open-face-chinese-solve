# calculate bonus points for a hand

from bonus import *

def calc_points(hand, pts_misset, pts_fantasy):
	import test_misset
	import eval_hand
	import calc_bonus_points
	
	misset_flg=test_misset.test_misset(hand)
	fantasy_flg=0
	
	#print('misset flag: ', misset_flg)
	
	if misset_flg==1:
		top_bonus_pts=0
		middle_bonus_pts=0
		bottom_bonus_pts=0
		
	else:
		top=eval_hand.eval_hand(hand[0])
		middle=eval_hand.eval_hand(hand[1])
		bottom=eval_hand.eval_hand(hand[2])
		
		if top[2]>=24: # pair of queens up top grants fantasyland
			fantasy_flg=1
		
		# bonus points 	
		top_bonus_pts=calc_bonus_points.calc_bonus_points(top, 'top')
		middle_bonus_pts=calc_bonus_points.calc_bonus_points(middle, 'middle')
		bottom_bonus_pts=calc_bonus_points.calc_bonus_points(bottom, 'bottom')
	
	# sum the total bonus points
	total_pts = top_bonus_pts + middle_bonus_pts + bottom_bonus_pts + pts_misset*misset_flg + pts_fantasy*fantasy_flg
		
	#print('top bonus: ', top_bonus_pts)
	#print('middle bonus: ', middle_bonus_pts)
	#print('bottom bonus: ', bottom_bonus_pts)
	#print('misset penalty: ', pts_misset*misset_flg)
	#print('fantasy bonus: ', pts_fantasy*fantasy_flg)
	#print('total points: ', total_pts)
	
	return total_pts
	