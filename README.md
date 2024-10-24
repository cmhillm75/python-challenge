# python-challenge list of sources used in creating the "main.py" script for the PyBank assignment  

* 1 PyBank_starter - provided the outline for opening, reading file and  
the commented steps to create the complete script.  

* 2 For establishing the variables utilized in class activities Evr_List_Comprehensions,  
lists_solution.py and <https://www.pythoncheatsheet.org/cheatsheet/basics#variables> as required  
to create a changeable amount for months and change.  

* 3 To read each row 1 at a time, needed to define what the variables will do. By adding 1 to total_months,  
and using next(reader) for each row, beginning at first_row, months.append adds the total # of months.

* 4 Google search the moving variables of net change and profit and loss required calculating the lines
 <https://stackoverflow.com/questions/27160565/reading-csv-file-in-python-and-summing-the-values-in-the-row>
 this link showed an example of rowtotal += int(column) and allowed to apply to our total_net which is the sum of profits.

* 5 To calculate the sum of the monthly profit changes, variable prev_profit_loss first need to get the sum of the
monthly differences and divide by the length of the row. Will be an integer (int) and start at 1st row, 2nd column.
<https://www.pythoncheatsheet.org/cheatsheet/built-in-functions> sum / len and had to apply round, 2 to get 0000.00 format.

* 6 Step 5 requires creating a "change" value to track the net changes and profits and we can use append to add together.
By using int(row[1]) it defines the value at our starting point to calculate the monthly change and the total profits/losses.
so to get the change we then would use the initial value int(row[1]) and subtract profits_loss to obtain the change from
each month.

* 7 To determine how to calculate the "greatest" portion of assigment, per Slack discussion, question was asked and
reference in "Ask the Class" response was to utilize max and min as the basis to determine and having obtained the changes
in calcuating the profits and losses and net changes, we could apply the max and min to get the answer.

* 8 to use info from step 7 I received the IndexError: list index out of range, searched for solution and obtained
<https://decodepython.com/python-indexerror-how-to-fix-it-with-strategies-and-solutions-code-sample/?form=MG0AV3> source
which provided if else as option to correct and applied to changes which translates to calculating the greatest values.

* 9 To find the greatest increase/decrease need to use index of changes to obtain the position where the highest and lowest value
resides so months[changes.index(greatest_increase) + 1] gives us the month after the greatest increase which is the month for
for the increase. If we don't include the month it happened, output would only provide the integer value.

* 10 For generating the output and printing the results reviewed Class Activities, Mod 3 - 08  
"Evr_GraduatingFunctions" for instructor demonstrations in how to set up the print functions using (f"String: {value to print}")  
, also provided insight on how to get output to print out in 2 decimals .2f and input $ as example used 1 decimal place .1f  
and % as a string with the variable. Followed the template for txt_file.write(output) for the items we wanted to print.

* 11 I chose f strings as we utilized this form of string printing mostly in class. I had issue getting strings to
print line by line, <https://www.pythoncheatsheet.org/cheatsheet/manipulating-strings> provided 'n\'. as a way to print new lines.

* PyPoll applied the script creating process used in the PyBank taking the starter code and breaking it out
as there is only 2 variables at work, votes and the candidate name with total_votes being the sum of
individual votes.

* Tested the code with the counter and it took longer to run than without so removed it from the final code.

* Already having completed the PyBank and using the sample HW we had the terminal and txt print out format
therefore utilized as setup.

* To create the loop, used enumarate since it is a built in function to keep track of each index as
we iterate thru the csv candidate column.,<https://www.pythoncheatsheet.org/builtin/enumerate>>

* To create the winner count started as none and again used a for loop to get each candidate and their votes.