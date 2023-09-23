#####################################
####### CHALLENGING PROBLEM 2 #######                                 
####### SHREYA BIRTHARE 34060222 ####
#####################################

import threading
import requests

# Define the number of URLs to generate and dump
NUM_URLS = 50000
POPULATION_SIZE = 6700000

# Function to generate and dump a single URL
def generate_and_dump_url(url_count):
    try:
        url = "https://en.wikipedia.org/wiki/Special:Random"
        response = requests.get(url)
        if response.status_code == 200:
            # Extract the article keyword from the URL
            random_url = response.url
            article_keyword = random_url.split("https://en.wikipedia.org/wiki/", 1)[1]
            
            # Write the article keyword to the file
            with open("generated_urls_{}.txt".format(NUM_URLS), "a") as f:
                f.write(article_keyword + "\n")
            print(f"Generated and dumped URL {url_count}")
    except Exception as e:
        print(f"Error generating/dumping URL {url_count}: {str(e)}")

def main():
    # Create and start multiple threads to generate and dump URLs concurrently
    threads = []
    for i in range(NUM_URLS):
        thread = threading.Thread(target=generate_and_dump_url, args=(i + 1, ))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

# Function to claculate observed numeber of pairwise duplicates
def calculateObservedDuplicates(article_list):
    article_frequency = {}
    for article in article_list:
        if article in article_frequency:
            article_frequency[article]+=1
        else:
            article_frequency[article]=1
    
    sum=float(0)

    for article in article_frequency.items():
        dupe=article[1]
        if(dupe>1):
            sum+= float((dupe*(dupe-1))/2)
    return sum

# Function to calculate expected number of pairwise duplicates using the formula given in class: (w)(w-1)/2n
def calculateExpectedDuplicates(sample_size, population_size):
    return float((sample_size* (sample_size-1))/(2*population_size))

if __name__ == "__main__":
    # Dump data into file
    with open("generated_urls_50000_2.txt".format(NUM_URLS), "w+") as f:
        f.write("")
    main()

    # Open the generated file to calculate observed number of pairwise duplicates
    f=open("generated_urls_{}.txt".format(NUM_URLS), "r")
    print("#########STATS FOR generated_urls_{}.txt#########\n".format(NUM_URLS))
    observedDuplicates= calculateObservedDuplicates(f.readlines())
    expectedDuplicates= calculateExpectedDuplicates(NUM_URLS, POPULATION_SIZE)
    print("*****Observed Duplicates: {} *****\n".format(observedDuplicates))
    print("*****Expected Duplicates: {} *****\n".format(expectedDuplicates))