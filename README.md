# info-extractor

## What is it? 
Personal project that uses OpenAI's API to give summaries on PowerPoint (.ppt, .pptx) and PDF (.pdf) files.

## Why?
Its always a hassle to reread hundreds of PowerPoint slides before exams, so why not use the "power" of AI to summarize.

Its important to be aware that the model I am using is *not perfect*, it will not include EVERY piece of information that
you would want to study before an exam. I would personally use this tool to *suplement* my revisions, not entirely
replace them. 

## How?
Simply pass the relative or full path of a .pptx, .ppt, or .pdf file when running the program.
<pre>
python main.py "full_or_relative_path_to_my_file"
</pre>

Next, the file path is validated, making sure it exists and is an allowed file type.

After this has happenend, we check if the file is empty, and if it isn't, the file is parsed using tika. A regular expression for newlines is used to clean up the text (parsing PowerPoints leaves massive amounts of newlines ^_^).

Then, we do the AI part. This is split into two steps. 
   Firstly, I authenticate by passing my OpenAI API Key and Org ID into openai (which are hidden from the reader), and then I am ready to go (it really is that simple).

   Secondly, I make a chat completion request. OpenAI makes it very easy to use their models. All of the AI related code is in the 'ai' folder. Its pretty small, and most of the LOC in there are error handling. Currently, this project is using the 
   gpt-3.5-turbo-16k model as I realized that I needed to handle a massive amount of tokens.

Once a response has been received from the model, it is error checked. For chat completion requests, we must make sure that the "finish_reason" is nothing other than "stop". More info about that here: https://platform.openai.com/docs/guides/gpt/chat-completions-api 

Finally, I gave myself two ways to view the response. 
   Option 1: Response is printed out in the terminal
   Option 2: Response is saved as a .txt file in the same directory as the initial file.

## Future Features?
Token Size Handling: What happens if I want to get a summary of a MASSIVE file?
   I chose a model with a massive token limit in order to not want to face this issue. I already handle the cases where
   the initial prompt is over the token limit, and if the response + prompt is over the token limit. I do not have a concrete idea of how I want to solve this problem, but I have a faint clue:  Split the input up (by some factor), and then send multiple requests of the split input. Each of these requests would need a prompt that builds on the previous request. In order to get the final output I would have to "glue" each response together to get a final response.

UI: Why must I paste a filepath?
   True, I could see myself in the future adding some sort of UI or GUI in order to make it easier to find and pass in a file. 

Multiplicity: Why only one file?
   Adding support for parsing more than one file at a time might be a valuable thing to have. The runtime would be very long, meaning its only use case would be to pass in a lot of files at once and then leave the program running for a while. The issue with this is that an error may happen at any point, and cause everything to stop. 

Prompt Selection: Only one prompt?
   Having a default prompt is nice and makes it easy to use. Maybe I would want to add the ability to make your own prompts. This could be useful if you don't just want a summary out of a file, but want something specific; like the ability to pinpoint and target specific topics or areas of interest in a file. 
   Example: "Give me all the information regarding ducks' mating calls from this paper on ducks."


## Does it work?
Yes. In the 'examples' folder there is a real PowerPoint that I had made in a previous class about the book "The Right Stuff". Also in that folder is the saved .txt file that has the model's response. 
Note: Since it is using AI, every new response to the same prompt will be different.


