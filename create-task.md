{% include navigation.html %}

Create Task: Username Generator

3 a.
3 b.
3. WRITTEN RESPONSES
3.a.i.
Oftentimes, the hardest part of registering for certain video games, websites, social media, etc. can be the simple
process of brainstorming a username. This specialized username-generating program was made on Replit in order to
remedy this, or at the very least, offer inspiration for those that are struggling with this process.
3.a.ii.
Various prompts are returned to the user in order to generate a type of username, giving the user a specialized username
that fits their wants/needs, an improvement compared to random generators and websites. The video also showcases a
feature that checks for a yes/no response in order to ensure that a mistake in input does not disrupt the output that is
desired.
3.a.iii.
The input is the yes/no responses given to the prompts that are generated for the user. The output of the program, or the
specialized username, is given based on the responses that are received.
3.b.i.
3.b.ii.
3.b.iii.
The name of the list being used in this response is "array_no_space_concise_uni."
3.b.iv.
The data contained in the list represent the possible usernames that can be generated if the user wants a username that
has no spaces and is concise and unique.
3.b.v.
This array is called through the function "no_space_concise_uni(choice)," which allows for a random integer representing
one of the stored values (in context, usernames that are concise, unique, and do not have a space) within the list to be
selected. Without the implementation of this array, there would be nothing to be selected through in order to give a
random output for a username. Therefore, this array is needed in order to provide a random output that is in line with the
user's inputs. For the program to function without this array, the values in the array would need to be stored within the
function itself, meaning that a random value must be selected through a list that is within the function every time the code
is run, making the function and logic needed more complex.
3 c.
3.c.i.
3.c.ii.
3.c.iii.
The procedure generates a username that has spaces and is unique. This helps contribute to the overall functionality of
the program by generating a type of username that the user chose with their inputs.
3.c.iv.
The algorithm implemented in this procedure first initializes the global index variable that will be referenced, then prints a
statement that thanks the user for playing and generates their username through the built-in random integer function,
where the index of the array being accessed, array_space_uni, and its length deducting 1 are the minimum and
maximum values that can be chosen as a random integer, representing a random username stored in the array. A while
loop for when the index is less than 2 is implemented, followed by a prompt that asks if the user desires to reroll, keeping
in mind that duplicates are possible due to another random integer being chosen again, which could be the same as the
one previously chosen. A try-except statement block is added to catch any assertion errors not reading Y/y or N/n, the
only possible inputs. An if-else statement is then made. If the response to the prompt is yes, the index is incremented by
1 and the function is called again to be repeated, but this time without the reroll prompt as the while loop no longer
applies. If the response is no, then the program ends.
3 d.
3.d.i.
First call:
The function is first called in the function "space(choice)," which calls the function if the user desires a username that has
a space and is unique.
Second call:
The function is also called within itself in a recursive loop if the user wishes to reroll. Once called, the index will increment
to 2, breaking out of the while loop.
3 d.ii.
Condition(s) tested by first call:
It is already preestablished at this point that the user wants a username with a space. Thus, the condition being tested in
the first call is whether or not the user wants a username that is unique or not.
Condition(s) tested by second call:
In the second call, the condition being tested is if the user has rerolled their username or not. If this function call is run
once, then it is determined that the user has requested a reroll, and there will not be an option to reroll again.
3.d.iii.
Results of the first call:
When the function is called in this specific instance, the output given is a username and a prompt that asks if the user
desires to reroll.
Results of the second call:
The result of the second call is giving an output that displays the username without a prompt that asks if the user desires
to reroll since they have just done so.
