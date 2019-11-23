import os
import pandas as pd
import pickle
import matplotlib.pyplot as plt

n_values=[10,50,100,200,500]
g_values=[0.1,0.2,0.4,0.6,0.8]
b_values=[0.2,0.3,0.5,0.7,0.9]


b=0.5
g=0.2
p_n=[(i+1) for i in range(10)]
# The following lines generates csv files for all values of n for both algorithms from files generates by other code file
for n in n_values:
	ex=[]
	inex=[]
	cn=[]
	with  open('exact_info_'+str(n)+"_"+str(g)+"_"+str(b)+'.pickle', 'rb') as handle:
		d1=pickle.load(handle)
	with  open('inexact_info_'+str(n)+"_"+str(g)+"_"+str(b)+'.pickle', 'rb') as handle:
		d2=pickle.load(handle)
	for i in range(10):
		ex.append(d1[i][2])
		inex.append(d2[i][2])
		cn.append(d1[i][4]/d1[i][3])
	file=list(zip(p_n,ex,inex,cn))
	df=pd.DataFrame(file,columns=['Problem No.','Steps taken in exact','Steps taken in inexact',"Condition Number"])
	df.to_csv("results_"+str(n)+".csv",index=False)

# The following code generates the csv file containg average results for all n for both algo and it also generates plots for avg
# results in the file
ex=[]
inex=[]
for n in n_values:
	df=pd.read_csv('results_'+str(n)+".csv")
	e,ine=0,0
	for	i in range(10):
		e+=df['Steps taken in exact'][i]
		ine+=df['Steps taken in inexact'][i]
	ex.append(e/10)
	inex.append(ine/10)
file=list(zip(n_values,ex,inex))
df=pd.DataFrame(file,columns=['Value of n','Avg. Steps taken in exact','Avg. Steps taken in inexact'])
df.to_csv("Average_results"+".csv",index=False)
plt.plot(n_values,ex,label="exact")
plt.plot(n_values,inex,label="inexact")
plt.xlabel("Value of n")
plt.ylabel("avg no. of steps")
plt.title("Average performance by exact and inexact")
plt.legend()
plt.show()


# This code generates csv files for all n for variations of number of steps with variation of gamma 
for n in n_values:
	ans_gi=[]
	for g in g_values:
		ans_n=0
		for i in range(10):
			avg_steps_bi=0
			for b in b_values:
				with  open('inexact_info_'+str(n)+"_"+str(g)+"_"+str(b)+'.pickle', 'rb') as handle:
					d=pickle.load(handle)
				avg_steps_bi+=d[i][2]
			ans_n+=avg_steps_bi/5
		ans_gi.append(ans_n/10)
	file=list(zip(g_values,ans_gi))
	df=pd.DataFrame(file,columns=['gamma','avg_steps'])
	df.to_csv("gamma_"+str(n)+".csv",index=False)

# This code generates csv files for all n for variations of number of steps with variation of beta 
for n in n_values:
	ans_bi=[]
	for b in b_values:
		ans_n=0
		for i in range(10):
			avg_steps_gi=0
			for g in g_values:
				with  open('inexact_info_'+str(n)+"_"+str(g)+"_"+str(b)+'.pickle', 'rb') as handle:
					d=pickle.load(handle)
				avg_steps_gi+=d[i][2]
			ans_n+=avg_steps_gi/5
		ans_bi.append(ans_n/10)
	file=list(zip(b_values,ans_bi))
	df=pd.DataFrame(file,columns=['beta','avg_steps'])
	df.to_csv("beta_"+str(n)+".csv",index=False)


# This code generates plots for the variation of no . of steps with gamma and beta 
for n in n_values:
	df=pd.read_csv('beta_'+str(n)+".csv")
	x=df['beta']
	y=df['avg_steps']
	plt.plot(x,y)
	plt.xlabel("Value of beta")
	plt.ylabel("avg no. of steps")
	plt.title("Variations of No. of Steps with beta for n = "+str(n))
	plt.legend()
	plt.show()

	df=pd.read_csv('gamma_'+str(n)+".csv")
	x=df['gamma']
	y=df['avg_steps']
	plt.plot(x,y)
	plt.xlabel("Value of gamma")
	plt.ylabel("avg no. of steps")
	plt.title("Variations of No. of Steps with gamma for n = "+str(n))
	plt.legend()
	plt.show()



print('done')