# compare two hands and calculate points won or lost

from bonus import *

def compare_hand(hand1,hand2):
	import test_misset
	import eval_hand
	import calc_bonus_points
	
	misset_flg1=test_misset.test_misset(hand1)
	misset_flg2=test_misset.test_misset(hand2)
	
	print(misset_flg1)
	print(misset_flg2)
	
	
	if misset_flg1==1 and misset_flg2==1:
		top_pts=0
		middle_pts=0
		bottom_pts=0
		sweep_ind=0
		
	elif misset_flg1==1:	
		top_pts=-1
		middle_pts=-1
		bottom_pts=-1
		sweep_ind=-1
		
		top2=eval_hand.eval_hand(hand2[0])
		middle2=eval_hand.eval_hand(hand2[1])
		bottom2=eval_hand.eval_hand(hand2[2])
		
		# bonus points 
		top1_bonus_pts=0
		middle1_bonus_pts=0
		bottom1_bonus_pts=0
		
		top2_bonus_pts=calc_bonus_points.calc_bonus_points(top2, 'top')
		middle2_bonus_pts=calc_bonus_points.calc_bonus_points(middle2, 'middle')
		bottom2_bonus_pts=calc_bonus_points.calc_bonus_points(bottom2, 'bottom')
		
	elif misset_flg2==1:
		top1=eval_hand.eval_hand(hand1[0])
		middle1=eval_hand.eval_hand(hand1[1])
		bottom1=eval_hand.eval_hand(hand1[2])
		sweep_ind=1
		
		# bonus points 
		top1_bonus_pts=calc_bonus_points.calc_bonus_points(top1, 'top')
		middle1_bonus_pts=calc_bonus_points.calc_bonus_points(middle1, 'middle')
		bottom1_bonus_pts=calc_bonus_points.calc_bonus_points(bottom1, 'bottom')
		
		top2_bonus_pts=0
		middle2_bonus_pts=0
		bottom2_bonus_pts=0
		
	else:
		top1=eval_hand.eval_hand(hand1[0])
		middle1=eval_hand.eval_hand(hand1[1])
		bottom1=eval_hand.eval_hand(hand1[2])
		top2=eval_hand.eval_hand(hand2[0])
		middle2=eval_hand.eval_hand(hand2[1])
		bottom2=eval_hand.eval_hand(hand2[2])
		
		if top1[2]>top2[2]:
			top_pts=1
		elif top1[2]<top2[2]:
			top_pts=-1
		else:
			top_pts=0
			
		if middle1[2]>middle2[2]:
			middle_pts=1
		elif middle1[2]<middle2[2]:
			middle_pts=-1
		else:
			middle_pts=0
			
		if bottom1[2]>bottom2[2]:
			bottom_pts=1
		elif bottom1[2]<bottom2[2]:
			bottom_pts=-1
		else:
			bottom_pts=0
		
		# determine if there was a sweep or not
		if top_pts==1 and middle_pts==1 and bottom_pts==1:
			sweep_ind=1
		elif top_pts==-1 and middle_pts==-1 and bottom_pts==-1:
			sweep_ind=-1
		else:
			sweep_ind=0
		
		# bonus points 	
		top1_bonus_pts=calc_bonus_points.calc_bonus_points(top1, 'top')
		middle1_bonus_pts=calc_bonus_points.calc_bonus_points(middle1, 'middle')
		bottom1_bonus_pts=calc_bonus_points.calc_bonus_points(bottom1, 'bottom')
		
		top2_bonus_pts=calc_bonus_points.calc_bonus_points(top2, 'top')
		middle2_bonus_pts=calc_bonus_points.calc_bonus_points(middle2, 'middle')
		bottom2_bonus_pts=calc_bonus_points.calc_bonus_points(bottom2, 'bottom')	
	
	# sum the total points won or lost
	total_pts = top_pts + middle_pts + bottom_pts + sweep_ind*b_sweep + top1_bonus_pts + middle1_bonus_pts + bottom1_bonus_pts - top2_bonus_pts - middle2_bonus_pts - bottom2_bonus_pts
		
	print('top points: ', top_pts)
	print('middle points: ', middle_pts)
	print('bottom points: ', bottom_pts)
	print('sweep points: ', sweep_ind*b_sweep)
	print('top bonus: ', top1_bonus_pts-top2_bonus_pts)
	print('middle bonus: ', middle1_bonus_pts-middle2_bonus_pts)
	print('bottom bonus: ', bottom1_bonus_pts-bottom2_bonus_pts)
	
		
	return total_pts
	