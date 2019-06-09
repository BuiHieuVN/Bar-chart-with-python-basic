mport numpy as np 
import matplotlib.pyplot as plt

my_data = list(np.genfromtxt(r'/home/hieu/Desktop/browser.csv',dtype=str,delimiter=","))

browser = my_data.pop(0)

my_data = np.asfarray(my_data,float) #convert numpy.str to numpy.float64

for i in range(len(my_data)):
    Browser_Count = dict({(key,value) for (key,value) in zip(browser,my_data[i])})

    Percentage_Sorted = sorted(Browser_Count.values(), reverse=True)

    Browser_Sorted = sorted(Browser_Count, key=Browser_Count.__getitem__, reverse=True)

    Index_Browser = range(len(Browser_Count))

    ax = plt.subplots() 
    width = 0.75
    plt.xlim(0, 100)
    my_color = ['red','pink','pink','pink','pink']

    plt.barh(Index_Browser, Percentage_Sorted, width, color = my_color)
    plt.yticks(Index_Browser, Browser_Sorted)
    #ax.set_yticklabels(Browser_Sorted, minor=False)

    for a, b in zip(Index_Browser, Percentage_Sorted):
        plt.text(b + 3.5, a, b, ha='center')

    plt.ylabel('Browsers')
    plt.xlabel('Percentage of using')
    plt.title('The most popular Browser')
    #plt.legend(handles)
    plt.savefig(str(len(my_data)-i)+'.png')
    plt.show()
