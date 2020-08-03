# kwkscrape
Simple twitter scraping tool using GetOldTweets3 through Windows command line (can only be used on windows)
How to use: (if you're comfortable with using argparse, just use the --help command with the scrapecmd file)
1. go to command line, or "cmd" in the windows search bar
2. change directory with "cd" command, to whichever folder the scrapecmd file is located in
3. when directory is set, type "python scrapecmd.py"
4. the parameters for scraping are "--username", "--count", and "--filename"
5. "--username" defines the associated @ name with the account you wish to scrape, not the display name
6. "--count" defines the amount of tweets you wish to scrape from the account
7. "--filename" defines the name of the output file that will contain the tweets; the filetype must be included and csv or txt files work the best.
