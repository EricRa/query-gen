# query-gen

![Screenshot of the query-gen app on Windows 10.](/query-gen.png)

A web search query generator for searching multiple sites at once.  

NOTE: This is mainly being used for testing Python GUI things. You should probably be using something like this instead:

https://github.com/EricRa/searchgroups-bm



Currently queries are formatted for DuckDuckGo specifically, but they may work with other search engines as well.

Tested on Windows 10 and Linux Mint, but it should run on any desktop platform.

# Usage

Install dependencies from requirements.txt
	
Run the qgen.pyw script (.pyw file extension is just to prevent Windows from opening a separate console window)

To customize your own sites or add more, see the "checkboxes" section of the script and change the strings for each checkbox object.  I may add this customization to the UI at some point.
	
	
# Dependencies

	- icecream
	- customtkinter
	- pyperclip
	
