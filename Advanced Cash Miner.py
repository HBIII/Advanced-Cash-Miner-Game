from copy import deepcopy
#import time

#start = time.time()								#for debugging purpose

def grid_update(grid):

	
	dummy_grid=[[0 for r in range(grid_size)]for c in range(grid_size)]			#making a copy of the original grid for checking any changes in updated grid

	policy_mat=[["" for x in range(grid_size)] for y in range(grid_size)]		#policy matrix that will denote the direction to move for the virtual figure
	if grid_size<126:
		while (dummy_grid!=grid):
			dummy_grid=deepcopy(grid)

			for i in range(grid_size):
				for j in range(grid_size):
					
					max_utility=-1000000.0
					
					#if the current state that is being considered is wall or terminal state
					if grid[i][j]==-131313.0 or terminal[i][j]=="t":
						if grid[i][j]==-131313.0:							#checking if there is a wall
							policy_mat[i][j]="N"
						else:												#there is a terminal state
							policy_mat[i][j]="E"

					#regular states
					else:

						# Up 
						if i-1>=0:
							utility1=0.0				#utility value for going 45 degrees anti-clockwise  grid[i-1][j-1]
							utility2=0.0				#utility value for going 45 degrees clockwise   grid[i-1][j+1]

							if j-1>=0:								#checking if the 45 degree anti-clockwise move has boundary if j-1>=0
								if grid[i-1][j-1]==-131313.0:				#checking if the 45 degree anti-clockwise move on the grid is a wall (value=-131313.0)
									utility1=0.5 * (1-p) * grid[i][j]
								else:
									utility1=0.5 * (1-p) * grid[i-1][j-1]
							else:
								utility1=0.5*(1-p)*grid[i][j]

							if j+1<=grid_size-1:					#checking if the 45 degree clockwise move has boundary if j+1<=grid_size-1
								if grid[i-1][j+1]==-131313.0:				#checking if the 45 degree clockwise move on the grid is a wall (value=-131313.0) 
									utility2=0.5 * (1-p) * grid[i][j]
								else:
									utility2=0.5 * (1-p) * grid[i-1][j+1]
							else:
								utility2=0.5 * (1-p) * grid[i][j]

							if grid[i-1][j]!=-131313.0:		#checking if there is wall of this particular block of grid       
								totalutil=reward+(gamma * (p * grid[i-1][j]+utility1+utility2))
								if totalutil>max_utility:
									max_utility=totalutil
									policy_mat[i][j]="U"
							else:
								totalutil=reward+(gamma * (p * grid[i][j]+utility1+utility2))
								if totalutil>max_utility:
									max_utility=totalutil
									policy_mat[i][j]="U"
						else:							#There is boundary
							utility1=0.0						#utility value for going 45 degrees anti-clockwise	grid[i-1][j-1]
							utility2=0.0						#utility value for going 45 degrees clockwise   grid[i-1][j+1]

							utility1=0.5 * (1-p) * grid[i][j]
							utility2=0.5 * (1-p) * grid[i][j]
							
							totalutil=reward+(gamma * (p * grid[i][j]+utility1+utility2))
							if totalutil>max_utility:
								max_utility=totalutil
								policy_mat[i][j]="U"

						#Down
						if i+1<=grid_size-1: 
							utility1=0.0				#utility value for going 45 degrees anti-clockwise  grid[i-1][j-1]
							utility2=0.0				#utility value for going 45 degrees clockwise   grid[i-1][j+1]

							if j-1>=0:								#checking if the 45 degree anti-clockwise move has boundary 
								if grid[i+1][j-1]==-131313.0:				#checking if the 45 degree anti-clockwise move on the grid is a wall (value=-131313.0)
									utility1=0.5 * (1-p) * grid[i][j]
								else:
									utility1=0.5 * (1-p) * grid[i+1][j-1]
							else:
								utility1=0.5 * (1-p) * grid[i][j]

							if j+1<=grid_size-1:					#checking if the 45 degree clockwise move has boundary 
								if grid[i+1][j+1]==-131313.0:				#checking if the 45 degree clockwise move on the grid is a wall (value=-131313.0)
									utility2=0.5 * (1-p) * grid[i][j]
								else:
									utility2=0.5 * (1-p) * grid[i+1][j+1]
							else:
								utility2= 0.5 * (1-p) * grid[i][j]

							if grid[i+1][j]!=-131313.0:		#checking if there is wall of this particular block of grid
								totalutil=reward + (gamma * (p * grid[i+1][j] +utility1+utility2))
								if totalutil > max_utility:
									max_utility = totalutil
									policy_mat[i][j] = "D"
							else:
								totalutil=reward+(gamma * (p * grid[i][j]+utility1+utility2))
								if totalutil > max_utility:
									max_utility = totalutil
									policy_mat[i][j] = "D"

						else:							#there is boundary
							utility1=0.0					#utility value for going 45 degrees anti-clockwise
							utility2=0.0					#utility value for going 45 degrees clockwise
							if i+1>grid_size-1:
								utility1=0.5 * (1-p) * grid[i][j]
								utility2=0.5 * (1-p) * grid[i][j]
							
							totalutil=reward+(gamma * (p * grid[i][j]+utility1+utility2))

							if totalutil > max_utility:
								max_utility = totalutil
								policy_mat[i][j]="D"

						#Left
						if j-1>=0:
							utility1=0.0					#utility value for going 45 degrees anti-clockwise
							utility2=0.0					#utility value for going 45 degrees clockwise

							if i-1>=0:						#checking if the 45 degree anti-clockwise move has boundary 					
								if grid[i-1][j-1]==-131313.0:			#checking if the 45 degree anti-clockwise move on the grid is a wall
									utility1=0.5 * (1-p) * grid[i][j]
								else:
									utility1=0.5 * (1-p) * grid[i-1][j-1]
							else:
								utility1=0.5 * (1-p) * grid[i][j]

							if i+1<=grid_size-1:			#checking if the 45 degree clockwise move has boundary 
								if grid[i+1][j-1]==-131313.0:			#checking if the 45 degree clockwise move on the grid is a wall
									utility2=0.5 * (1-p) * grid[i][j]
								else:
									utility2=0.5 * (1-p) * grid[i+1][j-1]
							else:
								utility2=0.5 * (1-p) * grid[i][j]

							if grid[i][j-1]!=-131313.0:	#checking if there is wall on this particular block of grid
								totalutil=reward+(gamma * (p * grid[i][j-1]+utility1+utility2))
								if totalutil>max_utility:
									max_utility=totalutil
									policy_mat[i][j]="L"
							else:						#Either there is boundary or there is wall of this particular block of grid
								totalutil=reward+(gamma * (p * grid[i][j]+utility1+utility2))
								if totalutil>max_utility:
									max_utility=totalutil
									policy_mat[i][j]="L"								
								
						else:
							utility1=0.0						#utility value for going 45 degrees anti-clockwise
							utility2=0.0						#utility value for going 45 degrees clockwise

							utility1=0.5 * (1-p) * grid[i][j]
							utility2=0.5 * (1-p) * grid[i][j]

							totalutil=reward+(gamma *(p*grid[i][j]+utility1+utility2))
							if totalutil>max_utility:
								max_utility=totalutil
								policy_mat[i][j]="L"

						#Right
						if j+1<=grid_size-1:
							utility1=0.0											#utility value for going 45 degrees anti-clockwise
							utility2=0.0											#utility value for going 45 degrees clockwise
							
							if i-1>=0:						#checking if the 45 degree anti-clockwise move has boundary 
								if grid[i-1][j+1]==-131313.0:
									utility1=0.5*(1-p)*grid[i][j]
								else:
									utility1=0.5*(1-p)*grid[i-1][j+1]
							else:
								utility1=0.5*(1-p)*grid[i][j]

							if i+1<=grid_size-1:			#checking if the 45 degree clockwise move has boundary 
								if grid[i+1][j+1]==-131313.0:
									utility2=0.5*(1-p)*grid[i][j]
								else:
									utility2= 0.5 * (1-p) * grid[i+1][j+1]
							else:
								utility2=0.5*(1-p)*grid[i][j]

						 	if grid[i][j+1]!=-131313.0:		#checking if there is boundry or if there is wall of this particular block of grid
								
								totalutil=reward+(gamma*(p*grid[i][j+1]+utility1+utility2))
								if totalutil>max_utility:
									max_utility=totalutil
									policy_mat[i][j]="R"
							else:

								totalutil=reward+(gamma*(p*grid[i][j]+utility1+utility2))
								if totalutil>max_utility:
									max_utility=totalutil
									policy_mat[i][j]="R"
						else:										#Either there is boundary or there is wall of this particular block of grid
							utility1=0.0									#utility value for going 45 degrees anti-clockwise
							utility2=0.0
															#utility value for going 45 degrees clockwise
							utility1=0.5*(1-p)*grid[i][j]
							utility2=0.5*(1-p)*grid[i][j]

							totalutil=reward+(gamma*(p*grid[i][j]+utility1+utility2))

							if totalutil>max_utility:
								max_utility=totalutil
								policy_mat[i][j]="R"
						grid[i][j]=max_utility
		return policy_mat
	else:
		while (True):

			dummy_grid=deepcopy(grid)
			delta=0
			epsilon=0.01

			for i in range(grid_size):
				for j in range(grid_size):
					
					max_utility=-100000.0
					
					#if the current state that is being considered is wall or terminal state

					if grid[i][j]==-131313.0 or terminal[i][j]=="t":
						if grid[i][j]==-131313.0:							#checking if there is a wall
							policy_mat[i][j]="N"
						else:												#there is a terminal state
							policy_mat[i][j]="E"

					#regular states

					else:

						# Up 
						if i-1>=0:
							utility1=0.0				#utility value for going 45 degrees anti-clockwise  grid[i-1][j-1]
							utility2=0.0				#utility value for going 45 degrees clockwise   grid[i-1][j+1]

							if j-1>=0:								#checking if the 45 degree anti-clockwise move has boundary if j-1>=0
								if grid[i-1][j-1]==-131313.0:				#checking if the 45 degree anti-clockwise move on the grid is a wall (value=-131313.0)
									utility1=0.5 * (1-p) * grid[i][j]
								else:
									utility1=0.5 * (1-p) * grid[i-1][j-1]
							else:
								utility1=0.5*(1-p)*grid[i][j]

							if j+1<=grid_size-1:					#checking if the 45 degree clockwise move has boundary if j+1<=grid_size-1
								if grid[i-1][j+1]==-131313.0:				#checking if the 45 degree clockwise move on the grid is a wall (value=-131313.0) 
									utility2=0.5 * (1-p) * grid[i][j]
								else:
									utility2=0.5 * (1-p) * grid[i-1][j+1]
							else:
								utility2=0.5 * (1-p) * grid[i][j]

							if grid[i-1][j]!=-131313.0:		#checking if there is boundary or if there is wall of this particular block of grid       
								totalutil=reward+(gamma * (p * grid[i-1][j]+utility1+utility2))
								if totalutil>max_utility:
									max_utility=totalutil
									policy_mat[i][j]="U"
							else:
								totalutil=reward+(gamma * (p * grid[i][j]+utility1+utility2))
								if totalutil>max_utility:
									max_utility=totalutil
									policy_mat[i][j]="U"
						else:									#Either there is boundary or there is wall of this particular block of grid
							utility1=0.0								#utility value for going 45 degrees anti-clockwise	grid[i-1][j-1]
							utility2=0.0								#utility value for going 45 degrees clockwise   grid[i-1][j+1]

							utility1=0.5 * (1-p) * grid[i][j]
							utility2=0.5 * (1-p) * grid[i][j]
							
							totalutil=reward+(gamma * (p * grid[i][j]+utility1+utility2))
							if totalutil>max_utility:
								max_utility=totalutil
								policy_mat[i][j]="U"

						#Down
						if i+1<=grid_size-1: 
							utility1=0.0				#utility value for going 45 degrees anti-clockwise  grid[i-1][j-1]
							utility2=0.0				#utility value for going 45 degrees clockwise   grid[i-1][j+1]

							if j-1>=0:								#checking if the 45 degree anti-clockwise move has boundary 
								if grid[i+1][j-1]==-131313.0:				#checking if the 45 degree anti-clockwise move on the grid is a wall (value=-131313.0)
									utility1=0.5 * (1-p) * grid[i][j]
								else:
									utility1=0.5 * (1-p) * grid[i+1][j-1]
							else:
								utility1=0.5 * (1-p) * grid[i][j]

							if j+1<=grid_size-1:					#checking if the 45 degree clockwise move has boundary 
								if grid[i+1][j+1]==-131313.0:				#checking if the 45 degree clockwise move on the grid is a wall (value=-131313.0)
									utility2=0.5 * (1-p) * grid[i][j]
								else:
									utility2=0.5 * (1-p) * grid[i+1][j+1]
							else:
								utility2= 0.5 * (1-p) * grid[i][j]

							if grid[i+1][j]!=-131313.0:		#checking if there is boundry or if there is wall of this particular block of grid
								totalutil=reward + (gamma * (p * grid[i+1][j] +utility1+utility2))
								if totalutil > max_utility:
									max_utility = totalutil
									policy_mat[i][j] = "D"
							else:
								totalutil=reward+(gamma * (p * grid[i][j]+utility1+utility2))
								if totalutil > max_utility:
									max_utility = totalutil
									policy_mat[i][j] = "D"

						else:									#Either there is boundary or there is wall of this particular block of grid
							utility1=0.0								#utility value for going 45 degrees anti-clockwise
							utility2=0.0								#utility value for going 45 degrees clockwise
							if i+1>grid_size-1:
								utility1=0.5 * (1-p) * grid[i][j]
								utility2=0.5 * (1-p) * grid[i][j]
							
							totalutil=reward+(gamma * (p * grid[i][j]+utility1+utility2))

							if totalutil > max_utility:
								max_utility = totalutil
								policy_mat[i][j]="D"

						#Left
						if j-1>=0:
							utility1=0.0								#utility value for going 45 degrees anti-clockwise
							utility2=0.0								#utility value for going 45 degrees clockwise

							if i-1>=0:						#checking if the 45 degree anti-clockwise move has boundary 					
								if grid[i-1][j-1]==-131313.0:			#checking if the 45 degree anti-clockwise move on the grid is a wall
									utility1=0.5 * (1-p) * grid[i][j]
								else:
									utility1=0.5 * (1-p) * grid[i-1][j-1]
							else:
								utility1=0.5 * (1-p) * grid[i][j]

							if i+1<=grid_size-1:			#checking if the 45 degree clockwise move has boundary 
								if grid[i+1][j-1]==-131313.0:			#checking if the 45 degree clockwise move on the grid is a wall
									utility2=0.5 * (1-p) * grid[i][j]
								else:
									utility2=0.5 * (1-p) * grid[i+1][j-1]
							else:
								utility2=0.5 * (1-p) * grid[i][j]

							if grid[i][j-1]!=-131313.0:	#checking if there is wall on this particular block of grid
								totalutil=reward+(gamma * (p * grid[i][j-1]+utility1+utility2))
								if totalutil>max_utility:
									max_utility=totalutil
									policy_mat[i][j]="L"
							else:						#Either there is boundary or there is wall of this particular block of grid
								totalutil=reward+(gamma * (p * grid[i][j]+utility1+utility2))
								if totalutil>max_utility:
									max_utility=totalutil
									policy_mat[i][j]="L"								
								
						else:
							utility1=0.0						#utility value for going 45 degrees anti-clockwise
							utility2=0.0						#utility value for going 45 degrees clockwise

							utility1=0.5 * (1-p) * grid[i][j]
							utility2=0.5 * (1-p) * grid[i][j]

							totalutil=reward+(gamma *(p*grid[i][j]+utility1+utility2))
							if totalutil>max_utility:
								max_utility=totalutil
								policy_mat[i][j]="L"

						#Right
						if j+1<=grid_size-1:
							utility1=0.0											#utility value for going 45 degrees anti-clockwise
							utility2=0.0											#utility value for going 45 degrees clockwise
							
							if i-1>=0:						#checking if the 45 degree anti-clockwise move has boundary 
								if grid[i-1][j+1]==-131313.0:
									utility1=0.5*(1-p)*grid[i][j]
								else:
									utility1=0.5*(1-p)*grid[i-1][j+1]
							else:
								utility1=0.5*(1-p)*grid[i][j]

							if i+1<=grid_size-1:			#checking if the 45 degree clockwise move has boundary 
								if grid[i+1][j+1]==-131313.0:
									utility2=0.5*(1-p)*grid[i][j]
								else:
									utility2= 0.5 * (1-p) * grid[i+1][j+1]
							else:
								utility2=0.5*(1-p)*grid[i][j]

						 	if grid[i][j+1]!=-131313.0:		#checking if there is boundry or if there is wall of this particular block of grid
								
								totalutil=reward+(gamma*(p*grid[i][j+1]+utility1+utility2))
								if totalutil>max_utility:
									max_utility=totalutil
									policy_mat[i][j]="R"
							else:

								totalutil=reward+(gamma*(p*grid[i][j]+utility1+utility2))
								if totalutil>max_utility:
									max_utility=totalutil
									policy_mat[i][j]="R"
						else:										#Either there is boundary or there is wall of this particular block of grid
							utility1=0.0									#utility value for going 45 degrees anti-clockwise
							utility2=0.0
															#utility value for going 45 degrees clockwise
							utility1=0.5*(1-p)*grid[i][j]
							utility2=0.5*(1-p)*grid[i][j]

							totalutil=reward+(gamma*(p*grid[i][j]+utility1+utility2))

							if totalutil>max_utility:
								max_utility=totalutil
								policy_mat[i][j]="R"
						grid[i][j]=max_utility
						delta = max(delta, abs(grid[i][j] - dummy_grid[i][j]))
			#counter=counter+1
		#print counter
			if delta < epsilon * (1 - gamma) / gamma:
				return policy_mat

with open('input.txt','r') as input_file:

	input =  input_file.read().splitlines()
	#print input
	counter=0
	grid_size=int(input[counter])
	counter=counter+1
	grid=[[0.0 for i in range(grid_size)]for j in range(grid_size)]
	
	totalwalls= int(input[counter])
	counter=counter+1
	for i in range(totalwalls):
		temp=input[i+counter].split(",")
		x=int(temp[0])
		y=int(temp[1])
		grid[x-1][y-1]=-131313.0
	counter=counter+totalwalls
	
	totalterminalstates= int(input[counter])
	counter=counter+1
	terminal = [['' for x in range(grid_size)] for y in range(grid_size)]
	#print totalterminalstates
	for i in range(totalterminalstates):
		temp=input[i+counter].split(",")
		x=int(temp[0])
		y=int(temp[1])
		grid[x-1][y-1]=float(temp[2])
		terminal[x-1][y-1]="t"
	#print grid
	counter=counter+totalterminalstates

	p =float(input[counter])
	counter=counter+1
	reward=float(input[counter])
	counter=counter+1
	gamma=float(input[counter])
	#print p,gamma,reward

	policy_grid=grid_update(grid)

	w=open('output.txt','w')
	for i in range (grid_size):
		for j in range (grid_size):
			w.write(str(policy_grid[i][j]))
			# to check whether we have reached the end of the row, if j!=(grid_size-1)
			if j!=(grid_size-1):
				w.write(",")
		# to check whether we have reached the end of the row, if i!=(grid_size-1)
		if i!=(grid_size-1):		
			w.write("\n")