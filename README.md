FFXIV-Crafting-Aide

what if i made the arrays into dictionaries, with the keys being the mat name and the value being the quantity?
what if i used an API to get the raw mat data (how to get it, what level gathering/monster, if it's sold by an npc and who/where for how much of what currancy)
i need to know how to call for certain information and how to have it display in a certain way 
so probably something like; user enters "bronze helm" and python runs to add the keys and combined values neccessary to the master list, 
then the api triggers and pulls the information for the keys and displays it in my user UI. 
then again, if i can use an API, do i really need to build my own database?

what do i want the UI to look like? 
something simple that reflects the users light/dark mode preferences. 
it needs to have my header added at the end of the coding process so it can't have it's own header... (right?)
so all this will be in the <main>
must have a field where the user can enter the craft they want to build (ex: maple clogs)
must have an add button, want it to display the results for all items currently in cart; like a calculator executes each line before the user inputs the next
so item "maple clogs" -> add -> displays results -> item "bronze helm" -> add -> dispays updated results -> etc
want the input field to automatically clear when add is clicked so user doesn't have to overwrite
