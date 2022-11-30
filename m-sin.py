import random
haft_sin=['samanoo' , 'sib' , 'sabze' , 'somagh' , 'sekke' , 'serke' , 'sonbol']
m = int(input())
randoms = random.sample(haft_sin , k=m)
print(f'\n'.join(randoms))