# Create a program to help the user type faster. Give him a word and ask him it five times. Check how many seconds
# it took him to type the word at each round. In the end , tell the user how many mistakes were made and show a chart
# with the typing speed evolution during the 5 seconds.
import matplotlib.pyplot as plt
import time as t

times = []
mistakes = 0
print('This program to help the user type faster. You will have to type the word "programming" as fats as you can for '
      'five times')
input("Press Enter to Start.")
while len(times) < 5:
    start = t.time()
    word = input('Type the word: ')
    end = t.time()
    time_elapsed = end - start

    times.append(time_elapsed)
    if word.lower() != 'programming':
        mistakes += 1

print('You made ' + str(mistakes) + ' mistake(s)')
print('Now lets see your evolution')
t.sleep(1.5)
x = [1, 2, 3, 4, 5]
y = times
plt.plot(x, y)
legends = ['1', '2', '3', '4', '5']
plt.xticks(x, legends)
plt.ylabel('Time in seconds')
plt.xlabel('Attempts')
plt.title('Typing Evolution')
plt.show()
