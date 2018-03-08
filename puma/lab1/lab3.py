import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

sample_size = 50000
affected_low = 1 #1 to 100
affected_high = 100

gen = (x for x in range(affected_low, affected_high+1))

def animate(i):
    print('-----------------------------')
    sick_people = next(gen)
    p_sick = sick_people / sample_size
    print('Really sick %', p_sick)
    p_not_sick = 1 - p_sick
    print('Really not sick %', p_not_sick)
    
    sick = sample_size * p_sick
    not_sick = sample_size * p_not_sick
    print('Sick=', sick)
    print('Not sick=', not_sick)
    
    p_negative_sick = 0.01
    p_positive_sick = 1 - p_negative_sick
    
    p_positive_not_sick = 0.02
    p_negative_not_sick = 1 - p_positive_not_sick
    
    positive_sick = sick * p_positive_sick
    positive_not_sick = not_sick * p_positive_not_sick
    print('Positive sick=', positive_sick)
    print('Positive not sick=', positive_not_sick)
    
    negative_sick = sick * p_negative_sick
    negative_not_sick = not_sick * p_negative_not_sick
    print('Negative sick=', negative_sick)
    print('Negative not sick=', negative_not_sick)
    
    all_positive = positive_sick + positive_not_sick
    print('All positive =', all_positive)
    
    actually_sick = positive_sick / all_positive
    print('Actually sick =', actually_sick)
    
    p_actually_sick = actually_sick * 100
    print('Actually sick % =', p_actually_sick)
    print('-----------------------------')
    ax1.clear()
    ax1.set_ylim((0,100))
    ax1.set_ylabel('% actually sick')
    ax1.bar(1, p_actually_sick, width=0.8)
    
    
anim = animation.FuncAnimation(fig, animate, interval=100)
plt.show()